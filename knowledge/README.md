# Web UI 设计知识库（knowledge/）

> 本目录是 web-ui-knowledge-base 项目的核心产出区：持续收集、登记、抽取、评审公开 Web UI/UX 设计知识。
> 知识模型与字段口径同源于母模板 `template-docs/ui-knowledge/README.md`（v1.62.0 起）；本仓是其**扩展层**——母模板核心层保持小而精（每条模式需跨 ≥2 项目实证），本仓承接全部收集量与候选池。

## 1. 定位与分工

```text
公开来源（awesome-design-md / 设计系统 / 规范 / 研究文章 / 产品观察）
  │ 只读输入
  ▼
本仓 knowledge/（收集 + 整理 + 评审）★收集的胖在这里长★
  │ 提炼出跨项目稳定的模式（reviewed 后可提名）
  ▼
母模板 template-docs/ui-knowledge/（核心层，随同步到达各项目）
  │ 下行同步
  ▼
派生项目（LUMEN / zhiyan / flowkit / …）做参考分析时按 scope 消费
```

- **本仓收**：全部 Source 登记、案例观察（Case）、候选模式（candidate Pattern/Principle）、许可证允许的文本语料镜像。
- **母模板收**：跨 ≥2 项目实证、经维护者评审的 reviewed/core 模式（经 `_proposals/` 提案回流，不在本仓直接写）。
- **项目消费**：各项目参考分析引用 `SRC-*` / `PAT-*` / `PRN-*` / `CASE-*` ID；采纳决定写在项目自己的 RA，不回写本仓。

## 2. 知识模型（四类记录 + 证据分级）

与母模板同源，简述如下；字段规范以母模板 `template-docs/ui-knowledge/README.md` §2/§4 为准：

| 记录类型 | ID 前缀 | 文件 | 用途 |
|---|---|---|---|
| Source | `SRC-*` | `sources.md` | 登记来源（规范 / 设计系统 / 研究 / 产品案例 / 代码仓） |
| Principle | `PRN-*` | `principles.md` | 跨产品成立的设计原则 |
| Pattern（视觉） | `PAT-VIS-*` | `patterns-visual.md` | 可复用视觉解法 |
| Pattern（交互） | `PAT-INT-*` | `patterns-interaction.md` | 可复用交互解法 |
| Case | `CASE-*` | `cases/` | 真实产品 / 设计稿的观察记录 |

证据分级：**A**（正式规范）/ **B**（成熟设计系统 / 有研究依据）/ **C**（多案例一致的可观察模式）/ **D**（灵感 / 单案例，只作发散）。

生命周期：`candidate → reviewed → core`（本仓内推进到 reviewed；core 晋升 = 回流母模板，走提案）。

## 3. 目录结构

```text
knowledge/
├── README.md                  # 本文件：定位 + 模型 + 使用方式
├── sources.md                 # Source 登记（总表）
├── principles.md              # Principle 记录
├── patterns-visual.md         # 视觉 Pattern
├── patterns-interaction.md    # 交互 Pattern
├── cases/                     # Case 观察记录（每案例一文件）
├── corpora/                   # 许可证允许镜像的第三方文本语料
│   └── awesome-design-md/     #   MIT 语料镜像 + SOURCE.md
└── SOP-collect.md             # 收集 SOP（新来源怎么进）
```

## 4. 使用方式

- **收集新来源**：按 `SOP-collect.md` 走（登记 → 许可核验 → 抽取 → 分级 → 评审）。
- **项目消费**：在项目参考分析（RA）里按 scope 查询本仓 + 母模板核心层，引用 ID；采纳 / 排除决定写项目自己的 RA。
- **晋升提名**：本仓 reviewed 的模式若在 ≥2 项目实证有效，起草 `_proposals/TEMPLATE-UPGRADE-*.md` 回流母模板。

## 5. 边界（与母模板一致，不放松）

- 不镜像第三方截图、设计稿、字体、图标、品牌资产——一律只存链接 + 自有摘要。
- D 级素材只作视觉发散，不得表述为成熟交互经验或可用性证据。
- 仓级开源许可证不自动覆盖引用的第三方素材；语料镜像按资产级许可判断（见 `corpora/*/SOURCE.md`）。
- 知识记录不写成任何项目的需求、接口或验收事实。
