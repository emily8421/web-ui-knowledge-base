# CHANGELOG

本文件记录派生项目自身版本历史；继承的模板版本见 `TEMPLATE-BASE.md`。

## v0.2.6（2026-09-19）

- 第二批人工评审（K4 清单驱动）：`CASE-ima-knowledge-base`、`CASE-antd-v5-tokens`、`CASE-meiqia-cs-workbench`、`CASE-linear-workbench`、`CASE-vercel-dashboard` 五条转 `reviewed（2026-09-19）`。**全库 8 条 Case 至此全部评审完毕**（待复核项如实标注继续挂起，不阻塞评审结论）。
- `PAT-VIS-102「中性底盘 + 单强调色」`证据边界由三案加固为五案（新增 linear 深色面、vercel 浅色演绎面；构成仍为 1 案产品本体 + 4 案营销/演绎面，浅/深双向覆盖，结论不变）；linear / vercel 条目提名行同步标注「已并入 PAT-VIS-102」防重复提名。
- 挂起项维持：ima-knowledge-base 6 项待复核（二手材料）、antd「主色必配同色相软底」提名待第 3 来源、ima「常驻问答面板」提名待 LUMEN 试点第 2 来源。

## v0.2.5（2026-09-19）

- K5 链接核验（kb-ops 流程，7 来源逐一 WebFetch 实测）：`SRC-A11Y-001/002`、`SRC-DS-001/002`、`SRC-VIS-001` 核验列刷新至 2026-09-19（GOV.UK 在活跃更新、awesome-design-md MIT 未变）；`SRC-DS-004`（Material Design 3）完成拖欠的首次核验（可访问，SPA 正文需 JS 渲染，标题层确认）。
- `SRC-HAI-001`（HAX Toolkit）死因定位：原址缺语言前缀，404 连续两判；换址 `https://www.microsoft.com/en-us/haxtoolkit/`（实测可达，标题「Microsoft HAX Toolkit」），链接核验恢复「已核验：可访问」。全表 11 来源现已无未核验 / 不可用项。

## v0.2.4（2026-09-19）

- 首批人工评审（K4 清单驱动，kb-ops 流程）：`CASE-intercom-cs-workbench`、`CASE-slack-messaging`、`CASE-ima-webui-tokens` 三条转 `reviewed（2026-09-19）`。
- 依据三案一致（炭黑+Fin 橙 / 茄紫+链接蓝 / 灰阶+品牌绿）新立 C 级模式 `PAT-VIS-102「中性底盘 + 单强调色」`（reviewed）；条目内声明证据构成（2 案营销面，其中 1 案演绎转述 + 1 案产品本体）与适用边界（品牌用色纪律层规律；工作台高密度界面配方验证待产品本体来源补充）。intercom 提名行同步标注「已立 PAT-VIS-102」防重复提名。
- 挂起项维持：ima-webui 3 条待复核（F12 级）、intercom 产品本体与暗色模式待复核、`PAT-VIS-102` 后续待第 2 产品本体证据加固——均不阻塞本次评审。

## v0.2.3（2026-09-19）

- 新增知识库管理技能 `.claude/skills/kb-ops/SKILL.md`（零依赖、无脚本，纯流程固化）：「列候选」（全库 candidate / 待复核 / 提名盘点，只读）、「评审与晋升」（candidate → reviewed 单条评审入口 + K3 回流提名路由）、「核验链接」（sources.md 批量可达性核验与核验列刷新，失效项列清单待人工）。所有写动作先列变更清单经确认后执行；本技能永不自动升 reviewed、不引入依赖。
- `knowledge/scenarios.md` 登记新增场景：K4 候选评审清单、K5 链接核验刷新（编号顺延）；K3 cmd 指针补 kb-ops 入口。

## v0.2.2（2026-09-19）

- 补录两份此前未入库的项目事实文档：`docs/env/local-env.md`（2026-08-26 由 `scripts/collect-env.ps1` 采集的本机环境留痕，人工确认项待补）与 `docs/inputs/input-review-report.md`（Phase1 知识库基础事实输入材料评审报告，候选态待人工确认）。仅补录既有产出，无知识内容变更。

## v0.2.1（2026-09-09）

- zhiyan 双端重设计定稿候选 D「直角细线专业台」触发参照补源：新增 `CASE-linear-workbench`（表面台阶 + 单强调纪律，深色面；「中性底盘 + 单强调色」第 4 案）、`CASE-vercel-dashboard`（近白画布黑白二重奏，浅色直角向；语义色 soft/deep 三件套、技术标签等宽字体观察）。均 candidate / D 级（营销面观察），待评审。
- 均自既有语料 `SRC-VIS-001` 抽取，无新来源登记。

## v0.2.0（2026-09-09）

- 首批「客服双端」参考批次入库（zhiyan 界面重设计消费线的补源动作）：登记 `SRC-DS-005`（Ant Design Mobile，B 级上限）、`SRC-PROD-002`（美洽，C 级上限）；新增观察 `CASE-meiqia-cs-workbench`（产品结构 / 人机协同分层）、`CASE-intercom-cs-workbench`（克制用色与表面分级，附「中性底盘 + 单强调色」C 级候选模式提名）、`CASE-slack-messaging`（IM 品牌营销面，触控与阴影分层对照）。均 candidate / D 级（营销面与单案例观察），待评审。
- 链接核验：mobile.ant.design、meiqia.com（2026-09-09 均可访问，核验记录见 sources.md）。

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
