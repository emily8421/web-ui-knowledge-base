# Source 登记（来源总表）

> 模型：Source 记录只证明「来源存在 + 许可口径」，不承载分析结论。字段口径同母模板 `template-docs/ui-knowledge/source-registry.md`（v1.62.0）。
> 本表含两类：**继承条目**（与母模板核心层同 ID 同事实，勿在本仓重复定义语义）与**本仓扩展条目**（母模板未登记的来源）。

## 1. 登记表

| SRC-ID | 类型 \ 维度 | 标题与发布方 | 来源 URL | 证据上限 | 许可与保存策略 | 最后核验 | 生命周期 | 链接核验 |
|---|---|---|---|---|---|---|---|---|
| `SRC-A11Y-001` | 规范 \ 可访问性 | WAI-ARIA APG，W3C | https://www.w3.org/WAI/ARIA/apg/ | A | 可保存摘要 + 链接 | 2026-08-14 | candidate（继承母模板） | 已核验：可访问 |
| `SRC-A11Y-002` | 规范 \ 可访问性 | WCAG 2.2，W3C | https://www.w3.org/TR/WCAG22/ | A | 可保存摘要 + 链接 | 2026-08-14 | candidate（继承） | 已核验：可访问 |
| `SRC-DS-001` | 设计系统 \ 交互流程 | GOV.UK Design System，GDS | https://design-system.service.gov.uk/ | B | 可保存摘要 + 链接（OGL v3.0） | 2026-08-14 | candidate（继承） | 已核验：可访问 |
| `SRC-DS-002` | 设计系统 \ 组件表单 | USWDS，GSA | https://designsystem.digital.gov/ | B | 只保存摘要 + 链接 | 2026-08-14 | candidate（继承） | 已核验：可访问 |
| `SRC-HAI-001` | 人机协作指南 \ 信任 | HAX Toolkit，Microsoft | https://www.microsoft.com/haxtoolkit/ | B | 只保存链接（官方页暂不可用） | 2026-08-14 | candidate（继承） | 暂时不可用 |
| `SRC-VIS-001` | 视觉案例集合 \ 视觉布局 | awesome-design-md，VoltAgent | https://github.com/VoltAgent/awesome-design-md | D | **本仓扩展**：仓级 MIT，文本语料（DESIGN.md）可镜像进 `corpora/`；第三方站点素材仍只存链接 | 2026-08-16（许可复核） | candidate（扩展） | 已核验：可访问 |
| `SRC-DS-003` | 设计系统 \ 视觉布局 | Ant Design，蚂蚁集团 | https://ant.design/ | B | 只保存摘要 + 链接（仓级 MIT，2026-08-31 核验） | 2026-08-31（链接可访问，标题「Ant Design - The world's second most popular React UI framework」） | candidate（扩展） | 已核验：可访问 |
| `SRC-DS-004` | 设计系统 \ 组件表单 | Material Design 3，Google | https://m3.material.io/ | B | 只保存摘要 + 链接 | 待核验 | candidate（扩展，待登记核验） | 未核验 |
| `SRC-PROD-001` | 产品案例 \ 知识库工作台 | ima（AI 知识管家），腾讯 | https://ima.qq.com | C | 只保存链接 + 自有摘要（闭源产品，无素材许可；不存截图） | 2026-08-31（链接可访问，标题「ima - 腾讯AI知识管家」；确认为产品 Web 端本体首屏） | candidate | 已核验：可访问 |

> 继承条目的语义与升级以母模板为准（同步时对齐）；本仓为其新增的观察（Case）不影响母模板状态。

## 2. 维护说明

- 新来源按 `SOP-collect.md` 五步进表；ID 前缀规则见 SOP §1.1。
- 「最后核验」记录日期 + 核验范围；链接失效只改「链接核验」列，不动生命周期。
- 许可变化（收紧 / 放宽）→ 更新保存策略列 + `corpora/*/SOURCE.md`；必要时把模式降级。
