# web-ui-knowledge-base

> 本项目由 `ai-project-template` 派生。它的「产品」是一个持续建设的 Web UI/UX 设计知识库。

## 项目简介

持续收集、登记、抽取、评审公开 Web UI/UX 设计知识（规范 / 设计系统 / 研究文章 / 产品案例 / 开源语料），以可追溯、许可干净、分级明确的知识记录（Source / Principle / Pattern / Case + A–D 证据分级）供各项目做前端参考分析时消费。

## 当前阶段

- 当前阶段：Phase1（知识库建设期）
- 交付物形态：文档仓（无运行时）
- 阶段目标：建全收集 SOP 与知识记录体系；完成首批来源登记与案例导入；建立评审节奏
- 非目标：不做 Web 应用 / 组件库；不替代任何项目的需求或设计决定；不镜像第三方截图与品牌资产

## 它能做什么

- `knowledge/`：核心产出区——来源登记、原则 / 视觉 / 交互模式、案例观察、MIT 语料镜像（含来源声明）
- `knowledge/SOP-collect.md`：收集 SOP——新来源五步进库（登记 → 许可核验 → 抽取 → 分级 → 评审）
- 与母模板 `template-docs/ui-knowledge/` 核心层形成「收集层 ↔ 核心层」分工：本仓承接全部收集量，跨 ≥2 项目实证的模式经提案回流母模板

## 快速开始

本仓为纯文档仓：git + Markdown 编辑即可，无环境安装要求。方法论与规则入口见 `ai/index.md`。

消费方式：各项目在自己的前端参考分析（`docs/research/*frontend-ui-reference-analysis.md`）中按 scope 查询本仓 `knowledge/`，引用 `SRC-*` / `PAT-*` / `PRN-*` / `CASE-*` ID；采纳 / 排除决定写在项目自己的 RA，不回写本仓。

## 文档入口

- `knowledge/README.md`：知识库定位、模型与使用方式（先看这个）
- `docs/00-09`：项目自身文档链（愿景 / 需求 / 计划；按文档剖面裁剪，`docs/06`/`07` 已省略）
- `ai/project-rules.md`：项目专属规则（Phase 边界 / 裁剪决策 / 禁区）

## 运行环境

- 纯文档仓，无运行时依赖；版本语义见 `ai/project-rules.md` §2.4

## 模板关系

- 通用方法论来自 `ai-project-template`（继承版本见 `TEMPLATE-BASE.md`）。
- 项目自身版本记录在 `VERSION`（当前 `v0.1.1`）；知识批次入库记 MINOR，单条修正记 PATCH。
- `knowledge/` 为项目自有目录，不参与模板同步；`template-docs/ui-knowledge/` 为母模板核心层镜像，其内容经同步维护，不在本仓直接改语义。
- 如发现可通用的模板优化，先在 `_governance/_proposals/` 起草提案，再回流模板仓库。

> 仓库可见性说明：本仓当前为 public（2026-08-16 创建）；计划 2026 年 9 月后评估转回 private。
