# 派生同步运行记录：v1.75.6 → v1.76.0

## 基本信息

- 项目：web-ui-knowledge-base（emily8421/web-ui-knowledge-base）
- 同步日期：2026-11-02
- 同步前模板版本：v1.75.6（2026-10-30 同步）
- 目标模板版本：v1.76.0（上游 VERSION 实读 FETCH_HEAD）
- 项目自身版本（`VERSION`）：v0.2.6（保持不变）
- 继承版本记录（`TEMPLATE-BASE.md`）：存在；Lineage type：ordinary derived project；同步后 Current synced template version：v1.76.0
- 同步分支：`chore/sync-template-v1.76.0`
- 实际同步提交：`08d9a80`（`sync template v1.76.0 from ai-project-template`）；前置 bootstrap 提交 `7e10f02`（`chore: bootstrap latest sync script`，1 文件 +1 行）
- 操作入口：`/run sync-methodology`（自然语言「同步最新模板」）
- AI 工具 / CLI：Claude Code（Claude Fable 5 / GLM 运行时）

## 执行命令

- dry-run：`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/sync-template.ps1 --dry-run`（日志 `.tmp/sync-dry-run.log`）
- commit：`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/sync-template.ps1 --commit --preserve-project-version`（日志 `.tmp/sync-commit.log`）
- 是否使用版本保留标志：`--preserve-project-version`（与 Lineage type 一致，无冲突）
- check-derived-sync：`powershell -NoProfile -ExecutionPolicy Bypass -File scripts/check-derived-sync.ps1 08d9a80` → 通过
- 是否触发 PowerShell fallback：否（v1.75.8 改版后按 SOP 直接 `powershell -NoProfile` + bypass 保留重试余地；实际首次即 EXIT=0）
- post-sync-cleanup：轻量执行（只读检查批，见下节）
- docs-system-audit（同步后审计）：轻量执行（只读判断，见下节）
- 项目验证建议 / 已执行验证：纯文档仓无测试 / lint / build 入口；已执行验证 = check-derived-sync 边界检查 + 版本一致性核对（`VERSION` v0.2.6 = `CHANGELOG.md` 顶部 v0.2.6）

### 命令真实性记录

| 步骤 | 实际命令 / 动作 | 退出结果 | 是否完整执行 | 是否等价替代 | 是否生成独立报告 | 备注 |
|---|---|---|---|---|---|---|
| dry-run 预览 | `sync-template.ps1 --dry-run` | EXIT=0，27 delta / 0 skip | 是 | 否 | 不适用 | 首跑 EXIT=1（本地 sync-template.sh 旧版），按脚本自带 bootstrap 路径更新后重跑成功；bootstrap 单独成提交 `7e10f02` |
| commit / 同步 | `sync-template.ps1 --commit --preserve-project-version` | EXIT=0，同步提交 `08d9a80` | 是 | 否 | 不适用 | 工作区干净 |
| check-derived-sync | `check-derived-sync.ps1 08d9a80` | EXIT=0，边界检查通过 | 是 | 否 | 否 | 无项目专属文件误触 |
| post-sync-cleanup | 只读检查批（workflow / _scaffold 残留 / local-env / 版本一致性 / 新骨架） | 全部通过 | 轻量执行 | 否 | 否 | 纯文档仓，无迁移项 |
| docs-system-audit | 只读判断（对照 v1.76.0 新规则对 Lean 剖面的影响） | 无回梳项 | 轻量执行 | 否 | 否 | 见文档体系审计摘要 |
| 项目验证 | check-derived-sync + 版本一致性核对 | 通过 | 是 | 否 | 不适用 | 纯文档仓无测试入口，如实记录 |

## A13 完成判据矩阵

| A13 步骤 | 证据 | 状态 | 若非完成，原因 | 下一步 |
|---|---|---|---|---|
| 标准闭环计划 | 本会话计划输出 + 用户确认（AskUserQuestion 两轮） | 完成 | | |
| dry-run 预览 | EXIT=0，27 delta 清单核对边界干净 | 完成 | | |
| commit + 边界验证 | 同步提交 `08d9a80` + `check-derived-sync` 通过 | 完成 | | |
| post-sync-cleanup | 只读检查批全过（workflow / 残留 / local-env / 版本） | 轻量执行 | 纯文档仓无迁移项，无需完整命令 | 无 |
| docs-system-audit | 只读判断无回梳项 | 轻量执行 | 同上 | 无 |
| 提案回流收口 | 决策矩阵见「提案回流收口」节 | 完成 | | |
| 同步报告留痕 | 本记录 | 完成 | | 收尾提交按 SOP 拆到同步 PR 合并后 |

> 结论口径：同步主链完成；A13 中 post-sync-cleanup / docs-system-audit 为轻量执行（纯文档仓下无实际整理 / 回梳对象），不宣称完整闭环。

## 同步结果

- 是否成功：是
- 新增 / 修改的方法论文件：27 个 delta（全部在 `template-sync.json` 清单内），要点：
  - 新增 `ai/review-guide.md`（评审总纲，v1.76.0 MINOR 核心件，登记同步清单）
  - `ai/document-lifecycle-rules.md` §13 增「图表体系评审清单」
  - `ai/index.md`（路由表「PR / CI / Git 收尾」行对齐 remote-ci-sop-profile，v1.75.8）
  - 14 件人读文档 56 处 `powershell -ExecutionPolicy Bypass` 示例改 `powershell -NoProfile`（v1.75.8）
  - `ai/prompts/maintainers/12-sync-template.md`（A13 矩阵补 registry 回写项）+ `11-template-proposal-summary.md`（先期状态核实）等 Prompt 更新（v1.75.7 / v1.76.0）
  - `scripts/sync-template.sh` bootstrap 提前单独提交；`scripts/README.md`、`template-sync.json`、`TEMPLATE-BASE.md`、`upstream/CHANGELOG*.md` 常规刷新
- `VERSION` / `CHANGELOG.md` 是否保持项目自身版本：是（v0.2.6）
- `TEMPLATE-BASE.md` 是否更新继承模板版本：是（v1.75.6 → v1.76.0，Synced at 2026-11-02）
- 项目专属文件是否被误改：否（dry-run 与 check-derived-sync 双重核对：无 `ai/project-rules.md` / `knowledge/` / `docs/00-09` / 领域文件）
- 是否新增 / 刷新 `ai/doc-standards/00-09`：无（本轮无 doc-standards 变更）
- 是否残留旧 `docs/_scaffold/`：否（实查）

## 同步跨度采用清单

- 跨度确定说明：`TEMPLATE-BASE.md` 旧继承版本 v1.75.6（排除）→ v1.76.0（包含），实查上游 CHANGELOG 含 v1.75.7 / v1.75.8 / v1.76.0 三个版本段，与预期一致。

| 版本 | 条目 | 桶 | 存量影响 | 动作 | 负责环节 | 状态 |
|---|---|---|---|---|---|---|
| v1.75.7 | 12-sync-template A13 矩阵补「母仓 registry 回写登记」项 | ③ 行为规则 | 仅模板仓发起模式生效，本仓为派生侧会话 | 下次模板仓发起同步时生效 | 下次任务 | 前瞻 |
| v1.75.7 | 11-template-proposal-summary 第 10 条「先期状态核实」 | ③ 行为规则 | 下次提案 triage 生效 | 纯前瞻归并 | 下次任务 | 前瞻 |
| v1.75.7 | check-registry-drift.ps1 新增等（模板仓专用，不在同步清单） | ④ 零迁移 | 无 | — | — | 一行带过 |
| v1.75.8 | 14 件文档 Bypass→NoProfile 示例改写 | ④ 随件生效 | 对未来同步 / 检查操作生效 | — | — | 已生效 |
| v1.75.8 | 路由表「PR / CI / Git 收尾」行对齐 remote-ci-sop-profile §2 最小必读集 | ③ 行为规则 | 下次 PR / CI 收尾任务读取成本下降 | 下次收尾按新行路由 | 下次任务 | 前瞻 |
| v1.76.0 | 新增 `ai/review-guide.md` 评审触发矩阵 | ① 结构迁移（新文件入清单）+ ③ 行为规则 | Lean 剖面纯文档仓按其 §6 裁剪，无 E1-E6 工程评估义务 | 已随同步入库；裁剪口径留档本节 | cleanup | 已覆盖 |
| v1.76.0 | document-lifecycle-rules §13 图表体系评审清单 | ③ 行为规则 | 本仓 docs 为裁剪态（无 04-09 设计文档图表群），影响极低 | 下次涉图表文档任务时对照 | 下次任务 | 前瞻 |
| v1.76.0 | 3 个 Prompt 轻挂钩 + 3 个评审命令接图表维度 | ④ 随件生效 | — | — | — | 已生效 |

桶分布：① 1 ｜ ② 0 ｜ ③ 4 ｜ ④ 3；待确认条目：无

执行反馈（3 行）：

1. 桶分类够用；唯一歧义点是 review-guide 同时属「结构迁移（新文件）+ 行为规则（触发矩阵）」，按主性质归 ① 并在 ③ 补记。
2. 耗时低：本次跨度 3 个版本、上游 CHANGELOG 一次读取即可分类，未增加明显读取成本。
3. 不做清单会漏掉的项：v1.75.7 的 registry 回写挂钩（若未来从模板仓发起同步，收尾须核对 registry 回写，否则 A13 误标完成）。

## 同步后整理摘要

- 是否执行 `/run post-sync-cleanup`：轻量执行（只读检查批）
- README / `ai/project-rules.md` / docs 分区是否需整理：否
- 已处理项：workflow 仅 `project-check.yml`（无模板仓自检入口残留）；无 `docs/_scaffold/` 残留；`docs/env/local-env.md` 存在（无需 collect-env）；`ai/project-rules.md` 无新骨架需人工迁移（v1.76.0 未新增 project-rules 字段）
- 待确认项：无
- 建议回写 / 后续迁移任务：无

## 文档体系审计摘要

- 是否执行 `/run docs-system-audit` 同步后审计模式：轻量执行（只读判断）
- 规范基线缺口：无（本轮同步未改 doc-standards；v1.76.0 新增件为 review-guide 索引型 + lifecycle §13 附录段）
- 可接受兼容差异：本仓为 Lean 剖面纯文档仓，按 `ai/review-guide.md` §6 剖面裁剪，不承担 E1-E6 工程阶段评估义务；知识治理流程（K1-K5）不属工程评审矩阵范围
- 项目事实风险：无
- 回梳计划摘要：无回梳项；下次涉及图表 / 评审类任务时对照新清单即可

## 项目验证建议

- 建议运行的测试 / lint / 文档检查 / 人工验收：纯文档仓，建议项 = `check-derived-sync`（已过）+ 版本一致性（已过）+ CI `project-check.yml`（PR 上观察）
- 已执行验证与结果：check-derived-sync EXIT=0；`VERSION` v0.2.6 与 `CHANGELOG.md` 顶部一致
- 未验证项与原因：无本地测试 / lint 入口（纯文档仓，`ai/project-rules.md` §3 已声明裁剪）

## 遇到的问题

- Git / gh / Git Bash / PowerShell / 网络问题：无
- 同步脚本问题：首跑 dry-run EXIT=1（本地 `sync-template.sh` 落后远端，v1.76.0 上游改了脚本兜底数组），属脚本预期防护；按脚本自带 bootstrap 指引更新后成功。注意：本次实际使用 `powershell -NoProfile -ExecutionPolicy Bypass`（bypass 保留；v1.75.8 新口径建议先无 bypass，本机实测 bypass 直接过，未做无 bypass 重试对照）
- Prompt / 快捷命令理解问题：无
- 文档说明不清：无
- 派生项目专属冲突：无

## 可优化点归纳

| 问题 | 是否项目专属 | 是否建议回流模板 | 建议提案 |
|---|---|---|---|
| 无新增（本轮流程顺畅，bootstrap 防护按预期工作） | — | 否 | — |

## 已生成的回流提案

- 本轮无新增。存量：`_governance/_proposals/TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md`（2026-10-30 建立，未开 issue，见下节）

## 提案回流收口

- 扫描范围：`_governance/_proposals/`（1 件）、`.ai/session-handoff.md`、`_governance/sync-records/template-sync/`、模板仓 issue（gh 实查 recent 8 件）
- 已确认被模板采纳或已有决议的提案：无变化（#478 / 裁剪执行落地已在上轮归档，状态不变）
- 已归档到 `_governance/_archive/proposals/` 的本地提案：本轮无新增归档
- 仍需保留在 `_governance/_proposals/` 的提案：`TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md`
- 无法判断是否已处理的 issue / 提案与待确认项：无

| 本地提案 | 模板 issue / PR | 远端状态 | 关闭原因 / 处理结果 | 本地动作建议 |
|---|---|---|---|---|
| TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md | 无（未开 issue） | 不适用 | 上游 v1.75.7 / v1.75.8 / v1.76.0 均未覆盖该缺口（gh 实查无同题 issue） | 保留；后续经 `submit-proposal` 开 issue 回流 |

> 本次同步即该提案动机场景的第二次实证：本轮预检已自行执行 `git fetch origin` + rev-list 核对（0/0 一致），提案所述「对上游模板实读远端、对派生仓自身无对等步骤」缺口在现行 SOP 中仍未覆盖。

## 后续动作

- 是否需要 `/run post-sync-cleanup`：否（轻量审计已无待整理项）
- 是否需要 `/run docs-system-audit`：否（无回梳项）
- 是否需要按审计结果回梳 `docs/00-09` / `docs/design` / `docs/env`：否
- 是否需要补项目验证入口：否（纯文档仓裁剪已声明）
- 是否需要人工清理旧目录：否
- 是否需要同步回模板仓库：存量提案 `TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md` 待开 issue 回流（可与本轮收尾一并处理，经用户确认）
