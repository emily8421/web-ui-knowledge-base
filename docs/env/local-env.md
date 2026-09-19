# 本机运行环境采集

> 由 `scripts/collect-env.ps1` 自动生成。自动采集项用于辅助技术方案选择；“人工确认项”仍需项目负责人补充。

## 自动采集

- 采集时间：2026-08-26 17:50:10 +08:00
- 计算机名：DESKTOP-9TC9SR2
- 当前用户：maixh
- 工作目录：D:\2-Project\5-Project Templates\web-ui-knowledge-base
- 操作系统：Microsoft Windows 11 家庭版 中文版 10.0.26200 64-bit
- PowerShell：5.1.26100.9168
- CPU：12th Gen Intel(R) Core(TM) i7-12650H
- CPU 核心 / 线程：10 核 / 16 线程
- 内存总量：31.73 GB
- 系统架构：AMD64

### GPU

- Intel(R) UHD Graphics（显存/显存近似：2.00 GB）
- OrayIddDriver Device（显存/显存近似：未知）
- NVIDIA GeForce RTX 3050 6GB Laptop GPU（显存/显存近似：4.00 GB）

### 磁盘

- C: 可用 128.70 GB / 总计 464.95 GB
- D: 可用 22.11 GB / 总计 259.26 GB
- E: 可用 139.27 GB / 总计 195.31 GB

### 常用工具

- Git：git version 2.54.0.windows.1
- Python：Python 3.14.3
- Node.js：v22.17.1
- npm：8.1.0
- Java：已安装（未获取到版本）
- Docker：Docker version 29.5.2, build 79eb04c
- Docker 运行状态：可用

## 人工确认项（2026-09-19 经项目负责人确认：纯文档仓口径）

- Demo 阶段允许最大内存占用：不适用（纯文档仓，git + Markdown 编辑即可，无运行时）
- Demo 阶段允许最大显存占用：不适用（无运行时）
- Demo 阶段允许最大磁盘占用：不适用（仓库为文本文件，体量以 `git count-objects` 实测为准）
- 是否允许联网调用外部 API：不适用（无运行时；联网仅限 git 同步与 K1 收集按需抓取公开网页）
- 是否允许安装新依赖 / Docker 镜像：不适用（项目零运行时依赖，口径见 `ai/project-rules.md` §2）
- 是否允许使用公司服务器：不适用（与 `ai/project-rules.md` §2.1 口径一致）
- 是否涉及公司数据 / 隐私数据：不涉及（只收集公开 Web 设计知识的链接与自有摘要，不镜像截图与品牌资产）
- 本机必须跑通的功能：git + Markdown 编辑（无其他运行时要求）
- 可 Mock / 可远程运行的功能：不适用

## 服务器资源预案

> 当本机资源不足以实现完整功能时填写。若 Demo / MVP 全部可本机运行，可写“暂不需要”。

- 触发条件：暂不需要（纯文档仓，全部工作可本机完成；若未来新增渲染 / 检查脚本再评估）
- CPU：暂不需要
- 内存：暂不需要
- GPU / 显存：暂不需要
- 磁盘：暂不需要
- 网络 / 端口：暂不需要
- 部署方式建议：暂不需要
- 权限 / 成本 / 安全注意事项：暂不需要
