     AI炒股靠谱吗？我让12个AI真实跑了一遍 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

AI炒股靠谱吗？我让12个AI真实跑了一遍
=====================

原创 知奥zhao 知奥ZHAO 2026-05-20 20:52

> 原文地址: [https://mp.weixin.qq.com/s/\_eBfIgMkbkfYcXfp3LwjKQ](https://mp.weixin.qq.com/s/_eBfIgMkbkfYcXfp3LwjKQ)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXIgx0WYv9l1as08lgVQyLspSySlGibqbKiaCluwTAicPlqRHgUPyia6Mibr84mSD6sbQcwXrxBUHG69IbMV7jI7pxFyUjzmkhqvHGzw/640?wx_fmt=png&from=appmsg)

文/知奥

  

写在前面

一个不会写代码的人，能不能靠 AI 把一套复杂的多智能体系统跑起来？

我用一个周末做了实验。结果真的跑通了。

这篇文章记录的是这个过程：环境怎么配、报错怎么解决、AI 搭档怎么协作，以及 12 个智能体如何完成一次从数据采集到投资裁决的完整推演。起点是【前哨AI小课第5季】的第 11 课的实战内容，我专门为跑这类实验入手了一台 MacBook Air——新电脑，没有历史包袱，权限开到最大。

  

一、这个项目是什么？

要部署的项目是在 GitHub的一个开源项目，叫 TradingAgents（TauricResearch/TradingAgents）。

19.8 万 star，作者团队还发了论文。

它的核心设计思路只有一句话：把华尔街投行的研究流程，用AI智能体来模拟。

不是一个 AI，而是 12 个。5 支团队，按流水线依次工作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXJb3icia81L2kXb4lQ1qXwE6zbCpkfYGQRvKcdJ1mia3ibPUg2VcDJ0lWGTpXjbTspGJUIybAqiccMDhf0rDcOObvdOXSCDkYuhhy7A/640?wx_fmt=png&from=appmsg)

后台跑的是大语言模型——OpenAI、Anthropic、Google、DeepSeek，任选。

关键洞察：这不是“让 AI 帮你炒股”的工具。它的价值在于辩论机制——强制让 AI 从多个对立角度审视同一只股票，避免单一模型的确认偏差。一个 AI 给你答案，容易自说自话；多个 AI 相互质疑，才可能逼出更接近真实的判断。

  

二、部署过程：一场真实的人机协作

我不是程序员。我甚至不太会配环境变量。

但我有两个 AI 搭档同时在线：

*   Claude Code：在终端里直接对话的 AI 编程助手，遇到报错贴给它，它帮你分析原因、给出命令、再验证结果；
    
*   豆包：开启共享屏幕和共享终端模式，直接看到我的操作界面，能实时发现我自己都没意识到的问题。
    

整个部署过程，就是在这两个搭档的接力帮助下推进的。

![](https://mmbiz.qpic.cn/mmbiz_png/a3jlfa2zsXKg0ArGHcicEbQPY4QO4lP7N4mKcxvqFuqiboP72cJw7AjcBJcnzib8vmeUlVJINrI7naUEGicRpAPjBYm8Xv9mCXjUO16kqJ9kDrQ/640?wx_fmt=png&from=appmsg)

第一步：克隆项目，基础安装

git clone https：//github.com/TauricResearch/TradingAgents.git cd TradingAgents python3 -m venv .venv .venv/bin/pip install -e .

这一步顺利，没什么好说的。

第二步：三连报错

第一次运行，报错了。

ImportError： Using SOCKS proxy， but the 'socksio' package is not installed.

翻译成人话：你开了 SOCKS5 代理，但系统缺一个叫 socksio 的包。

尝试安装，又踩坑——在 zsh 终端里，pip install httpx\[socks\] 会报“no matches found”，因为方括号在 zsh 里有特殊含义，需要加引号：

.venv/bin/pip install 'httpx\[socks\]'

但因为 SSL 证书问题，PyPI 直连失败了。换清华镜像源：

.venv/bin/pip install -i https：//pypi.tuna.tsinghua.edu.cn/simple socksio

装完重跑，又报错——

ConnectError： \[Errno 61\] Connection refused

代理端口写错了。我写的是 33210，实际上跑在 7890。

把所有代理变量清掉重来：

unset http\_proxy https\_proxy all\_proxy HTTP\_PROXY HTTPS\_PROXY ALL\_PROXY export http\_proxy=http：//127.0.0.1：7890 export https\_proxy=http：//127.0.0.1：7890

这三连报错，是两个 AI 搭档接力解决的。

值得单独说一个细节：中间有一次，豆包通过共享终端直接看到了我的操作，它发现我写的是 $env：HTTP\_PROXY=“xxx”——这是 Windows PowerShell 的语法，在 Mac 的 zsh 里根本不生效。这个坑的来源很典型：我之前长期用 Windows，肌肉记忆带过来了，自己完全没意识到。如果只是把报错截图给 AI 看，这个问题很难被发现；但豆包看到了我的整个终端界面，一眼就定位了。顺带一提，这类系统差异我到现在也没完全搞清楚，但 AI 说怎么改我就怎么改，问题就解决了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXJfRCKqxal0YnReA6OrAuf6sbP7USgg2XaUNLda0dKvxV7ZTZqyaGFQGZkNliaXakajYRibh4cBibIjH605Z0lvofhwic82icicdJUTc/640?wx_fmt=png&from=appmsg)

这就是「共享屏幕」和「贴报错截图」之间的本质区别：一个看到的是症状，一个看到的是现场。

最后诊断出的国内部署开源项目核心原则：pip 装包时关代理（或用镜像源），程序调用 API 时开 HTTP 代理，永远不要设 all\_proxy 的 SOCKS 代理。

第三步：配置参数，正式启动

排除网络问题后，CLI 成功启动，弹出一个交互式配置界面：

配置项

我的选择

说明

股票代码

CRCL

Circle Internet Group，USDC 发行方

分析日期

2026-05-19

当前最新数据

输出语言

中文

直接出中文报告

分析师团队

全选 4 个

技术/情绪/新闻/基本面全上

研究深度

Medium

2 轮辩论，平衡速度与深度

LLM 供应商

DeepSeek

性价比最高

模型配置

Flash + Pro 双引擎

Flash 跑分析师（频繁调用），Pro 跑决策（深度推理）

选 DeepSeek 的逻辑很简单：成本。Flash 模型负责 4 个分析师和辩论环节，调用频繁，追求速度；Pro 模型负责研究主管和最终决策，调用次数少，但需要深度推理。这个搭配下来，一次完整分析的 API 成本是几毛钱。

  

三、15分钟53秒：一场实时的智能体协作

确认配置后，终端变成了一个实时仪表盘。

左侧是进度面板，12 个智能体的状态在跳动：市场分析师 in progress、情绪分析师 completed、新闻分析师 completed……右侧是消息面板，每个智能体的思考过程、工具调用、中间结论滚动输出。

整整 15 分53 秒。

期间有两个小插曲值得记录：

社交媒体数据获取失败，但智能体没有崩溃

StockTwits 和 Reddit 的数据抓取因为 SSL 问题全部失败。情绪分析师在报告里诚实地写道：

“在 r/wallstreetbets、r/stocks、r/investing 上均未找到任何提及 CRCL 的帖子。影响：CRCL 在主流散户讨论社区中的热度极低。”

它把数据缺失本身当作一个信号来分析，而不是报错退出。这种鲁棒性设计是好的。

结构化输出降级，但流程没中断

研究主管和投资组合经理的 Pydantic 模型解析失败，系统自动降级为自由文本输出：

Research Manager： structured-output invocation failed； retrying once as free text Portfolio Manager： structured-output invocation failed； retrying once as free text

可能是 DeepSeek 对特定 JSON Schema 的兼容性问题，但降级策略保证了主流程不中断。

最终数据：LLM 调用 29 次，工具调用 22 次，消耗 token 约 42 万，生成 7 份报告。

  

四、智能体在终端里真的吵起来了

先说清楚：下面这段不是为了讨论 CRCL 值不值得买，而是为了观察——多智能体系统在面对同一只股票时，是如何形成一个有交叉质询支撑的判断的。

最精彩的部分在第二阶段——研究团队的多空辩论。

我把这一段原文摘出来，因为它值得仔细读。

  

看多研究员的开场：

“我看到对面的熊派分析师已经把数据摊了一桌子，又是 MACD 快死叉，又是毛利率暴跌到 8%，还搬出了老虎环球清仓的消息。说实话，我听完之后，第一反应不是害怕，而是觉得——这恰恰是我们这些有准备的投资者，应该贪婪的时刻。”

核心论点四条：回调是正常洗盘（50/200 日均线完好）；毛利率下滑是一次性费用扭曲，Q3/Q4 已连续盈利；《Clarity Act》是 USDC 的合规护城河；贝莱德领投 2.22 亿美元私募，顶级机构背书。

结论：强力买入，当前回调是战略性建仓的黄金窗口。

  

看空研究员的反击：

“你刚刚那一番话，听起来头头是道，但很可惜，你用来支撑故事的论据，经不起数据的推敲。”

然后一刀一刀切下来。

第一刀，关于毛利率。 看多说是“战略性投入”导致的暂时性下滑。看空追问：

“那你解释一下，为什么全年资本支出只有 5600 万美元，占营收不足 2%？如果真在进行大规模战略转型，capex 应该同步增长。钱花哪儿了？”

看多方没有回答这个问题。

就这样。整段辩论记录里，这个追问之后，是一段空白。这是整场辩论的第一个转折点——不是因为看空方说得有多精彩，而是因为看多方选择了沉默。

  

第二刀，关于贝莱德投资。 看多一再引用贝莱德领投 2.22 亿美元私募融资，称之为“最强背书”。看空的核心反击是：

“贝莱德选择私募而非在公开市场以 111 美元买入，恰恰说明他们认为二级市场价格并不便宜。私募投资者享有的锁定期、折扣和优先条款，使其风险回报结构与二级市场散户截然不同。将两者等同，是对风险结构的根本性误读。”

看多方的回应是：贝莱德的参与“象征着主流金融机构对加密赛道的认可”。

看空方接着问：你能解释一下，认可赛道，和认可当前股价，这两件事是一回事吗？

又是沉默。

  

第三刀，关于现金流。 看多把 5.42 亿经营现金流作为核心亮点，认为这说明核心业务“极其强劲”。看空拆解了一组数字：总资产 787.1 亿美元中，758.9 亿是受限现金——那是 USDC 储备金，不是公司资产，法律上不属于 Circle 可以动用的钱。真实可支配现金只有 15.3 亿。

看多方没有正面回应这个数字，转而强调“自由现金流转化率高”。

研究主管后来在裁决里专门提到：看多方在三个关键节点的回应质量明显弱于看空方，这是最终裁决倾向空方的核心依据。

![](https://mmbiz.qpic.cn/mmbiz_png/a3jlfa2zsXLRic5OQkIO16oEDibCH7zEYicAEoHBuNsEfibnhgKGian3zIN9pTYGfYuWxnTxA0ZyYxsrSICVwJ3eBK6ajcc3HickkUyEoJPQN44Bc/640?wx_fmt=png&from=appmsg)

  

五、系统给出的推理结论：这是样本，不是建议

16 分钟后，系统弹出一行字：

Analysis Complete! Agents： 12/12 | LLM： 29 | Tools： 22 | Tokens： 366.6k | Reports： 7/7

投资组合经理在这次样本分析中给出的结论：SELL，参考价格 $111.39。

理由如下：

维度

多方论据

空方论据

最终权重

基本面

营收 +63.5%、FCF 5.4 亿

TTM 亏损、毛利率 8%

空方偏重

技术面

50/200 均线完好

跌破 10EMA、MACD 缩减

平衡

催化剂

Clarity Act、BlackRock

Tiger Global 清仓

多方偏重

估值

PEG 4.34 相对合理

PE 50x 已包含乐观预期

空方偏重

风险

高增长潜力

加密敏感性、宏观逆风

空方偏重

三个维度空方偏重，不是拍脑袋的结论——它有辩论记录作为依据。研究主管的裁决里写得很清楚：熊方在毛利率和估值两个维度的论据更扎实，根本原因是牛方对「增量营收为何不带来增量毛利」这个问题，始终没有给出有说服力的回答。胜负不是打分打出来的，是一方论据被追问后沉默了。

![](https://mmbiz.qpic.cn/mmbiz_png/a3jlfa2zsXIUuibTZgficlCKXPAL5RTgNCfSaufAz5lD49Lvicbw9lFiaYsXTtBnx5Jr9MXCnQ9wUkagSg5iau33uS8LDNqwNadbjmiaWZF214L9o/640?wx_fmt=png&from=appmsg)

最终结论里有一段，我觉得写得很好：

“CRCL 是一家业务赛道具有长期价值的公司，这一点在辩论中三方并无本质分歧。但投资决策的核心永远不是'公司是否好'，而是'当前价格是否好'。在 111 美元的价格上，CRCL 尚未达到那个标准。”

不像随口生成的答案。更像一份经过交叉质询后的阶段性判断。

像一个真正研究过的人，在交叉验证之后得出的结论。

  

六、这次实验让我想了什么

关于这个系统的价值边界

必须说清楚：这个系统的输出不是投资建议，也不应该被当作投资建议。

它的真正价值在三个地方：

第一，信息聚合。15 分钟内完成了一个分析师团队可能需要几天的数据收集和初步整理——技术指标、新闻事件、财务数据、机构动向，一次性拉取，格式化输出。

第二，对抗性思维。强制从多空两个角度审视同一只资产，避免单一视角的确认偏差。你让一个 AI 分析一只股票，它很可能会顺着你想听的方向说；你让两个 AI 互相怼，才可能看到真实的论据强度。

第三，结构化起点。报告的格式规范、逻辑层层递进，适合作为深度研究的起点，而不是终点。

关于人在哪里

在这次部署中，我做了三件事：选股票、选配置、修复代理端口。

但这三件事里，有一件是真正需要人判断的：参数决策。为什么选 CRCL 而不是别的股票？为什么用 DeepSeek 而不是 GPT？研究深度选 Medium 而不是 Deep，意味着什么——2 轮辩论和 3 轮辩论，结论会不会不同？

这些问题，AI 无法替你问，也无法替你判断。

工具越强，人的判断框架就越重要。因为当工具能帮你做任何事情的时候，“做什么”就变成了决定性的问题。

关于两个 AI 搭档的分工

这次部署里，Claude Code 和豆包的分工自然形成了两种模式：

Claude Code 负责被动诊断——你把报错贴给它，它分析、出方案、你执行。信息是你过滤后传递过去的。

豆包的共享终端负责主动观察——它直接看到你的操作现场，能捕捉到你自己都没注意到的问题。那次 $env： 的 Windows 语法错误，就是这样被发现的：不是我意识到哪里不对，而是豆包看到了整个界面，直接点出来的。

两种模式是互补的。前者适合「我知道哪里出了问题，需要解决方案」；后者适合「我不知道哪里出了问题，需要有人看着我」。

关于输入方式本身

还有一件事值得单独说——跟 AI 协作，输入方式本身也是效率的一部分。

这次部署过程中，我大量用了豆包输入法的语音输入来跟 AI 对话。

逻辑很简单：正常说话速度是打字的 3 到 5 倍，而 AI 时代，你给的信息量远比精准度重要。你打字给 AI 描述一个报错，可能只有几十个字；你张嘴说，自然就会把前因后果、试过的方案、卡在哪里全说出来——AI 拿到足够的上下文，给出的回答质量完全不一样。

豆包输入法 Mac 版今年才上线，在此之前电脑端的语音输入一直是一片荒漠。这个版本流式输出，说完即入，识别准确率极高，中英混说也基本没问题（对我这种英文苦手很重要），用久了会越来越懂你的高频词汇。

我不是在推荐某个具体产品，而是想强调一件事：AI 时代，输入方式本身也会影响协作效率。语音输入让上下文供给变得更充分，这一点比选什么工具更重要。我现在已经完全换成语音输入，回不去了。如果你也在高频跟 AI 对话，值得试一次。

  

七、给想试试的人：最小部署步骤

环境要求

*   Python 3.10+
    
*   一个 LLM API Key（推荐 DeepSeek，性价比最高）
    
*   网络能访问 API 端点（国内需要 HTTP 代理）
    

完整命令

\# 1. 克隆项目 git clone https：//github.com/TauricResearch/TradingAgents.git cd TradingAgents  

\# 2. 创建虚拟环境并安装 python3 -m venv .venv .venv/bin/pip install -e .  

\# 3. 安装 SOCKS 代理支持（用镜像源） .venv/bin/pip install -i https：//pypi.tuna.tsinghua.edu.cn/simple socksio  

\# 4. 配置 API Key（以 DeepSeek 为例） echo “DEEPSEEK\_API\_KEY=sk-your-key-here” >； .env  

\# 5. 配置代理（关键！） unset all\_proxy ALL\_PROXY  # 清掉 SOCKS export http\_proxy=http：//127.0.0.1：7890 export https\_proxy=http：//127.0.0.1：7890  

\# 6. 启动 .venv/bin/tradingagents

成本参考

用 DeepSeek V4 Flash + Pro 分析一只股票，约消耗 42 万 token，单次成本约 不到一块钱人民币。换成 GPT-4o 或 Claude 3.5 Sonnet，成本会高出约一个数量级。

  

结语

12 个 AI 智能体，花了 15 分钟 53 秒，完成了技术分析、基本面研究、多空辩论、风控审查和最终决策的完整流程，输出了一份逻辑清晰的中文研究报告。

“卖出”建议是否正确，不重要。

重要的是：它是通过辩论得出的，而不是通过计算得出的。看多方提论点，看空方拆论据，来回几轮，直到有一方被追问后沉默了。这个过程，比任何一份单向分析报告都更有参考价值——因为你能看到推理的全貌，知道哪些假设经得起质疑，哪些没有。

那个「当前价格是否好」的结论，不像随口生成的答案。像一个真正研究过的人，在交叉验证之后得出的判断。

这才是这套机制真正有价值的地方。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXKmuKpt3QNdFRYZQYmpMC1WWhRj2ce9TYVUp383FkwommFhcc4nkp8JezmpgN9SK4EOOGrcUVpgnibzjuXIg1OqeIfV8mv1SorE/640?wx_fmt=png&from=appmsg)

  

最后说一件事。

我有个习惯：学完一个东西、跑完一个项目，把自己和 AI 协作的过程整理成文章发出来。这是费曼学习法的实践——能讲清楚，才说明真的懂了。而公开发表还有另一层价值：它会帮你找到同频的人。你写什么、怎么学、关注什么，本身就是一个信号。

这篇文章就是这么来的。

也感谢前哨AI小课铺了这条路。很多时候，普通人不是没有学习能力，而是缺一条可以照着走的路。当路被铺出来，剩下的就是亲手试一次。

  

免责声明：本文仅记录技术部署过程和实验结果，不构成任何投资建议。股市有风险，投资需谨慎。

项目地址：github.com/TauricResearch/TradingAgents

  

* * *

推荐阅读：

*   [用GPT Image2.0+Seedance2.0，满足孩子篮球明星梦](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488305&idx=1&sn=29e0442f8ef257c21ab6014d9b1621c9&scene=21#wechat_redirect)
    
*   [我不会写代码，但我用AI做出了3个数学动画 | 一次「养马」的完整记录](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488253&idx=1&sn=0f168f47e63f2ea240b10065a6eeb89b&scene=21#wechat_redirect)
    
*   [日更235天不如AI编程一天？| 不懂代码，24小时造出自己的数字大脑](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488213&idx=1&sn=f195d4aeddbd8dc9207239975a169406&scene=21#wechat_redirect)
    
*   [AI才是完美主义者和拖延症的天然解药](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488015&idx=1&sn=9c4dc23d1853c7277dfe58b338f910e5&scene=21#wechat_redirect)
    
*   [我不会写代码，但我做出了一个 App：一次对“自然语言编程”的祛魅](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247487938&idx=1&sn=821245016d014c84d81bc99c0529f12b&scene=21#wechat_redirect)
    
*   [把你工作中的所有事都用AI先做一遍——AI的最高水平，理应成为你的最低水平](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247484202&idx=1&sn=40ce54be9ae84c24fa0b5e1277ab2470&scene=21#wechat_redirect)
    

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言