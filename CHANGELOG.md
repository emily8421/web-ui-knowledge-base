# CHANGELOG

本文件记录派生项目自身版本历史；继承的模板版本见 `TEMPLATE-BASE.md`。

## v0.1.1（2026-08-16）

- 执行目录裁剪：删除 `frontend/` / `backend/` / `tests/` / `docker/` 四个占位目录（仅含 `.gitkeep` + README）与 `docs/06-db-design.md` / `docs/07-api-spec.md` 两份未填写骨架，与 `ai/project-rules.md` §3 既有裁剪决策对齐；`ai/project-rules.md` §4 补记执行事实。
- 起草模板优化提案 `_proposals/TEMPLATE-UPGRADE-裁剪执行落地.md`（new-project `--shape` + 裁剪执行步骤 + post-sync-cleanup 审计项 + 根目录地图），待回流 ai-project-template。

## v0.1.0（2026-08-16）

- 初始化项目，基于 ai-project-template v1.62.0 创建。
