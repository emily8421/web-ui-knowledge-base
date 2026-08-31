#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract-tokens.py — collect-source 技能的静态设计令牌抽取脚本（Plan A）。

用途：抓取一个公开网页的 HTML 与前 N 份样式表，抽取设计令牌（CSS 自定义属性）、
调色板、字体栈、字号 / 圆角 / 间距 / 动效时长分布，输出中文 Markdown 报告
（尾部附机器可读 JSON 块）。零第三方依赖，仅标准库；不写盘，仅 stdout。

退出码：0 = 正常（含「疑似 JS 渲染 → 走 Plan B」提示）；2 = 抓取失败；3 = 参数错误。

用法（Windows git-bash，务必带 PYTHONUTF8=1 防乱码）：
  PYTHONUTF8=1 python .claude/skills/collect-source/scripts/extract-tokens.py <URL> \
      [--max-css 5] [--max-css-bytes 2097152] [--timeout 15] [--format md|json] [--ua <str>]

边界（与 SOP-collect.md 一致）：只抓浏览器本就会请求的静态资源（HTML + ≤5 份 CSS）；
诚实 UA；无 cookie / 认证 / 绕墙；不落盘任何第三方素材；截图 / 品牌资产永不处理。
"""

import argparse
import gzip
import json
import re
import sys
import time
import urllib.request
from collections import Counter
from html.parser import HTMLParser
from urllib.parse import urljoin

DEFAULT_UA = "wuikb-collect-source/0.1 (+knowledge-base research; no storage)"
HTML_CAP = 2 * 1024 * 1024          # HTML 读取上限 2MB
RUN_BUDGET_S = 60.0                  # 整轮抓取时间预算
MOUNT_RE = re.compile(r'<[^>]+id=["\']?(root|app)["\']?', re.I)


class ArgError(Exception):
    """参数错误 → 退出码 3。"""


class Parser3(argparse.ArgumentParser):
    """argparse 出错时退出码用 3（与抓取失败的 2 区分）。"""

    def error(self, message):
        raise ArgError(message)


# ---------------------------------------------------------------- HTML 解析 --

class PageScan(HTMLParser):
    """收集样式表链接、内联 <style>、meta theme-color、<title>、script 字节量。"""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.css_links = []        # 顺序保持
        self.inline_styles = []
        self.theme_color = None
        self.title_parts = []
        self.script_bytes = 0
        self._in_title = False
        self._in_style = False
        self._style_buf = []
        self._in_script = False
        self._script_buf = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "link":
            rel = (a.get("rel") or "").lower()
            href = a.get("href") or ""
            if "stylesheet" in rel and href:
                self.css_links.append(href)
        elif tag == "style":
            self._in_style = True
            self._style_buf = []
        elif tag == "meta":
            if (a.get("name") or "").lower() == "theme-color" and a.get("content"):
                self.theme_color = a["content"].strip()
        elif tag == "title":
            self._in_title = True
        elif tag == "script":
            self._in_script = True
            self._script_buf = []

    def handle_endtag(self, tag):
        if tag == "style" and self._in_style:
            self._in_style = False
            self.inline_styles.append("".join(self._style_buf))
        elif tag == "title":
            self._in_title = False
        elif tag == "script" and self._in_script:
            self._in_script = False
            self.script_bytes += len("".join(self._script_buf))

    def handle_data(self, data):
        if self._in_title:
            self.title_parts.append(data)
        elif self._in_style:
            self._style_buf.append(data)
        elif self._in_script:
            self._script_buf.append(data)


# ------------------------------------------------------------------ CSS 解析 --

class CssAcc:
    """跨多份 CSS 累积的抽取结果。"""

    def __init__(self):
        self.custom_props = []     # [{"name","value","selector","source"}]
        self.colors = Counter()    # 归一化颜色字面量 → 次数
        self.font_families = []    # 保持出现顺序，最多 8 条
        self.font_sizes = Counter()
        self.radii = Counter()
        self.spacing = Counter()   # "padding=8px" 这类带属性前缀
        self.spacing_px = []       # 纯 px 数值（刻度假设用）
        self.durations = Counter()

    def any_signal(self):
        return bool(self.custom_props) or len(self.colors) >= 5


COMMENT_RE = re.compile(r"/\*.*?\*/", re.S)
HEX_RE = re.compile(r"#([0-9a-fA-F]{3}|[0-9a-fA-F]{4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})(?![0-9a-fA-F])")
FUNC_COLOR_RE = re.compile(r"\b(rgba?|hsla?)\(\s*[^)]*\)", re.I)
DURATION_RE = re.compile(r"\b\d*\.?\d+m?s\b")
PX_VALUE_RE = re.compile(r"(-?\d*\.?\d+)px\b")
SPACING_PROPS = {"padding", "padding-top", "padding-right", "padding-bottom", "padding-left",
                 "margin", "margin-top", "margin-right", "margin-bottom", "margin-left",
                 "gap", "row-gap", "column-gap"}
DECL_RE = re.compile(r"^([-\w]+)\s*:\s*(.+)$", re.S)


def normalize_hex(digits: str) -> str:
    """3/4/6/8 位 hex → 小写 6/8 位。"""
    if len(digits) in (3, 4):
        digits = "".join(ch * 2 for ch in digits)
    return "#" + digits.lower()


def collect_colors(value: str, acc: CssAcc):
    for m in HEX_RE.finditer(value):
        acc.colors[normalize_hex(m.group(1))] += 1
    for m in FUNC_COLOR_RE.finditer(value):
        acc.colors[m.group(0).lower()] += 1


def process_declaration(text: str, selector: str, source: str, acc: CssAcc):
    text = text.strip()
    if not text or text.startswith("@"):
        return
    m = DECL_RE.match(text)
    if not m:
        return
    prop, value = m.group(1).lower(), m.group(2).strip()
    collect_colors(value, acc)
    if prop.startswith("--"):
        acc.custom_props.append(
            {"name": prop, "value": value, "selector": selector, "source": source})
    elif prop == "font-family":
        if value not in acc.font_families and len(acc.font_families) < 8:
            acc.font_families.append(value)
    elif prop == "font-size":
        acc.font_sizes[value] += 1
    elif prop == "border-radius":
        acc.radii[value] += 1
    elif prop in SPACING_PROPS:
        acc.spacing[f"{prop}={value}"] += 1
        for pm in PX_VALUE_RE.finditer(value):
            acc.spacing_px.append(float(pm.group(1)))
    elif prop in ("transition", "transition-duration", "animation", "animation-duration"):
        for dm in DURATION_RE.finditer(value):
            acc.durations[dm.group(0)] += 1


def walk_css(css: str, source: str, acc: CssAcc):
    """轻量括号游走：维护选择器栈，把每条声明交给 process_declaration。"""
    css = COMMENT_RE.sub("", css)
    stack, buf = [], []
    for ch in css:
        if ch == "{":
            stack.append("".join(buf).strip() or "@block")
            buf = []
        elif ch == "}":
            tail = "".join(buf).strip()
            buf = []
            if stack:
                stack.pop()
            if tail and stack:
                process_declaration(tail, " > ".join(s for s in stack if s) or "?",
                                    source, acc)
        elif ch == ";":
            decl = "".join(buf)
            buf = []
            if stack:
                process_declaration(decl, " > ".join(s for s in stack if s) or "?",
                                    source, acc)
        else:
            buf.append(ch)
            if len(buf) > 4096:
                buf = buf[-4096:]  # 防超长内容撑爆缓冲


def resolve_var(value: str, root_map: dict, depth: int = 0) -> str:
    """尽力把 var(--x) 解析成 :root 里的实际值（≤5 层，防环）。"""
    if depth > 5:
        return value

    def repl(m):
        base = root_map.get(m.group(1))
        return resolve_var(base, root_map, depth + 1) if base is not None else m.group(0)

    return re.sub(r"var\(\s*(--[\w-]+)[^)]*\)", repl, value)


# -------------------------------------------------------------------- 抓取 --

def fetch(url: str, ua: str, timeout: int, cap: int, kind: str):
    """抓单个资源 → (raw, note, content_type, status)。异常向上抛由调用方处理。"""
    req = urllib.request.Request(url, headers={
        "User-Agent": ua,
        "Accept": "text/css,*/*;q=0.1" if kind == "css" else "text/html,*/*;q=0.1",
        "Accept-Encoding": "identity",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read(cap + 1)
        note = ""
        if len(raw) > cap:
            raw, note = raw[:cap], f"超过 {cap} 字节上限，已截断"
        enc = (resp.headers.get("Content-Encoding") or "").lower()
        if enc == "gzip" or raw[:2] == b"\x1f\x8b":
            try:
                raw = gzip.decompress(raw)
            except OSError:
                note = (note + "；gzip 解压失败，按原始字节解码").strip("；")
        elif enc in ("br", "deflate"):
            note = (note + f"；服务器强制 {enc} 压缩，可能乱码").strip("；")
        return raw, note, resp.headers.get("Content-Type", ""), resp.status


def decode_html(raw: bytes) -> str:
    head = raw[:2048].decode("latin-1", errors="replace")
    m = re.search(r'charset=["\']?([\w-]+)', head, re.I)
    enc = m.group(1) if m else "utf-8"
    try:
        return raw.decode(enc, errors="replace")
    except LookupError:
        return raw.decode("utf-8", errors="replace")


# -------------------------------------------------------------------- 判定 --

def js_reason(html_bytes: int, script_bytes: int, css_total: int,
              css_link_n: int, acc: CssAcc) -> str:
    """返回判定为 JS 渲染的依据；空串 = 判定正常。"""
    if css_link_n == 0 and not acc.any_signal():
        return "无 <link rel=stylesheet> 且无可用的内联令牌"
    if html_bytes < 30_000 and script_bytes > 10 * max(css_total, 1) and css_total >= 0:
        return (f"抓到的 CSS 共 {css_total}B，script {script_bytes}B 超其 10 倍以上，"
                f"HTML 仅 {html_bytes}B（疑似挂载点 + 运行时注入样式）")
    if not acc.custom_props and len(acc.colors) < 5:
        return "抓到的 CSS 零自定义属性且颜色字面量不足 5 个"
    return ""


PLAN_B_TIP = """判定：疑似 JS 渲染 / 运行时注入样式（依据：{reason}）→ 走 Plan B

Plan B 操作（F12 复制，约 5 分钟）：
  1. Chrome / Edge 打开目标页 → F12 → Elements 面板选中 <html> 元素
  2. Styles 面板找 :root 区块（或 Computed 面板搜索「--」），全选复制自定义属性
     （--color-* / --font-* / --radius-* / --spacing-* 等）
  3. 或在 Console 执行（把 :root 规则复制到剪贴板；跨域样式表会自动跳过）：
       copy([...document.styleSheets].flatMap(s => {{ try {{ return [...(s.cssRules || [])]; }} catch (e) {{ return []; }} }})
         .filter(r => r.selectorText && r.selectorText.includes(':root'))
         .map(r => r.style.cssText).join('\\n'))
  4. 把复制到的变量粘贴给 Claude，继续 S2 抽取
"""


# -------------------------------------------------------------------- 主流程 --

def main() -> int:
    ap = Parser3(add_help=True, description="静态设计令牌抽取（collect-source Plan A）")
    ap.add_argument("url")
    ap.add_argument("--max-css", type=int, default=5)
    ap.add_argument("--max-css-bytes", type=int, default=2 * 1024 * 1024)
    ap.add_argument("--timeout", type=int, default=15)
    ap.add_argument("--format", choices=["md", "json"], default="md")
    ap.add_argument("--ua", default=DEFAULT_UA)
    args = ap.parse_args()
    url = args.url.strip()
    if not re.match(r"^https?://", url):
        raise ArgError(f"URL 必须以 http:// 或 https:// 开头，收到：{url}")

    t0 = time.monotonic()
    fetched = []

    try:
        raw, note, _ctype, status = fetch(url, args.ua, args.timeout, HTML_CAP, "html")
    except Exception as e:
        print(f"抓取失败：{url}\n错误：{e}\n"
              f"可尝试 curl 兜底：curl -sL --max-time 20 '{url}' | head -c 2000",
              file=sys.stderr)
        return 2
    html = decode_html(raw)
    html_bytes = len(raw)
    fetched.append({"type": "html", "url": url, "bytes": html_bytes,
                    "note": note or (f"HTTP {status}" if status != 200 else "")})

    scan = PageScan()
    try:
        scan.feed(html)
        scan.close()
    except Exception as e:
        fetched.append({"type": "parse-warn", "url": url, "bytes": 0,
                        "note": f"HTML 解析警告：{e}"})

    acc = CssAcc()
    css_total = 0
    for i, style in enumerate(scan.inline_styles):
        walk_css(style, f"inline#{i + 1}", acc)
        css_total += len(style)
        fetched.append({"type": "inline-style", "url": f"{url}#inline-{i + 1}",
                        "bytes": len(style), "note": ""})

    css_links = scan.css_links[:args.max_css]
    skipped = len(scan.css_links) - len(css_links)
    if skipped:
        fetched.append({"type": "note", "url": "", "bytes": 0,
                        "note": f"样式表超过 --max-css={args.max_css}，跳过其余 {skipped} 份"})
    for href in css_links:
        if time.monotonic() - t0 > RUN_BUDGET_S:
            fetched.append({"type": "note", "url": href, "bytes": 0,
                            "note": "超过整轮 60s 时间预算，停止后续抓取"})
            break
        css_url = urljoin(url, href)
        if not css_url.startswith(("http://", "https://")):
            fetched.append({"type": "skip", "url": href, "bytes": 0, "note": "非 http(s) 资源"})
            continue
        try:
            raw_c, note_c, _ct, _st = fetch(css_url, args.ua, args.timeout,
                                            args.max_css_bytes, "css")
        except Exception as e:
            fetched.append({"type": "css-error", "url": css_url, "bytes": 0,
                            "note": f"抓取失败：{e}"})
            continue
        css_total += len(raw_c)
        fetched.append({"type": "css", "url": css_url, "bytes": len(raw_c), "note": note_c})
        walk_css(raw_c.decode("utf-8", errors="replace"), css_url, acc)

    # :root 令牌优先 + var() 尽力解析
    root_map = {}
    for cp in acc.custom_props:
        if cp["selector"].split(" > ")[0].strip() == ":root" and cp["name"] not in root_map:
            root_map[cp["name"]] = cp["value"]
    for cp in acc.custom_props:
        cp["resolved"] = resolve_var(cp["value"], root_map)
    ordered = sorted(
        acc.custom_props,
        key=lambda c: (0 if c["selector"].split(" > ")[0].strip() == ":root" else 1, c["name"]))

    reason = js_reason(html_bytes, scan.script_bytes, css_total, len(css_links), acc)

    result = {
        "url": url,
        "title": "".join(scan.title_parts).strip() or None,
        "theme_color": scan.theme_color,
        "html_bytes": html_bytes,
        "script_bytes": scan.script_bytes,
        "css_link_total": len(scan.css_links),
        "css_fetched": len([f for f in fetched if f["type"] == "css"]),
        "inline_style_blocks": len(scan.inline_styles),
        "fetched": fetched,
        "custom_properties": ordered,
        "colors_top40": acc.colors.most_common(40),
        "color_distinct": len(acc.colors),
        "font_families": acc.font_families,
        "font_sizes": acc.font_sizes.most_common(),
        "border_radius": acc.radii.most_common(),
        "spacing": acc.spacing.most_common(40),
        "spacing_multiples": {
            "of_4": sum(1 for v in acc.spacing_px if v and v % 4 == 0),
            "of_8": sum(1 for v in acc.spacing_px if v and v % 8 == 0),
            "total_px_values": len(acc.spacing_px),
        },
        "durations": acc.durations.most_common(),
        "js_rendered": bool(reason),
        "js_reason": reason,
    }

    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0

    w = sys.stdout.write
    w(f"# extract-tokens 报告：{url}\n\n")
    w(f"- 页面标题：{result['title'] or '（未取得）'}；theme-color：{scan.theme_color or '无'}\n")
    w(f"- HTML {html_bytes}B · script {scan.script_bytes}B · CSS 链接 {len(scan.css_links)} 份"
      f"（抓取 {result['css_fetched']}）· 内联 style {len(scan.inline_styles)} 块\n\n")
    w("## 1. 抓取清单\n\n| 类型 | 字节 | 备注 / URL |\n|---|---|---|\n")
    for f in fetched:
        note = f["note"] or ""
        u = f["url"] if f["type"] in ("css", "css-error", "skip", "note") else ""
        sep = " " if note and u else ""
        w(f"| {f['type']} | {f['bytes']} | {note}{sep}{u} |\n")
    w("\n## 2. 设计令牌（自定义属性，:root 优先）\n\n")
    if ordered:
        w("| 名称 | 值 | 解析值 | 声明处 |\n|---|---|---|---|\n")
        for cp in ordered[:120]:
            w(f"| `{cp['name']}` | `{cp['value'][:60]}` | "
              f"`{cp['resolved'][:60]}` | {cp['selector'][:40]} |\n")
        if len(ordered) > 120:
            w(f"| … | 共 {len(ordered)} 条，仅列前 120 | | |\n")
    else:
        w("（未发现自定义属性）\n")
    w(f"\n## 3. 调色板（频次 top40，共 {result['color_distinct']} 种）\n\n"
      "| 颜色 | 次数 |\n|---|---|\n")
    for c, n in result["colors_top40"]:
        w(f"| `{c}` | {n} |\n")
    w("\n## 4. 字体栈\n\n")
    for f in acc.font_families:
        w(f"- `{f}`\n")
    if not acc.font_families:
        w("（未发现 font-family 声明）\n")
    w("\n## 5. 字号分布\n\n")
    for v, n in result["font_sizes"]:
        w(f"- `{v}` × {n}\n")
    if not result["font_sizes"]:
        w("（未发现 font-size 声明）\n")
    w("\n## 6. 圆角集合\n\n")
    for v, n in result["border_radius"]:
        w(f"- `{v}` × {n}\n")
    if not result["border_radius"]:
        w("（未发现 border-radius 声明）\n")
    sm = result["spacing_multiples"]
    w(f"\n## 7. 间距集合（top40）与刻度假设\n\n"
      f"- 纯 px 值 {sm['total_px_values']} 个，其中 4 的倍数 {sm['of_4']}、8 的倍数 {sm['of_8']}"
      "（占比高 → 存在 4/8pt 刻度节奏）\n\n")
    for v, n in result["spacing"]:
        w(f"- `{v}` × {n}\n")
    if not result["spacing"]:
        w("（未发现 padding/margin/gap 声明）\n")
    w("\n## 8. 动效时长\n\n")
    for v, n in result["durations"]:
        w(f"- `{v}` × {n}\n")
    if not result["durations"]:
        w("（未发现 transition/animation 时长）\n")
    w("\n## 9. 判定\n\n")
    if reason:
        w(PLAN_B_TIP.format(reason=reason))
    else:
        w("判定：静态 CSS 可用（Plan A 成立），令牌与参数如上。\n")
    w("\n```json\n" + json.dumps(result, ensure_ascii=False, indent=2) + "\n```\n")
    return 0


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stderr.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass
    try:
        sys.exit(main())
    except ArgError as e:
        print(f"参数错误：{e}", file=sys.stderr)
        sys.exit(3)
