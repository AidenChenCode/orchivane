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
