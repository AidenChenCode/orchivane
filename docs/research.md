# Ponytail、Superpowers 与本套件的取舍

研究日期：2026-10-19。读取公开仓库源码与插件清单，不仅看 README；未执行上游 hooks 或安装脚本。以下版本以本次浅克隆的提交为准，不承诺未来仓库行为不变。

| 项目 | 读取版本 | 固定源码 |
| --- | --- | --- |
| Ponytail | manifest 5.3.2；`09c434ab73ca43761c5d8b0c5d341926c2fba710` | [仓库快照](https://github.com/DietrichGebert/ponytail/tree/09c434ab73ca43761c5d8b0c5d341926c2fba710) |
| Superpowers | manifest 7.0.0；`bb92a77741419a4ab5f06e711a283343f1ada0c3` | [仓库快照](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3) |

本机安装的 Superpowers 技能版本为 6.4.2；本次仓库研究为 7.0.0，两者不混称。本套件沿用已有多会话制度及个人 handoff/health-check 技能的方法，独立整理为通用规则；不包含任何原项目角色ID、私有资料或运行数据。

## 从 Ponytail 学什么

**复用优先，省掉没有必要的新系统。** 其核心 Skill 给出了从已有能力、标准库到最小实现的选择顺序，同时保留校验、错误处理与安全要求。本套件直接使用客户端会话工具和 Markdown 记录，不造消息总线、调度器、角色数据库或额外 MCP。来源：[核心 Skill](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/skills/ponytail/SKILL.md)。

**把规则和分发分开。** Ponytail 同时有技能目录、插件清单和生命周期 hooks。本套件借鉴技能加轻量清单的分发方式；没有照搬每次会话/提示自动注入的 hooks，因为用户只需在多会话协作任务中启用规则。来源：[插件清单](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/.codex-plugin/plugin.json)、[hooks 配置](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/hooks/claude-codex-hooks.json)。

**效率结论需要对应的正确性证据。** 其 2026-10-07 benchmark 明确了模型、CLI、任务数、重复次数与覆盖限制：39题、每臂5轮、3臂共585轮；运行环境限制了 agent shell。18道 surgical 题有隐藏正确性测试，其他题的交付/编译检查不能等同全面质量判断。对我们更有价值的是这种可追溯的实验边界，而非把其省 token/耗时比例宣传成我们的效果。本套件目前只有小样本场景核验，不声称效率提升。来源：[benchmark 报告](https://github.com/DietrichGebert/ponytail/blob/09c434ab73ca43761c5d8b0c5d341926c2fba710/benchmarks/results/2026-10-07-agentic.md)。

## 从 Superpowers 学什么

**入口负责路由，阶段文件负责细节。** 技能按规划、执行、调试、审查等任务划分，避免把所有细则塞进每次对话。本套件使用一个入口和按需加载的 references，减少同名/相似技能争抢；建制、派工、巡检与 handoff 均有明确产物。参考：[技能目录](https://github.com/obra/superpowers/tree/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills)。

**给实施者任务契约，给总控真实回执。** 其 implementer prompt 包含目标、上下文、约束、自检及明确交付状态；执行流程保存任务进度，避免上下文恢复后重复完成项。我们把这转译成长会话任务说明与持久变更记录，并保留规格符合性与实际质量的区别。来源：[实施提示](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/subagent-driven-development/implementer-prompt.md)、[执行技能](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/subagent-driven-development/SKILL.md)。

**技能也要用行为场景测试。** writing-skills 强调用压力场景检验规则是否改变执行，不把文档写得长视为有效。本套件记录未加载前的回答、加载后的实际测试文件及局限。基线已能守住核心边界，因此本轮不能证明技能带来改进，只能证明约定被整理且有限场景未出现回退。来源：[writing-skills](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/skills/writing-skills/SKILL.md)。

没有全盘移植其工程流程：临时新 subagent 与长期专业 session 的生命周期不同；小任务不固定走多轮审查；不把每次协作都升级成完整开发流程。7.0.0 执行技能中的持续裁决机制也不用于覆盖用户给定的预算、停止条件或暂停要求。当前 Codex 插件清单显式设置空 hooks，本套件同样不安装生命周期 hook。来源：[Codex 清单](https://github.com/obra/superpowers/blob/bb92a77741419a4ab5f06e711a283343f1ada0c3/.codex-plugin/plugin.json)。

## 我们这套机制应继续保留的部分

1. 用户面对一个总控；按实际交付设置长期角色，已有授权不反复询问。
2. 专业角色交出成果、版本、验证和遗留项，总控核验后收口。
3. 更正必须更新受影响的现行口径，原文和冻结版本保留。
4. 交接有实际接班、自动化承接、ignored 资料独立保全、归档后复核。
5. 巡检只关注变化，覆盖不足如实记录，减少重复唤醒。

这是一层跨项目协作规则，可以与 Ponytail 的实现原则及 Superpowers 的工程技能配合。它不接管客户端权限系统，也不把技能文件当作自动运行的 agent 平台。

## 包装依据

采用根 `plugin.json` 加兼容 `.codex-plugin/plugin.json`；技能可单独安装。依据读取时的 [官方打包文档](https://developers.openai.com/plugins/build/plugins) 与 [技能说明](https://developers.openai.com/plugins/concepts/skills)。本轮没有提交插件市场或验证跨客户端安装；清单存在不等于插件已安装。

## 同领域项目补充对照与后续建议

2026-10-19，为候选名 Baton 查重时发现两个同领域项目。此次读取下列固定版本的 Skill、协议及评测说明，未安装或执行它们；对其机制的描述来自文档，不是本项目验证过的效果。

| 项目与固定版本 | 可借鉴之处 | 本项目的取舍 |
| --- | --- | --- |
| [cablate/baton](https://github.com/cablate/baton/tree/0ab4d2ec5c69820001eeac2a12fab2c87fd3e943) | 派工前评估单人替代方案、独立性、唯一写入主责和最终整合者；考虑重复阅读与整合成本 | setup 已包含小任务单会话及成本判断，可用实际反例验证，避免仅凭空闲并发槽开角色 |
| [jpawchan/baton](https://github.com/jpawchan/baton/tree/ca53c1649f9d1242e51ac43fc3712513067fafcf) | 冻结实际派发的上下文；按任务、轮次、报告、差异摘要绑定审阅证据；运行租约防止旧进程覆盖新状态 | 保留原生会话工具，优先在现有任务记录中明确派发轮次和证据版本；目前没有引入其锁、租约、CLI或调度运行时的必要 |

依据：[派工 Skill](https://github.com/cablate/baton/blob/0ab4d2ec5c69820001eeac2a12fab2c87fd3e943/SKILL.md)、[配对评测协议](https://github.com/cablate/baton/blob/0ab4d2ec5c69820001eeac2a12fab2c87fd3e943/benchmarks/case-01-multi-surface-refactor/protocol.md)、[任务与审阅规范](https://github.com/jpawchan/baton/blob/ca53c1649f9d1242e51ac43fc3712513067fafcf/SPEC.md)、[评测与历史冻结说明](https://github.com/jpawchan/baton/blob/ca53c1649f9d1242e51ac43fc3712513067fafcf/benchmarks/README.md)。

以下是待决策的改进建议，尚未实现，也不扩大当前实验的修订预算：

1. **先闭环安装体验。** 给新用户一个只读核验步骤，分别确认包版本、技能是否被当前宿主发现、所需原生能力及实际可用模式。优先定位已观察到的CLI能发现、桌面清单未出现问题；文件可读与插件安装成功分开记录。
2. **让派工与验收可追溯到同一次尝试。** 复用现有变更记录，必要时保存派发轮次、冻结输入、工具返回及验收产物版本。补一个小型引用核验工具前先确认重复需求；它应覆盖我们实测失败的相对引用，而非再建一套任务数据库。
3. **验证恢复能力。** 下一轮原生实验重点覆盖创建结果不确定、重复投递、过期回执、接班前主责冲突；另行授权和隔离真实handoff/归档验证。已有安全条款不能代替实际恢复证据。
4. **验证拆分是否值得。** 用相同起点、相同任务和独立验收做小规模配对实验，保留失败和未完成样本。除了实际可得的耗时与成本，记录用户搬运上下文次数、重复解释、覆盖冲突和验收遗漏；不能从单次19/20推导质量或效率提升。

本项目继续关注长期专业会话、唯一总控入口和跨阶段接班。共用原则按需吸收；没有真实用例与验收证据前，不扩建后台编排平台或把上游测量结果写成本项目收益。
