# 项目专属规则

> 本文件是项目专属规则的**种子实例**（不参与跨项目同步）。字段规范、填写要求、审计项与禁止项的
> 单一事实源在 `ai/doc-standards/project-rules.md`（规范基线，随模板同步）；生成 / 审计 / 精修本文件时对照规范基线。规则分层原则见 `ai/global-rules.md` §5。
>
> 判断标准：一条规则换到另一个完全不同的项目上是否还成立——
> 不成立（涉及具体技术栈/具体功能/具体Phase定义）就属于本文件（实例）；成立属规范基线或通用层。
>
> 填写时机：§1 Phase边界、§2 技术栈与项目约束、§3 项目形态与文档裁剪在生成 docs/03-09 **之前**填
> （作为约束）；§4 目录特例、§5 编码约定与禁区在审核 03-09 **之后**补。

## 初始化必填检查（生成 docs/03-09 前）

在使用 `ai/prompts/docs/01-review-inputs.md` 评审输入材料并用 `ai/prompts/docs/00-generate-or-complete-docs.md` 生成或补全 `docs/03-09` 前，必须确认以下项目已填写，不得保留占位说明直接进入设计阶段：

- `项目名称` 与 `代号/缩写` 已明确；若暂不需要缩写，写“无”。
- `§1 Phase边界` 已明确当前阶段允许、禁止与下一阶段预告；禁止项不得留空。
- `§2 技术栈与项目约束` 已列出本项目确定使用的主要技术；不确定版本写“待确认”，不得虚构。
- `§2.1 运行环境与资源约束` 已通过 `scripts/collect-env.ps1` 生成 `docs/env/local-env.md`，并完成人工确认项；若暂不能采集，必须说明原因。
- `§2.2 图表格式偏好` 已确认（默认 mermaid，可改 plantuml）；未确认则按默认 mermaid，不阻断。
- `§3 项目形态与文档裁剪` 已明确持久化、对外接口、演示形态、`docs/06`、`docs/07` 与需要保留的代码目录。
- `§2.4 项目版本管理` 已确认：默认从 `v0.1.0` 起步，并保持 `VERSION` 与 `CHANGELOG.md` 顶部项目版本一致；如需改规则，先在本节写明。
- 不适用的模板目录或文档已有“保留 / 省略 / 删除”决策；省略 `docs/06` 或 `docs/07` 时必须在 §3 留下说明。
- 新增项目文档的类型与路径已按 `docs/README.md` 分区规则判断；不得把新增文档直接放到 `docs/` 根目录。
- 若以上任一项无法判断，AI 必须先向用户提问或提出待确认项，不得继续生成后续设计文档。

## 0. 项目标识

项目名称：web-ui-knowledge-base（Web UI 设计知识库）
代号/缩写：wuikb

## 1. Phase边界

当前阶段：Phase1（知识库建设期）

允许：
- 收集、登记、抽取、评审公开 Web UI/UX 设计知识（规范 / 设计系统 / 研究文章 / 产品案例 / 开源仓库）
- 在本仓 `knowledge/` 下维护 Source / Principle / Pattern / Case 四类记录与证据分级（A–D）
- 镜像许可证明确允许的第三方文本语料（如 MIT 仓的 DESIGN.md），须带署名 + 来源 + 许可证标注
- 维护「收集 SOP」并按 SOP 持续收集新来源

禁止：
- 不收集第三方截图、设计稿、字体、图标、品牌资产（无论许可状态，一律只存链接 + 自有摘要）
- 不把知识记录写成任何项目的需求、接口或验收事实（本仓只产知识，不产项目决定）
- 不把 D 级（灵感 / 单案例）素材表述为成熟交互经验或可用性证据
- 不在本仓实现 Web 应用 / 组件库 / 设计系统代码（知识库是文档仓，`frontend/` 不启用）

下一阶段预告：
- Phase2：模式扩充 + 人工评审节奏 + 与母模板 `template-docs/ui-knowledge/` 核心层的晋升通道（candidate → reviewed → 跨 ≥2 项目实证 → 晋升提案回流母模板）

## 2. 技术栈与项目约束

纯文档仓：Markdown + Git。无前端 / 后端 / 数据库 / AI 模型运行时。脚本仅用模板自带 `scripts/`（check / sync 类），不新增运行时依赖。

例外（v0.1.2 起）：`.claude/skills/*/scripts/` 允许存放本项目自有的**零依赖纯标准库** Python 辅助脚本（本机 Python 3.14 已装，不引入第三方依赖、不新增安装步骤）；该目录为项目自有，不参与模板同步，也不落入模板 `scripts/`。当前实例：`.claude/skills/collect-source/scripts/extract-tokens.py`（K1 收集的静态设计令牌抽取，仅 stdout）。

## 2.1 运行环境与资源约束

> 字段规范见 `ai/doc-standards/project-rules.md` §4 §2.1（约束架构与技术方案选择；Demo / MVP 优先本机可运行，资源不足须在 `docs/05-tech-spec.md` 写降级策略或服务器预案；`docs/env/local-env.md` 只记录本机事实，不等于技术路线已被环境支撑）。

- 本机环境文档：`docs/env/local-env.md`（由 `scripts/collect-env.ps1` 生成，人工补充确认项）
- 技术环境评估报告：豁免（纯文档仓，无真实运行依赖；若未来加渲染 / 检查脚本再补做）
- Demo 阶段必须能在本机运行的部分：无运行时要求；git + Markdown 编辑即可
- 允许降级 / Mock / 远程运行的部分：不适用
- 禁止在本机运行的重资源部分：无
- 是否允许使用公司服务器：不适用
- 若需服务器，资源申请口径：不适用

## 2.2 图表格式偏好

> 字段规范见 `ai/doc-standards/project-rules.md` §4 §2.2；图表格式规范见 `ai/document-lifecycle-rules.md` §13，场景引导见 `template-docs/scenario-guides.md` §7。

- 图表格式：`mermaid`（默认）/ `plantuml`
- 若选 mermaid 以外格式，说明原因（如团队工具链、渲染环境）：用默认 mermaid

- 是否涉及可点击 UI：否（知识库为纯文档仓）
- 是否需要开发前可视化原型：豁免（无 UI 交付；风险 = 无）

## 2.4 项目版本管理

默认从 `v0.1.0` 起步，并保持 `VERSION` 与 `CHANGELOG.md` 顶部项目版本一致；`VERSION` / `CHANGELOG.md` / `TEMPLATE-BASE.md` 关系与 `PATCH` / `MINOR` / `MAJOR` 规则见 `ai/doc-standards/project-rules.md` §4 §2.4。可按项目交付节奏覆盖默认规则，但必须在本节写明；是否使用 git tag / GitHub Release：（待确认；默认不强制）。

本项目覆盖口径：知识内容批量导入 / 新来源批次入库记 MINOR；单条记录修正、链接核验更新记 PATCH；知识模型（四类记录 / 字段 / 生命周期）变更记 MAJOR。补充口径（v0.1.2 起）：单个新来源（1 条 SRC + 对应 Case）入库记 PATCH；≥2 个新来源或成批 Case 导入记 MINOR；工具 / 技能新增（不改知识模型）记 PATCH。

## 2.5 运行时版本锁定

> 字段规范见 `ai/doc-standards/project-rules.md` §4 §2.5（与 §2.1 运行环境与资源约束正交：§2.1 管硬件资源，§2.5 管运行时版本与切换工具；工具推荐见 `template-docs/env-setup.md`「运行时版本管理」；声明落点 `docs/05-tech-spec.md` §1）。

- 是否启用运行时版本锁定：豁免（纯文档仓，无运行时）
- 锁定的运行时与版本：不适用
- 版本声明文件：无
- 切换工具：无
- CI 校验方式：无
- 锁定原因：不适用
- 豁免理由：零运行时依赖；风险 = 无；若未来新增检查 / 渲染脚本，再按规范补声明

## 3. 项目形态与文档裁剪

> 本节用于初始化阶段，决定 docs/06、07 是否保留，以及 frontend/backend/tests/scripts/docker
> 哪些目录真正需要。此节应在生成 docs/03-09 之前先填好。

- 是否有持久化存储：无（知识记录即 Markdown 文件）
- 是否有对外接口：无（消费方式 = 各项目按 scope 读取本仓文件）
- 演示形态：不需演示（`frontend/` 不启用）
- 前端交互设计：豁免（纯文档知识库，无 UI 交付）
- UI 原型策略：豁免（同上）
- 通用详细设计：豁免（无非平凡子系统 / 外部服务 / 状态机；知识治理流程属内容运营，不是子系统设计）
- System Skeleton Gate：豁免（纯文档仓，无系统框架可验收；风险 = 无，补做时点 = 若未来加渲染 / 检查脚本再评估）
- docs/06-db-design.md：省略（无数据库）
- docs/07-api-spec.md：省略（无接口）
- 需要保留的代码目录：scripts/（模板 check / sync 脚本）；frontend/ backend/ tests/ docker/ 不启用

按项目形态裁剪规则（docs/06 / 07 何时省略、`frontend/` 启用条件、详细设计 / 前端交互 / UI 原型触发条件、目录裁剪等）见 `ai/doc-standards/project-rules.md` §4 §3；本节裁剪决策须与 `docs/00-09` 实际结构一致，省略项留下说明，不适用的裁剪行可删除。

## 4. 目录规范的项目特例

（本项目目录结构与 global-rules.md 的通用骨架有差异，特例说明如下）

- 新增 `knowledge/` 目录：本项目的核心产出区（Source / Principle / Pattern / Case 四类知识记录 + 证据分级）。这是项目自有目录，不参与模板同步。
- `knowledge/corpora/`：许可证允许镜像的第三方文本语料（如 MIT 仓的 DESIGN.md），每份带 `SOURCE.md`（出处 / 许可证 / 镜像日期）。
- `knowledge/scenarios.md`：**项目特有场景手册**（K1 收集 / K2 上游同步 / K3 晋升提名等）。母模板 `template-docs/scenario-guides.md` 在同步清单内会被覆盖，项目特有场景一律写本文件，编号用 K 前缀与母模板 A/C/M 空间隔离。
- `template-docs/ui-knowledge/`：随模板同步维护的核心层镜像（小而精）；本项目知识晋升到该层走 `_governance/_proposals/` 提案回流母模板，不在本仓直接改语义（同步会覆盖）。
- 省略 `docs/06` / `docs/07`（见 §3）；`frontend/` / `backend/` / `tests/` / `docker/` 不创建。
- 裁剪已执行（v0.1.1）：`frontend/` / `backend/` / `tests/` / `docker/` 四个占位目录与 `docs/06-db-design.md` / `docs/07-api-spec.md` 两份未填写骨架已于 2026-08-16 删除，与 §3 决策对齐；若未来 Phase 变更启用任一形态，按 `ai/doc-standards/project-rules.md` §4 §3 重新创建并回填 §3。

## 5. 编码约定与禁区

> Phase 级功能禁止见 §1，技术栈替代品禁止见 §2，本节只管代码层。字段规范见 `ai/doc-standards/project-rules.md` §4 §5。
> 每条尽量具体可执行；没有则写“无”，不要留空占位。

### 5.1 既有约定（新代码必须向其看齐）
- 命名：知识记录 ID 沿用母模板前缀体系（`SRC-*` / `PRN-*` / `PAT-VIS-*` / `PAT-INT-*` / `CASE-*`）；文件名 kebab-case。
- 分层与目录：知识内容只进 `knowledge/`；随模板同步的 `template-docs/ui-knowledge/` 不写项目内容。
- 既有模式：四类记录 + A–D 证据分级 + candidate/reviewed/core 生命周期，字段口径与母模板 `template-docs/ui-knowledge/README.md` §2/§4 保持一致（同源模型，本仓是其扩展层）。
- 错误处理 / 日志：不适用（纯文档仓）。

### 5.2 禁区（未经人工确认不得触碰）
- 不得擅改的文件 / 模块：`template-sync.json`（同步清单）、`scripts/`（同步脚本）、`TEMPLATE-BASE.md`。§5.2 的 `scripts/` 禁区指根目录模板同步脚本；`.claude/skills/**` 为项目自有目录（见 §2 例外），其内新增脚本经人工确认后允许，禁止任何第三方依赖。
- 不得擅自引入的依赖：任何新依赖（本仓零运行时依赖）。
- 不得自行实现的功能：镜像第三方截图 / 品牌资产（永久禁区，见 §1）；把本仓知识记录写成项目需求或验收事实。
- 愿景 / 01 中的功能点不等于已批准实现；阶段归属以 `docs/03-prd.md` §3 路线图为准，编码以 §1 当前阶段为准。

## 6. AI修改确认规则

AI 修改确认规则（写入前说明目的 / 影响范围 / **预计文件** / 预计变更摘要 / 风险与验证方式；批量操作先列全部文件与每文件变更摘要；只读分析无需逐次确认但不借只读之名修改；单次授权仅限该次任务；**模板只能约束 AI 行为和项目期望**，不能替代工具权限模型，建议启用写入前确认 / patch 预览并用 `git status` / `git diff` 兜底）见 `ai/doc-standards/project-rules.md` §5。
