# CHANGELOG

本文件记录派生项目自身版本历史；继承的模板版本见 `TEMPLATE-BASE.md`。

## v0.1.6（2026-08-31）

- K1 补充观察（ima 视觉令牌向）：新增 `CASE-ima-webui-tokens`（Plan A 静态抽取 ima.qq.com 产品 Web 端本体——TDesign 底盘 + ima 自有薄主题层的双层令牌架构、灰阶接管品牌梯度 + 低频绿强调、半透明叠加与多机制双主题、14px 主战场字阶、圆角 8px 主档、4/8 间距节奏；candidate / D 级，含 3 条待复核）。
- `SRC-PROD-001` 最后核验刷新至 2026-08-31（确认 ima.qq.com 为产品 Web 端本体首屏，非营销页）。

## v0.1.5（2026-08-31）

- 新增 `.claude/skills/collect-source/MANUAL.md`：面向非设计师使用者的大白话操作手册（触发短语、四关卡应答要点、三种采集方式配合动作、标本页对照判断法、FAQ 与速查卡）。

## v0.1.4（2026-08-31）

- collect-source 技能新增两道评审机制：**S3.5 AI 协审**（附录 F 八项评估标准，逐条观察回溯原始抽取数据，✗ 项先修复再审——把「数字对不对」从非设计师用户身上卸掉）；**标本页渲染回放**（附录 G，按 Case 记录值生成 `.ai/preview/` 本地 HTML 标本页，用户与原站并排对比「像不像」完成体验审）。
- `.gitignore` 增 `.ai/preview/`；`ai/project-rules.md` §2 例外补标本页边界说明（一次性验证产物，不入库、非交付物，与纯文档仓边界不冲突）。

## v0.1.3（2026-08-31）

- collect-source 技能首跑实测（ant.design）：新增 `CASE-antd-v5-tokens`（v5 令牌体系与站点视觉配方观察，candidate / D 级）；`SRC-DS-003` 完成链接核验与许可核验（仓级 MIT），生命周期去掉「待登记核验」。
- 首跑验证了补充观察子流程（去重 → 既有 SRC 下加 Case + 刷新核验列）与 Plan A 静态抽取（dumi SSR 场景无需降级 Plan B）。

## v0.1.2（2026-08-31）

- 新增 K1 收集半自动技能 `.claude/skills/collect-source/`：`SKILL.md`（S0–S5 阶段门流水线，G1–G4 人工确认门，默认草稿模式零写入）+ `scripts/extract-tokens.py`（零依赖纯标准库静态设计令牌抽取，Plan A/B/C 采集降级；冒烟验证 ima.qq.com / linear.app / 坏域名 / 坏参数四例通过）。
- `ai/project-rules.md` §2 补技能目录零依赖脚本例外、§5.2 澄清禁区不含 `.claude/skills/**`、§2.4 补「单来源入库记 PATCH」口径（对齐 ima 入库 `7d0c3f3` 未升版的既成事实）。
- `knowledge/scenarios.md` K1 补半自动执行入口与说明。

## v0.1.1（2026-08-16）

- 执行目录裁剪：删除 `frontend/` / `backend/` / `tests/` / `docker/` 四个占位目录（仅含 `.gitkeep` + README）与 `docs/06-db-design.md` / `docs/07-api-spec.md` 两份未填写骨架，与 `ai/project-rules.md` §3 既有裁剪决策对齐；`ai/project-rules.md` §4 补记执行事实。
- 起草模板优化提案 `_proposals/TEMPLATE-UPGRADE-裁剪执行落地.md`（new-project `--shape` + 裁剪执行步骤 + post-sync-cleanup 审计项 + 根目录地图），待回流 ai-project-template。

## v0.1.0（2026-08-16）

- 初始化项目，基于 ai-project-template v1.62.0 创建。
