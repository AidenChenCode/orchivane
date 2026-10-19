# Orchivane 0.3.1

[English](README.en.md) · [MIT](LICENSE) · [贡献与本地验证](CONTRIBUTING.md)

**一个目标，多方协作，持续接班。** Orchivane 取 orchestration（编排）与 vane（方向标）的意象：让专业角色协同推进同一个目标。

## AI 写代码之后，谁来把整个项目推进下去？

一个需求跨越前端、后端、研究和测试时，你可能已经开了几个 AI 对话：每个都能处理自己的任务，但协作工作又回到了你身上。

- **你在搬运上下文。** 把这个窗口的结论复制给另一个，反复解释目标、约束和已经做过的决定。
- **并行开始互相干扰。** 两个会话改了同一份文件，一个仍按旧接口实现，最后需要你辨认哪一版有效。
- **换个对话就要重新交代。** 长对话结束了，新会话看到了摘要，却不知道哪些结论已确认、哪里有未提交成果、谁正在接着做。
- **“完成”很难判断。** 代码写完、测试通过、需求验收、推送和部署混成一句“已完成”，遗留问题没有明确的承接人。
- **你仍然是项目协调员。** 要决定下一步叫谁、给多少背景、何时验收，还要防止已经否定的方案被再次执行。

Orchivane 把这些协作责任交给一个总控入口：总控先澄清目标，再按实际需要组织专业会话，明确每项成果的唯一主责、输入版本、写入范围和验收条件。专业角色交付可核验的成果；换班时连同决定、证据、限制和下一步一起交接。小任务可以留在一个对话中完成。

例如，你只需告诉总控“为现有产品增加登录功能”：它先核对现有身份方案和接口，再判断实施与独立验收如何分工；收到交付后，分别说明实现、验证、推送与部署的状态。你继续参与目标和关键取舍，无须在每个角色窗口重复描述需求。以上是预期使用方式，实际工具能力和已验证范围见文末。

## 从一个想法开始

从一个项目想法开始，先调研并与用户沟通，判断适合什么协作机制，再形成分工与启动方案。没有已有 session 或资料也可使用；已有项目则复用其角色和入口。进入多会话执行后，用户在总控提出需求，总控统一派工、验收和收口。适用于开发、研究、内容与运营项目。

本套件包含一个可独立安装的 Skill 和轻量插件清单。核心入口短，按任务加载建制、派工验收、巡检、handoff 与 Codex 适配模块；没有后台服务、额外依赖或自动唤醒 hook。

## 直接使用

在已加载该技能的新对话中输入：

```text
使用 $orchivane，我有一个新项目想法，目前没有其他 session。
先帮我调研并和我沟通，判断需要什么协作机制，再给出具体分工和启动方案。
```

常用请求：

- 从零设计：`使用 $orchivane，我想做……，先了解需求和关键约束，调研后建议是否需要拆 session、怎么拆。`
- 接管现有项目：`使用 $orchivane，核对已有 session 的职责与当前 TODO，不派新任务。`
- 统一派工：`使用 $orchivane，按我已确认的任务清单向对应 session 派工，并读取交付结果。`
- 换班：`使用 $orchivane，给当前总控准备交接包，先不创建或归档。`
- 执行换班：`使用 $orchivane，按这份交接包创建接班会话、核验接班并转接关联自动化；保全资料且条件满足后归档旧会话并做归档后复核。`
- 单次巡检：`使用 $orchivane，检查这个项目的多会话协作，只报告新异常、关键缺口和下一步。`

流程是“理解目标 → 必要调研与分轮沟通 → 推荐协作结构 → 具体启动方案 → 按授权落地”。按长期上下文、工作依赖和独立验收需要拆分，也可以建议暂留当前对话。角色数量与命名按项目确定；已有授权直接沿用，真实新增的创建/发消息等动作才集中补问。长期角色与临时 subagent 分开管理。

## 安装与迁移

### 插件安装（推荐）

使用与其他 Codex 插件相同的“添加来源 → 安装插件”流程。无需先克隆仓库：

```sh
codex plugin marketplace add alexzhu0/orchivane
codex plugin add orchivane@orchivane-local
```

上述命令已在 Codex CLI 0.157.1 实际完成：0.3.1插件安装并启用，技能从插件缓存发现为 `orchivane:orchivane`。可用下面的命令核对安装状态：

```sh
codex plugin list --marketplace orchivane-local --json
```

2026-10-19，本机用户已确认桌面插件目录可见；两个新建桌面对话实际从插件缓存读取0.3.1并使用规则，其中一个请求正文未点名技能。本轮无需重启。目录可见由用户观察，启用状态和实际读取由工具核验，详见[桌面验收与复现](tests/desktop-plugin.md)。流程依据 [OpenAI插件打包文档](https://developers.openai.com/plugins/build/plugins)，具体命令以本机CLI帮助为准。这是通过公开GitHub来源分发，尚未上架官方精选目录。

插件安装后，可以说“使用 Orchivane 帮我组织这个项目”，或选择客户端显示的 `orchivane:orchivane` 技能。下文及独立安装的 `$orchivane` 示例指同一套规则。若此前已安装独立Skill，先完整备份到技能扫描目录之外，确认插件可用后仅保留一个活跃来源，避免重复加载；不要删除本地定制。

**是否需要“启动”？** 本包是按任务读取的技能，没有需要手动启动的后台进程。`installed=true`、`enabled=true` 表示已安装并启用；再用一个新对话核验实际加载。可直接输入：

```text
请检查本轮可用技能清单是否有 Orchivane。
若有，读取声明入口，报告版本，并用它建议一个需求尚不明确的新项目是否需要多个长期角色。
若没有就报告未发现，不自行搜索文件补救。本轮只读，不创建或派工。
```

清单出现、实际读取、按规则行动是三个不同检查点。自然语言触发受宿主、模型及其他技能影响；需要稳定选用时明确点名。此核验无需新增项目文件、脚本或角色。

### 独立 Skill 安装

```sh
git clone https://github.com/alexzhu0/orchivane.git
cd orchivane
```

独立 Skill 的完整目录是 [`skills/orchivane`](skills/orchivane/SKILL.md)，运行它无需 Python 或新依赖。下载/克隆本仓库后，在仓库根目录执行下面的 macOS/Linux 示例（目标已有文件或链接时拒绝覆盖）：

```sh
mkdir -p "$HOME/.agents/skills"
test ! -e "$HOME/.agents/skills/orchivane" && test ! -L "$HOME/.agents/skills/orchivane" && cp -R skills/orchivane "$HOME/.agents/skills/orchivane"
```

目录必须包含 `references/` 与 `agents/`，不要只复制 SKILL.md。Windows 可把整个目录复制到用户目录下 `.agents/skills/`。旧客户端使用 `~/.codex/skills/` 的安装须实际核验发现能力。选择一个安装来源；更新前核对其路径和版本，保留本地定制。目录规则依据 [Codex 技能文档](https://learn.chatgpt.com/docs/build-skills)。

0.3.1 更名自 Session Control，调用入口改为 `$orchivane`。已有 `session-control` 安装者，先将旧目录及本地定制备份到技能扫描目录之外，再安装新目录，避免两个入口同时生效。历史测试与冻结示例保留原名，不能把更名当作重新验证。

旧名0.3.0的本机独立复制安装曾被CLI发现，但三个新桌面对话均未列出该技能，原路径的根因仍未确认。后续0.3.1插件安装路线已通过新桌面对话加载验证；没有重测旧独立安装，也不将插件成功改写为旧路线已修复。当前验证结果见[验证记录](tests/evaluation.md)。

自动发现尚未生效时，可以明确要求助手“读取我安装目录中的 `orchivane/SKILL.md` 并按其流程工作”，提供真实完整路径。这是显式加载方式，应单独记录，不能当成自动发现或插件安装通过。

仓库内 `.agents/plugins/marketplace.json` 定义插件来源，根 `plugin.json` 为 portable 格式，`.codex-plugin/plugin.json` 为兼容格式。本包没有后台调度或自动执行 hook。

旧的个人 `session-handoff` / `session-health-check` 可以继续保留。新技能内部已有完整交接与巡检流程，无运行时依赖；明确使用 `$orchivane` 即可进入统一机制。旧技能未自动改写，以免影响已有项目。

## 内容与证据

| 内容 | 入口 |
| --- | --- |
| 核心规则与路由 | [SKILL.md](skills/orchivane/SKILL.md) |
| 从零调研沟通、机制设计、项目接管和恢复 | [setup.md](skills/orchivane/references/setup.md) |
| 任务说明、一次确认与验收 | [dispatch.md](skills/orchivane/references/dispatch.md) |
| 交接、资料保全、自动化转接、归档后复核 | [handoff.md](skills/orchivane/references/handoff.md) |
| 按变化巡检与通知 | [health-check.md](skills/orchivane/references/health-check.md) |
| 原生能力与降级方式 | [codex.md](skills/orchivane/references/codex.md) |
| Ponytail / Superpowers 源码研究与取舍 | [研究记录](docs/research.md) |
| 项目定位、同类方案与下一步取舍 | [价值与优化评估](docs/value-assessment.md) |
| 桌面插件发现、启用与使用复现 | [桌面验收](tests/desktop-plugin.md) |
| 当前标准、平台支持与边界 | [兼容性说明](docs/compatibility.md) |
| 真实多会话案例（最终19/20，未通过） | [借物小站完整记录](examples/tool-library/README.md) |
| 原生端到端实验的复现步骤 | [native-e2e.md](tests/native-e2e.md) |
| 行为测试条件与实测边界 | [场景](tests/scenarios.md)、[结果](tests/evaluation.md) |

## 能力边界

技能规定工作方法，客户端提供创建/读取/消息/自动化工具。缺少工具时可生成任务和交接材料，不能实际操控其他会话。检查或建制不自动授权创建新聊天、发消息、修复产品或归档。调度只在用户要求时建立。

0.3.0 根据真实原生会话实验补上技能版本标识、创建窗口登记与共享目录及冻结依赖核验，并提供开发校验、CI、MIT许可及贡献说明。静态验证不会创建聊天或调用供应商；运行方法见贡献文档。具体实测覆盖与未验证项以测试记录为准，不把单次流程成功推为所有客户端或所有项目有效。
