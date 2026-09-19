# 派生项目模板同步运行记录：v1.75.3

## 基本信息

- 项目：web-ui-knowledge-base（Web UI 设计知识库）
- 同步日期：2026-09-19
- 同步前模板版本：v1.71.0（2026-08-31）
- 目标模板版本：v1.75.3（模板仓 main 实读）
- 项目自身版本（`VERSION`）：v0.2.2（同步前在本轮先提交 `docs/env/local-env.md` 与 `docs/inputs/input-review-report.md` 时升版，见 62b190f）
- 继承版本记录（`TEMPLATE-BASE.md`）：存在；Lineage type：ordinary derived project；当前同步到：v1.75.3
- 同步分支：`chore/sync-template-v1.75.3`
- 实际同步提交：`fef2c33 sync template v1.75.3 from ai-project-template`（bootstrap 提交 `e26294e` 在前）
- 操作入口：`/run sync-methodology`（自然语言「同步最新方法论」）
- AI 工具 / CLI：Claude Code

## 执行命令

- dry-run：`powershell -ExecutionPolicy Bypass -File scripts/sync-template.ps1 --dry-run --no-stat`（首跑 EXIT=1 触发 bootstrap，bootstrap 后重跑 EXIT=0；日志 `.tmp/sync-dry-run.log`）
- commit：`bash scripts/sync-template.sh --commit --preserve-project-version`（脚本 dry-run 输出自荐 bash 入口，与 SOP PowerShell 入口等价）
- 是否使用版本保留标志：`--preserve-project-version`（与 `TEMPLATE-BASE.md` Lineage type 一致）
- check-derived-sync：`powershell -ExecutionPolicy Bypass -File scripts/check-derived-sync.ps1 fef2c33` → 通过（29 文件全部合规）
- 是否触发 PowerShell fallback：否
- post-sync-cleanup：按 `ai/prompts/maintainers/15-post-sync-cleanup.md` §5 审计清单逐项只读执行；2 项整理经用户确认后执行
- docs-system-audit（同步后审计）：轻量执行（结构级对照 + 规范基线增量点名）
- 项目验证建议 / 已执行验证：见「项目验证建议」节

### 命令真实性记录

| 步骤 | 实际命令 / 动作 | 退出结果 | 是否完整执行 | 是否等价替代 | 是否生成独立报告 | 备注 |
|---|---|---|---|---|---|---|
| dry-run 预览 | `sync-template.ps1 --dry-run --no-stat` | 首跑 EXIT=1（脚本落后→bootstrap）；重跑 EXIT=0，added=1 / modified=28 | 是 | 否 | 不适用 | 风险路径命中=无；README 命中均为清单内模板 README |
| commit / 同步 | `bash scripts/sync-template.sh --commit --preserve-project-version` | EXIT=0，提交 fef2c33 | 是 | 否（bash 入口为脚本自荐，非 fallback） | 不适用 | 工作区干净 |
| check-derived-sync | `check-derived-sync.ps1 fef2c33` | EXIT=0 通过 | 是 | 否 | 不适用 | 项目专属路径零触及 |
| post-sync-cleanup | 15 号 Prompt §5 清单逐项只读审计 + 2 项确认后写入 | 审计零残留；整理 2 项完成 | 完整执行 | 否 | 否（摘要在本记录） | 详见「同步后整理摘要」 |
| docs-system-audit | 结构级对照 + 规范基线增量点名 | 无强制重写项 | 轻量执行 | 否 | 否 | 纯文档仓，内容级全量审计判低收益 |
| 项目验证 | check-derived-sync + CI 待触发 | 边界检查通过 | 是（本地部分） | 否 | 不适用 | CI run 待 push 后观察，记未验证项 |

## A13 完成判据矩阵

| A13 步骤 | 证据 | 状态 | 若非完成，原因 | 下一步 |
|---|---|---|---|---|
| 标准闭环计划 | 用户确认记录（AskUserQuestion：开始执行 + 先提交 untracked） | 完成 |  |  |
| dry-run 预览 | EXIT=0，变更计数 + 风险路径=无 | 完成 |  |  |
| commit + 边界验证 | 同步提交 fef2c33 + check-derived-sync 通过 | 完成 |  |  |
| post-sync-cleanup | §5 清单逐项审计（零残留）+ 整理 2 项已执行 | 完整执行 |  |  |
| docs-system-audit | 结构对照 + 增量点名（本记录两节） | 轻量执行 | 纯文档仓，内容级全量审计判低收益 | 可选：后续按需运行完整审计 |
| 提案回流收口 | `_governance/_proposals/` 为空、无模板仓 issue 链接 | 完成 |  | 无待收口项 |
| 同步报告留痕 | 本文件 | 完成 |  |  |

> 状态含 `轻量执行`，本次标记为「同步主链完成，A13 闭环尚有剩余项（docs-system-audit 完整执行为可选项）」。

## 同步结果

- 是否成功：是
- 新增 / 修改的方法论文件：29（新增 1：`ai/doc-standards/stage-exit-baseline.md`；修改 28，含 `ai/index.md`、六规则文件、`template-sync.json`、同步 / 边界脚本、`template-docs/ui-knowledge/README.md` 等）
- `VERSION` / `CHANGELOG.md` 是否保持项目自身版本：是（v0.2.2 保持）
- `TEMPLATE-BASE.md` 是否更新继承模板版本：是（v1.71.0 → v1.75.3）
- 项目专属文件是否被误改：否（边界检查确认零触及 `README.md` / `ai/project-rules.md` / `docs/00-09` / `knowledge/`）
- 是否新增 / 刷新 `ai/doc-standards/00-09`：刷新（03-prd 等）+ 新增 `stage-exit-baseline.md`
- 是否残留旧 `docs/_scaffold/`：否

## 同步跨度采用清单

- 跨度确定说明：`TEMPLATE-BASE.md` 旧继承版本 v1.71.0 排除 → 目标 v1.75.3 包含；`upstream/CHANGELOG.md` 实查跨度内共 9 个版本（v1.72.0–v1.75.3，另 v1.71.1 在旧版本内不计入），与预期一致。

| 版本 | 条目 | 桶 | 存量影响 | 动作 | 负责环节 | 状态 |
|---|---|---|---|---|---|---|
| v1.72.0 | 沙箱 spawn 失败分流（rules-core §2） | ③ | 无存量 | 已随同步下行 | 下次任务 | 已生效 |
| v1.72.1 | 治理目录母仓自留内容审计 | ① | 存量仓需查 | 本轮 cleanup 已执行，结果干净 | cleanup | 已执行 |
| v1.72.2 | CHANGELOG-PLAIN 误报修复 | ④ | — | 一行带过（本轮警告为真实滞后，非误报） | — | 无需动作 |
| v1.73.0 | 路由章节级标注（`ai/index.md`） | ③ | 读取成本下降 | 已随同步下行 | 下次任务 | 已生效 |
| v1.73.0 | 任务卡执行记录（implementation-lifecycle §4.1） | ③ | 新任务卡默认 | 下次知识收集任务生效 | 下次任务 | 待生效 |
| v1.73.0 | `stage-exit-baseline.md` 规范基线 | ② | 03 §4 / 09 判据可对照 | 点名登记；Lean 剖面可裁剪 | docs-system-audit | 已点名 |
| v1.73.0 | document-lifecycle §5 重复编号修正 | ④ | — | 本轮已按新编号读取，引用无断点 | — | 无需动作 |
| v1.74.0 | `REC-*` 五类记录 + §9.1 两仓回流 | ② | 本仓 knowledge 模型仍四类 | 登记 open item（知识模型决策，项目版本语义 MAJOR） | 用户裁决 | 已登记 |
| v1.74.0 | web-fullstack-profile §10 承载声明 | ④ | 本仓无前端 | 一行带过 | — | 无需动作 |
| v1.75.0 | 三层领域布局（domain/ 保留名） | ④ | 普通路线零影响 | 一行带过 | — | 无需动作 |
| v1.75.1 | 跨度采用清单步骤 | ① | — | 本轮首次执行（即本表） | — | 已执行 |
| v1.75.2 | cleanup 审计项 + CI paths 检查点 | ① | — | 审计已执行（干净）；`project-check.yml` 无 paths 过滤问题 | cleanup | 已执行 |
| v1.75.3 | web-fullstack-profile §10 承载判据 | ④ | 本仓无前端 | 一行带过 | — | 无需动作 |

桶分布：① 3 ｜ ② 2 ｜ ③ 3 ｜ ④ 5；待确认条目：1（v1.74.0 `REC-*` 采纳决策，用户裁决）

执行反馈（3 行）：

1. 桶分类够用；②③按「是否存在可点名审计面」判定无歧义。`REC-*` 同时具规范基线与项目决策属性，归 ② 并登记 open item。
2. 耗时约 5 分钟；基于 `upstream/CHANGELOG.md` 顺序读取（9 版本约 90 行），成本低。
3. 不做清单会漏的项：`stage-exit-baseline` 对 `03 §4` 退出标准的可对照性、`REC-*` 与本仓 knowledge 四类模型的关系——两者都不是「同步报错」型缺口，无清单易误判为无影响。

## 同步后整理摘要

- 是否执行 `/run post-sync-cleanup`：是（15 号 Prompt §5 清单逐项只读审计 → 迁移计划经用户确认 → 执行）
- README / `ai/project-rules.md` / docs 分区是否需整理：均合规，无需整理
- 已处理项：
  - 残留审计全部干净：模板仓专用脚本 ×5、模板仓专用文档 ×4、根 `MAINTAINERS.md`、`.github` 收件箱模板、`template-docs/` 旧路径、根级治理目录、治理容器母仓自留内容——均无残留
  - `CHANGELOG-PLAIN.md` 补齐 v0.1.2–v0.2.2 大白话条目（原停在 v0.1.1，dry-run 警告即由此触发；同步自 v1.75.x 起保留该文件不再覆盖）
  - `docs/env/local-env.md` 人工确认项按纯文档仓口径补全（原 9 项「待确认」+ 服务器资源预案 8 项；经用户确认填「不适用 / 暂不需要」）
- 待确认项：无新增（历史 C-002 翻转说明见「遇到的问题」）
- 建议回写 / 后续迁移任务：无

## 文档体系审计摘要

- 是否执行 `/run docs-system-audit` 同步后审计模式：轻量执行（结构级）
- 规范基线缺口：`stage-exit-baseline.md`（v1.73.0 新增）与 `docs/03-prd.md` §3 各 Phase 退出标准的可对照性未逐条核对（Lean 剖面可裁剪，列为可选后续审计）
- 可接受兼容差异：`knowledge/` 仍为四类记录（Source / Principle / Pattern / Case），模板核心层已扩为五类（+`REC-*`）——同源模型的扩展层滞后，不属违规，采纳与否属知识模型决策（项目版本语义 MAJOR）
- 项目事实风险：无
- 回梳计划摘要：无强制回梳；不机械重写旧 docs

## 项目验证建议

- 建议运行的测试 / lint / 文档检查 / 人工验收：纯文档仓验证入口 = `check-derived-sync`（已过）+ `git diff --check` + push 后 `project-check.yml` CI
- 已执行验证与结果：`check-derived-sync.ps1 fef2c33` 通过；`git status` 干净
- 未验证项与原因：CI run 未观察（分支未推送；推送后应确认 Check 绿）

## 遇到的问题

- Git / gh / Git Bash / PowerShell / 网络问题：无
- 同步脚本问题：无（首跑 EXIT=1 为脚本身份自检的预期行为——本地脚本落后即停并给出 bootstrap 指引，按指引执行后通过）
- Prompt / 快捷命令理解问题：无
- 文档说明不清：无
- 派生项目专属冲突：历史 handoff C-002（2026-08-31 确认「`docs/env/local-env.md` 保持本地未跟踪」）在本轮由用户明确翻转为「先提交到 main」（62b190f，v0.2.2），以本次确认为准；该文件含本机事实（计算机名 / 用户名），如需撤回可 `git rm` 后脱敏重提交

## 可优化点归纳

| 问题 | 是否项目专属 | 是否建议回流模板 | 建议提案 |
|---|---|---|---|
| 无（本轮流程顺畅；bootstrap 自检按预期拦截旧脚本） | — | 否 | — |

## 已生成的回流提案

- 无（本次无模板回流提案）

## 提案回流收口

- 扫描范围：`_governance/_proposals/`（仅 README，无提案）、`.ai/session-handoff.md`、`_governance/sync-records/template-sync/` 全部记录、模板仓 issue 链接（无）
- 已确认被模板采纳或已有决议的提案：无
- 已归档到 `_governance/_archive/proposals/` 的本地提案：无（`_archive/proposals/` 现状维持）
- 仍需保留在 `_governance/_proposals/` 的提案：无
- 无法判断是否已处理的 issue / 提案与待确认项：无

| 本地提案 | 模板 issue / PR | 远端状态 | 关闭原因 / 处理结果 | 本地动作建议 |
|---|---|---|---|---|
| （无本地提案） | — | — | — | — |

## 后续动作

- 是否需要 `/run post-sync-cleanup`：否（本轮已完整执行）
- 是否需要 `/run docs-system-audit`：可选（完整执行为低优先；如做，点名核对 `stage-exit-baseline` ↔ `03 §4`）
- 是否需要按审计结果回梳 `docs/00-09` / `docs/design` / `docs/env`：否
- 是否需要补项目验证入口：否（push 后观察 CI 即可）
- 是否需要人工清理旧目录：否（本轮 `.tmp/` 任务日志由 AI 收尾清理）
- 是否需要同步回模板仓库：否

## open items（本轮登记）

| ID | 待确认项 | AI 建议 | 建议依据 | 备选方案 | 取舍影响 / 阻塞关系 |
|---|---|---|---|---|---|
| C-REC-001 | 是否采纳模板 v1.74.0 的 `REC-*` 配方记录（knowledge 模型四类 → 五类） | 暂不采纳，先在 Phase1 观察是否有「按产品类型组织的选型结论」真实产出需求；有真实条目再立案 | 本仓是收集层，模板核心层暂不存放 REC 条目（`template-docs/ui-knowledge/README.md` §4.3）；无真实条目前扩模型属提前设计 | ① 暂不采纳 ② 立即扩五类 ③ 仅在 `knowledge/README.md` 登记占位说明 | 知识模型变更按项目版本语义记 MAJOR；不阻塞同步收尾与日常 K1/K2 收集 |
