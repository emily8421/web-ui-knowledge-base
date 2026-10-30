# 派生项目模板同步运行记录：v1.75.3 → v1.75.6

## 基本信息

- 项目：web-ui-knowledge-base（wuikb）
- 同步日期：2026-10-30
- 同步前模板版本：v1.75.3（2026-09-19）
- 目标模板版本：v1.75.6（fetch 上游 main 实读 `VERSION`，非预设）
- 项目自身版本（`VERSION`）：v0.2.6（保持不动）
- 继承版本记录（`TEMPLATE-BASE.md`）：存在；Lineage type：ordinary derived project；同步后 Current synced template version: v1.75.6
- 同步分支：`chore/sync-template-v1.75.6`
- 实际同步提交：`1888b8b`（PR #4 squash 合并 → main `8187711 sync template v1.75.6 from ai-project-template (#4)`）
- 操作入口：`/run sync-methodology`（自然语言「同步模板」）
- AI 工具 / CLI：Claude Code
- 特殊背景：项目自旧机器迁入，用户不确定是否最新——已补核验（见「遇到的问题」）

## 执行命令

- dry-run：`powershell -ExecutionPolicy Bypass -File scripts/sync-template.ps1 --dry-run`（输出重定向 `.tmp/` 日志 + grep 摘要，git-guide §5.8）
- commit：`powershell -ExecutionPolicy Bypass -File scripts/sync-template.ps1 --commit --preserve-project-version`
- check-derived-sync：**推送前**对纯同步提交 `1888b8b`（HEAD）运行——v1.75.4/#478 权威校验时点；合并后 main HEAD `8187711` 复核二次通过
- 是否触发 PowerShell fallback：否
- post-sync-cleanup：轻量执行（见下）
- docs-system-audit（同步后审计）：轻量执行（见下）
- 项目验证建议 / 已执行验证：CI `project-check` 绿（run 41000583731，6s）；纯文档仓无测试入口，未验证项 = 无

### 命令真实性记录

| 步骤 | 实际命令 / 动作 | 退出结果 | 是否完整执行 | 是否等价替代 | 是否生成独立报告 | 备注 |
|---|---|---|---|---|---|---|
| dry-run 预览 | `sync-template.ps1 --dry-run`（log 重定向） | EXIT=0；10 delta 全部清单内；禁触路径（README / ai/project-rules / docs/00-09 / knowledge/）零命中 | 是 | 否 | 不适用 | `TEMPLATE-BASE.md` 存在自动启用双版本模式 |
| commit / 同步 | `sync-template.ps1 --commit --preserve-project-version` | EXIT=0；`1888b8b`，10 文件 | 是 | 否 | 不适用 | `VERSION` 保持 v0.2.6 |
| check-derived-sync | 推送前（HEAD=1888b8b）+ 合并后（HEAD=8187711） | 两次均「✅ 派生项目同步边界检查通过」 | 是 | 否 | 否 | 合并后**零伪影**（对照上轮 5 项，见「结果」） |
| post-sync-cleanup | 只读核验：workflow 形态 / `_scaffold` 残留 / 结构迁移盘点 | 跨度零结构迁移；`project-check.yml` 已就位；无 `docs/_scaffold/` 残留 | 轻量执行 | 否 | 否（本记录即载体） | 3 PATCH 无可整理项 |
| docs-system-audit | 对照跨度内 standards 变更（08-dev-plan / project-rules §2.4）点名核对 `docs/08` 完成包节 | 规范基线缺口无；`docs/08` 完成包字段渐进补（行为规则，见采用清单） | 轻量执行 | 否 | 否 | 纯前瞻 + 渐进适用，无机械重写 |
| 项目验证 | `gh pr checks 4` | project-check pass（6s） | 是 | 否 | 不适用 | 纯文档仓，CI 即验证入口 |

## A13 完成判据矩阵

| A13 步骤 | 证据 | 状态 | 若非完成，原因 | 下一步 |
|---|---|---|---|---|
| 标准闭环计划 | 预检报告 + 用户三次确认（restore / commit / push+PR）+ 合并方式确认 | 完成 | — | — |
| dry-run 预览 | EXIT=0，10 delta 全清单内 | 完成 | — | — |
| commit + 边界验证 | `1888b8b` + 推送前 check-derived-sync 通过（权威时点）+ 合并后复核通过 | 完成 | — | — |
| post-sync-cleanup | 只读核验：零结构迁移 / workflow 就位 / 无残留 | 轻量执行 | 跨度仅 3 PATCH，无可整理项 | 无需补做 |
| docs-system-audit | 跨度 standards 变更点名核对 | 轻量执行 | 3 PATCH 仅②桶一条且为渐进适用 | 下次知识批次收口生效（#481） |
| 提案回流收口 | #478 归档至 `_governance/_archive/proposals/`（决策矩阵见下） | 完成 | — | — |
| 同步报告留痕 | 本记录 | 完成 | — | — |

> 结论：同步主链完成；cleanup / audit 为轻量执行（跨度 3 PATCH、零结构迁移、无可整理项，已记录裁决依据），其余全部完成。

## 同步结果

- 是否成功：是
- 新增 / 修改的方法论文件（10）：`TEMPLATE-BASE.md`、`ai/global-rules.md`、`ai/implementation-lifecycle-rules.md`、`ai/doc-standards/08-dev-plan.md`、`ai/doc-standards/project-rules.md`、`ai/prompts/maintainers/12-sync-template.md`、`git-guide.md`、`template-docs/capability-packages.md`、`upstream/CHANGELOG.md`、`upstream/CHANGELOG-PLAIN.md`
- `VERSION` / `CHANGELOG.md` 是否保持项目自身版本：是（v0.2.6 / v0.2.6 顶部未动）
- `TEMPLATE-BASE.md` 是否更新继承模板版本：是（v1.75.3 → v1.75.6）
- 项目专属文件是否被误改：否
- 是否新增 / 刷新 `ai/doc-standards/00-09`：本次跨度内无镜像变化（`08-dev-plan` / `project-rules` 两件为 files_all 内 standards 增量；仓库无 `docs/*` 镜像，dry-run 已确认）
- 是否残留旧 `docs/_scaffold/`：否

## 同步跨度采用清单

- 跨度确定说明：`TEMPLATE-BASE.md` 旧继承版本 v1.75.3（排除）→ v1.75.6（包含）；实读 `upstream/CHANGELOG.md` 顶部三段，与预期一致

| 版本 | 条目 | 桶 | 存量影响 | 动作 | 负责环节 | 状态 |
|---|---|---|---|---|---|---|
| v1.75.4 | #478 校验时点指引（本仓提案，收窄采纳） | ③ | 推送前权威校验 + 留痕 | 本轮即按新规执行 | 本轮 | 已落地 |
| v1.75.4 | #479 公文腔词语约束（global-rules §10 第 6 款） | ③ | 纯前瞻，存量渐进适用 | 后续写作生效 | 写作类任务 | 生效中 |
| v1.75.4 | #481 Sprint 完成包版本回写挂钩（impl §7.1 + doc-standards 08/project-rules §2.4） | ② | 点名 `docs/08` 完成包字段未含 VERSION/CHANGELOG 挂钩 | 下次知识批次收口补（本仓 `ai/project-rules.md` §2.4 已有同向口径，无冲突） | docs-system-audit / 知识 Sprint 收口 | 待生效 |
| v1.75.5 | 同步 PR 边界方向 A（12-sync-template「同步 PR 边界」段 + git-guide §5.5） | ③ | PR 只含同步提交；收尾件拆合并后 | 本轮即按新规执行（首验生效） | 本轮 | 已落地 |
| v1.75.6 | 治理机制解耦 Phase 1（capability-packages 契约层 + global-rules 域标注） | ④ | 派生项目零迁移零门禁 | — | — | 无需动作 |

桶分布：① 0 ｜ ② 1 ｜ ③ 3 ｜ ④ 1；待确认条目：无

执行反馈（3 行）：

1. 桶分类够用；#481 双重属性（规范基线 + 行为规则）按「存在可点名受影响 docs」判②，边界规则可用。
2. 耗时与读取成本：低——3 PATCH 跨度，读 `upstream/CHANGELOG.md` 顶部约 80 行即覆盖，未分段。
3. 不做清单会漏掉的项：#478 / v1.75.5 对**同步流程自身**的即时影响（校验时点 / PR 边界）——不做清单极易按旧流程把收尾件混进同步 PR（上轮实证）。

## 同步后整理摘要

- 是否执行 `/run post-sync-cleanup`：轻量核验（未展开完整命令）
- README / `ai/project-rules.md` / docs 分区是否需整理：否
- 已处理项：workflow 核验（`project-check.yml` 就位，无 `template-check.yml`）；MAINTAINERS.md 无历史残留（符合 v1.70.0+ 预期）
- 待确认项：无
- 建议回写 / 后续迁移任务：无

## 文档体系审计摘要

- 是否执行 `/run docs-system-audit` 同步后审计模式：轻量（对照跨度内 standards 变更）
- 规范基线缺口：无
- 可接受兼容差异：`docs/08` 完成包字段暂未含 VERSION/CHANGELOG 挂钩（#481，渐进适用，下次知识批次收口补）
- 项目事实风险：无
- 回梳计划摘要：无需回梳

## 项目验证建议

- 建议运行的测试 / lint / 文档检查 / 人工验收：CI `project-check`（`git diff --check` + 版本一致性）；同步 PR 已绿
- 已执行验证与结果：project-check pass（run 41000583731）
- 未验证项与原因：无

## 遇到的问题

- Git / gh / Git Bash / PowerShell / 网络问题：无 fallback。**迁移背景补核验**（预检 A 阶段既有清单之外）：本项目自旧机器迁入、用户不确定是否最新——已 `git fetch origin` + ahead/behind 核验（0/0 一致）+ git 身份核验（完好）；另发现 5 个 knowledge corpora 文件纯 CRLF/LF 幻影改动（diff 0 hunk），经用户确认 `git restore` 处置。两项均暴露预检缺口，已立案回流提案（见下）。
- 同步脚本问题：无
- Prompt / 快捷命令理解问题：无
- 文档说明不清：无
- 派生项目专属冲突：无

**正向观察**：v1.75.5 新规（同步 PR 只含同步提交）首轮执行即验证生效——合并后 main HEAD `check-derived-sync` **零伪影通过**；对照 2026-09-19 上轮（收尾件混入 PR，合并后 5 项伪影失败）。

## 可优化点归纳

| 问题 | 是否项目专属 | 是否建议回流模板 | 建议提案 |
|---|---|---|---|
| 同步预检 A 阶段不含派生仓自身 origin 新鲜度核验（迁移 / 换机 / 多机场景工作区干净 ≠ 最新） | 否 | 是 | `TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md` |
| 迁移后 autocrlf 幻影改动触发「工作区不干净即停」多一轮确认 | 否（环境类，Windows + 迁移通用） | 暂不（低频、一次 restore 即解，已记 `.ai/pitfalls/`） | — |
| 同步场景仍需整读 document-lifecycle / implementation-lifecycle 全文，与主链交集小 | 否 | 候选（可评估路由表章节级标注） | 暂不立案（收益待更多同步样本） |

## 已生成的回流提案

- `_governance/_proposals/TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md`

## 提案回流收口

- 扫描范围：`_governance/_proposals/` / `.ai/session-handoff.md` / `_governance/sync-records/template-sync/` / 模板仓 issue 链接
- 已确认被模板采纳或已有决议的提案：`TEMPLATE-UPGRADE-squash-merge-sync-boundary-check.md`（#478）
- 已归档到 `_governance/_archive/proposals/` 的本地提案：上述一件（本轮归档，README 索引已建）
- 仍需保留在 `_governance/_proposals/` 的提案：`TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md`（新立，待提交模板仓 issue）
- 无法判断是否已处理的 issue / 提案与待确认项：无

| 本地提案 | 模板 issue / PR | 远端状态 | 关闭原因 / 处理结果 | 本地动作建议 |
|---|---|---|---|---|
| squash-merge-sync-boundary-check | [#478](https://github.com/emily8421/ai-project-template/issues/478) | merged（随 v1.75.4 聚合 PR 入库，changelog 署名本仓） | 部分采纳（收窄采纳：方向 2 校验时点指引落地；方向 1 正则放宽不实施，v1.54.3 已先期覆盖） | 归档 ✅（本轮） |

## 后续动作

- 是否需要 `/run post-sync-cleanup`：否（本跨度零结构迁移）
- 是否需要 `/run docs-system-audit`：否（轻量已覆盖；可选完整执行维持低优先）
- 是否需要按审计结果回梳 `docs/00-09`：仅 `docs/08` 完成包字段下次知识批次收口渐进补（#481）
- 是否需要补项目验证入口：否（CI 即入口）
- 是否需要人工清理旧目录：否
- 是否需要同步回模板仓库：是——新提案 `TEMPLATE-UPGRADE-sync-precheck-origin-freshness.md` 待按 `submit-proposal` 流程开模板仓 issue
