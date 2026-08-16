# 收集 SOP（新来源怎么进知识库）

> 目标：每条新知识可追溯、许可干净、分级明确，避免知识库退化成「有链接没证据」的清单。

## 0. 快速判断

新来源到手 → 判断类型：**规范 / 设计系统 / 研究文章 / 产品案例 / 代码仓**。对应证据等级上限：A / B / B / C / C（视觉合集类为 D）。

## 1. 标准流程（五步）

```text
① 登记 → sources.md 加一行 SRC-*（先占 ID，标 candidate）
② 许可核验 → 查仓级 LICENSE + 素材级权利；确定保存策略（摘要 / 语料镜像 / 只链接）
③ 抽取 → 按类型产出 PRN-* / PAT-* / CASE-* 草稿（全标 candidate）
④ 分级 → 每条标 A/B/C/D + 适用 / 不适用条件
⑤ 评审 → 维护者人工复核后升 reviewed（含链接核验状态更新）
```

各步要点：

1. **登记**：`SRC-ID` 用稳定前缀（`SRC-A11Y-*` 可访问性 / `SRC-DS-*` 设计系统 / `SRC-HAI-*` 人机协作 / `SRC-VIS-*` 视觉合集 / `SRC-RES-*` 研究 / `SRC-PROD-*` 产品观察 / `SRC-CODE-*` 代码仓）。字段见 sources.md 表头。
2. **许可核验**：
   - 仓级 MIT / Apache / CC-BY 等宽松许可 → 可镜像**文本语料**进 `corpora/`（带 `SOURCE.md`：出处 + 许可证 + 镜像日期 + 上游 URL）。
   - 未声明 / 限制性许可 → 只保存链接 + 自有摘要。
   - **截图 / 设计稿 / 字体 / 图标 / 品牌资产：无论什么许可都不镜像**（永久禁区）。
   - 判断不了 → 标「许可待确认」，只存链接。
3. **抽取**：一案一文进 `cases/`（`CASE-<产品>-<主题>.md`）；模式进 `patterns-*.md`；跨产品原则进 `principles.md`。每条必填：要解决的问题 / 适用 / 不适用条件 / 来源 ID / 证据等级 / 状态。
4. **分级**：按能支撑多强的结论定级，不按视觉质量定级；D 级条目写明「只作发散」。
5. **评审**：维护者逐条看来源可访问性、等级准确性、适用边界合理性；通过标 `reviewed（日期）`，否则留 candidate 或删。

## 2. 上游同步（awesome-design-md 类聚合仓）

聚合仓是「上游原料」，定期（建议每月或按需）：

```text
git -C <本地克隆> pull → diff 出新增案例 → 按 §1 流程处理新增 → 记录同步日期
```

- 上游更新不自动触发抽取；每次同步后人工挑值得分析的案例。
- 上游改了许可或下架 → 更新 `corpora/*/SOURCE.md` + 对应 `SRC-*` 的许可字段。

## 3. 版本与提交约定

- 批量导入 / 新来源批次入库 → MINOR（`v0.x+1.0`）；单条修正 / 链接核验 → PATCH。
- commit message：`knowledge: 登记 SRC-XXX …` / `knowledge: 新增 CASE-xxx 观察` / `knowledge: 升级 PAT-VIS-xxx 为 reviewed`。
- 提交前跑 `powershell -ExecutionPolicy Bypass -File scripts/check-markdown-clean.ps1 knowledge docs`（若可用）。

## 4. 禁止项（重申）

- 不为省事跳过许可核验直接镜像。
- 不把单案例拔高成 C 级以上（「一个产品这么做」≠「多案例一致」）。
- 不在 Case 里贴大段原文（自有提炼为主，引用点到为止）。
- 不删 reviewed 记录（降级 / 废弃走 `deprecated` 状态留痕）。
