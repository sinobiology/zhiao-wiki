     女娲 skills 是什么？一篇看懂 AI 如何学习“像某个人那样思考” \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

女娲 skills 是什么？一篇看懂 AI 如何学习“像某个人那样思考”
====================================

原创 知奥zhao 知奥ZHAO 2026-04-10 23:41

> 原文地址: [https://mp.weixin.qq.com/s/oiz3pp8PE77cROAs5sVInQ](https://mp.weixin.qq.com/s/oiz3pp8PE77cROAs5sVInQ)

![](https://mmbiz.qpic.cn/mmbiz_png/a3jlfa2zsXLMg0Re25QOsQHColX77YNKuZ58b4eba2xib1vS8vjTH7ibpAX6pWIe1P2LHwibIXxV6llB89uC4ic2U6cxjtIicawzcamRw7icErngE/640?wx_fmt=png&from=appmsg)

文/知奥

这段时间，很多人都在谈 OpenClaw、Agent、技能生态。

表面上看，大家讨论的是 AI 会不会自己上网、会不会自己拆任务、会不会自己调用工具；但往深一层看，真正的分水岭其实只有一句话：

**AI 到底是在“回答问题”，还是在“按某种方法做事”？**

没有技能的 AI，更像一个知识很丰富的聊天对象。你问一句，它答一句；你再追问，它再补充一点。它能说很多，但未必真能把事情做成。

而一旦有了 Skill，情况就变了。

Skill 像是给 AI 装上的“手脚”，也是给它装上的“套路”。它不只是知道什么，更知道遇到一个问题时，应该先看哪里、怎么拆解、去哪里找资料、最后按什么风格交付。也正因如此，OpenClaw 这类自主 Agent 一火，围绕 Skill 的讨论立刻跟着升温。因为 Agent 真正的能力上限，往往不取决于模型本身，而取决于它背后接了什么技能、沿着什么工作流去行动。

而最近这个方向里，最有意思的项目之一，就是 **女娲 skills**。

它有一句很抓人的口号：

> **“你想蒸馏的下一个员工，何必是同事。”** 

这句话之所以让人一下记住，不只是因为它有传播力，更因为它把一个正在发生的变化点了出来：

过去，大家想的是“把同事的工作经验做成 skill”；  
而女娲想做的，是**把任何一个人的思维方式，提炼成可调用的 AI 技能**。

这就不是“复刻某个人会做什么”了，而是更进一步，去逼近一个更难的问题：

**这个人，到底是怎么想问题的？**

* * *

一、女娲不是“角色扮演”，而是“思维方式蒸馏”
-----------------------

很多人第一次看到女娲，容易误会它是在做“AI 扮演名人”。

不是。

它最核心的定位是:  
**女娲不是复制人，而是提炼思维框架。**  
它要捕捉的不是 _WHAT they said_，而是 _HOW they think_。

这句话非常关键。

因为一个人真正值钱的地方，往往不是他说过哪些金句，而是他看世界时默认戴着哪副“镜片”。

比如，有的人一遇到问题，先看激励机制；  
有的人先拆底层约束；  
有的人先问用户要什么；  
有的人先看风险暴露在哪里；  
还有的人，会本能地先判断投入产出比。

这些东西，平时并不总是显眼，但它们构成了一个人长期稳定的认知风格。女娲要做的，就是尽可能把这套东西提炼出来，装进一个可运行的 Skill 里。

按照 `SKILL.md` 的定义，一个好的人物 Skill，至少要包含几层内容：

*   他用什么心智模型看世界
    
*   他用什么决策启发式做判断
    
*   他怎么表达，语言里有什么“DNA”
    
*   他明确反对什么
    
*   以及，这个 Skill 做不到什么、边界在哪里
    

换句话说，女娲想做的不是“名人语录生成器”，而是一个**认知操作系统打包器**。

* * *

二、它和“同事.skill”的区别，恰恰说明了它为什么重要
-----------------------------

  

**同事.skill 证明了蒸馏一个人是可行的。** 但女娲紧接着往前迈了一步：既然连同事都能蒸馏，那为什么不直接蒸馏乔布斯、芒格、费曼、马斯克？(GitHub)

这背后的差别，其实非常大。

“同事.skill”更接近于整理一个人的做事经验：  
他怎么写文档、怎么处理需求、怎么跑流程、怎么复盘问题。

而女娲想蒸馏的，是更上一层的东西：  
**不是“他怎么做”，而是“他为什么会这么做”。**

这就像两个层次的学习：

第一层，是学招式。  
第二层，是学内功。

前者能让你模仿一个动作，后者能让你在新场景里自己出招。

这也是女娲最有价值的地方。因为普通人过去学习高手，往往只有三种方式：读书、听访谈、摘金句。你记住了很多结论，却很难真的拿走对方的判断框架。女娲试图做的，就是把这种分散、零碎、只能“看”的学习，改造成一种可以“调用”的学习。

以后你面对一个问题，问的可能不再是：

“这个人说过什么？”

而是：

“**如果按这个人的思维方式来分析，这件事会怎么看？**”

* * *

三、为什么这个项目会突然火起来？
----------------

从 GitHub 仓库公开页面可以看到，`alchaincyf/nuwa-skill` 发布5天，当前已经获得约 **6.4k stars**、**942+ forks**，并采用 **MIT License** 开源。

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXJbNRmsF7h6gb7KGdeIMxgrzCf4iaCtDQDP1JcHTQ72BmMicVbQfbmZ2Gf27fpLGKhgjr9pHQyibm93qxMCdunXOMdkXfwScxab0o/640?wx_fmt=jpeg&from=appmsg)

一个刚上线不久的项目，能在这么短时间里引发大量关注，原因当然不只是“名字起得好”。

更重要的是，它踩中了一个非常真实的需求变化：

很多人已经不满足于让 AI 帮自己“查资料、写摘要、润文案”了。  
他们真正想要的是：

**AI 能不能让我临时借到一种更强的思考方式？**

这和传统工具的差别很大。

普通工具解决的是“效率问题”；  
而女娲这类项目，开始触碰“判断问题”。

效率工具帮你更快干完原本会干的事；  
认知工具则可能让你换一种方式看问题，甚至避免掉很多本来会犯的错。

这就是它最吸引人的地方。

* * *

四、女娲到底是怎么“造人”的？
---------------

这是整个项目最值得细讲的部分。

### 1\. 它先判断：你是要“蒸馏一个人”，还是要“找一种思维方式”？

在 `SKILL.md` 里，女娲并不是一上来就开工，而是先做入口分流。它把用户需求分成两类：

一类是明确型：  
“蒸馏芒格”“做一个费曼 skill”。

另一类是模糊型：  
“我想提升决策质量”“有没有一种思维方式能帮我看透商业本质”。

前一种，直接进入蒸馏流程。  
后一种，则先做“需求诊断”，根据你的困惑反推更适合蒸馏谁，或者蒸馏一个什么主题。

这个设计非常聪明。

因为多数普通用户并不知道自己“该找谁”。他知道的只是：自己现在在表达、决策、创业、写作、教学、产品、投资这些地方有卡点。女娲先帮他定位问题，再推荐相应的人物视角或主题视角，本质上已经不是一个单纯的生成器，而开始像一个“思维顾问入口”。

* * *

### 2\. 真正干活的，是 6 个并行 Agent

女娲最硬核的一点，是它不是靠一个 Agent 去“搜几篇文章然后总结”，而是明确要求启动 **6 个并行 subagent**，分别处理不同信息维度。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXKDlBjXAIC5Gf0GB9wuEaicpWrvmicoDASGdlZW2KxZ2ia7CElzA2lHC6kqbPNWymjibB1BxRVdqmTCmdzOOI8LVich8ZbDWfpficTxc/640?wx_fmt=png&from=appmsg)

这 6 个 Agent 的分工，大致是：

*   **著作 Agent**：看书、长文、论文、newsletter，找反复出现的核心论点
    
*   **对话 Agent**：看播客、视频、访谈、AMA，找即兴反应和被追问时的回答方式
    
*   **表达 Agent**：看社交媒体和短文，分析高频词、句式、争议立场和表达风格
    
*   **他者 Agent**：看别人对他的评价、书评、批评，补盲区
    
*   **决策 Agent**：看重大决策、关键转折和行为记录，判断“说的”和“做的”是否一致
    
*   **时间线 Agent**：整理完整生平与最近动态，防止 Skill 过时
    

你可以把它理解成：  
**不是在“搜资料”，而是在“拼一个人”。**

如果只看著作，你看到的是他最系统、最体面的那一面；  
如果只看访谈，你看到的是他即兴思考时的底色；  
如果只看社交媒体，你看到的是他最习惯性的表达；  
如果只看别人评价，你又可能被他人的偏见带跑。

六路并行的意义，就是尽量不让任何单一材料，独占这个人的画像解释权。

* * *

### 3\. 不是说过几句漂亮话，就算“心智模型”

女娲最严肃的地方，在于它没有把“人物分析”做成金句摘录。

在 `SKILL.md` 里，它要求所有候选观点必须经过 **三重验证**，才能进入最终 Skill：

**第一，跨域复现。**  
这个观点是不是在两个以上不同话题、不同场景中反复出现？

**第二，预测能力。**  
它能不能帮助你推断这个人面对新问题时的大致立场？

**第三，排他性。**  
这是不是他的独特镜片，而不是所有聪明人都会说的通用套话？

三项都通过，才能升级为“心智模型”；  
只通过一两项，最多降级成“决策启发式”；  
完全不过，就直接丢弃。

这套机制的价值非常大。

因为互联网上最不缺的，就是把一句正确的废话包装成“高手心法”。  
而女娲等于在说：**不够独特、不够稳定、不能生成新判断的观点，不配进 Skill。**

这一下就把它和一般的“名人总结文”拉开了层次。

* * *

### 4\. 它最后生成的，不只是“像谁说话”，而是“按谁的方法做判断”

完成调研和提炼之后，女娲会把结果装进一个标准化的 `SKILL.md` 结构里。

这里面不仅有：

*   心智模型
    
*   决策启发式
    
*   表达 DNA
    
*   价值观与反模式
    
*   智识谱系
    
*   诚实边界
    

更关键的是，它还专门设计了一个部分，叫：

回答工作流（Agentic Protocol）
-----------------------

这一段的意思不是“让 AI 用某个人的语气说话”，而是让它在遇到具体问题时，先判断这个问题属于哪一类，再决定是否需要先做研究，最后按这个人的思维方式输出判断。

这一步，才是女娲最像“技能”而不是“人设卡”的地方。

因为真正厉害的人，从来不只是“表达得像自己”，而是“处理问题的路径和别人不一样”。

女娲想蒸馏的，恰恰就是这条路径。

* * *

五、它已经蒸馏了哪些“脑子”？
---------------

根据 README 当前展示，项目已经内置或示例化了多个人物 Skill，包括：

Paul Graham、张一鸣、Karpathy、Ilya、MrBeast、特朗普、乔布斯、马斯克、芒格、费曼、Naval、塔勒布、张雪峰，以及一个主题型的 **X 导师**。

这件事本身就很说明问题。

因为这份名单并不是一群同类人。  
里面有企业家，有投资者，有科学家，有内容创作者，也有现实风格非常强的公众人物。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXJOiaic3yteSuQAzglBdPmOo0otibgrY34IBwnFBvEO8TpDhld6icMlXOOBg28SicAicNfjC2NrSTxoPa3bQLolTApNicVAy6NS6dADJA/640?wx_fmt=png&from=appmsg)

这说明女娲并不是在做“名人周边”，而是在做一个更底层的东西：  
**把不同类型的认知方式，整理成一个可随时切换的工具箱。**

你要学表达，可以调用费曼；  
要学决策，可以调用芒格；  
要学注意力和传播，可以看 MrBeast；  
要学现实约束和投入产出，张雪峰这类视角就很有代表性。

它真正值钱的不是“蒸馏了多少人”，而是你第一次会直观意识到：

**原来学习一个高手，不一定非得读完他一整套作品之后再慢慢消化；你也可以先调用他的判断镜头来处理自己的问题。**

* * *

六、普通人拿它来干什么？
------------

如果只是从操作层面看，女娲的安装并不复杂。README 提供的方式是一条命令：

`npx skills add alchaincyf/nuwa-skill` 

装好之后，你既可以自己蒸馏新人物，也可以直接调用现成视角。比如 README 里展示的用法，就是“蒸馏一个保罗·格雷厄姆”“造一个张小龙的视角 Skill”“用芒格的视角分析投资决策”“费曼会怎么解释量子计算”等。

但在我看来，它真正的价值，不在“能不能用”，而在“会改变什么”。

### 第一，它改变了普通人的学习方式

过去我们学一个高手，很像在旁听。  
看书、看访谈、记金句、做摘录。

现在则更像是把对方请到你面前，让他帮你一起看一个具体问题。

这两种学习方式，差别很大。

前者学到的是知识；  
后者更容易逼近方法。

* * *

### 第二，它给了人一种“借视角”的能力

很多人遇到问题反复卡住，并不是因为信息太少，而是因为只会从自己的惯性出发。

同一个问题，你总是从同一扇窗往外看，自然容易得到同一种答案。

而人物 Skill 的价值，就是强行帮你换窗。

比如你在做职业决策时，  
芒格会先看激励和长期复利；  
塔勒布会先看下行风险和可选性；  
张雪峰可能会先看现实回报和资源约束；  
乔布斯则会问，你到底有没有品味和聚焦。

这些答案未必一致。  
但正因为不一致，你才第一次看见自己原来遗漏了哪些变量。

* * *

### 第三，它让“比较不同思维方式”这件事，第一次变得很直观

这可能是最重要的一点。

女娲并不是在告诉你：某个人的脑子最好，其他人都不行。

恰恰相反，它是在提醒你：  
**不同的人之所以得出不同结论，不是因为谁更聪明，而是因为他们默认关注的东西不同。**

  
  
  
  

当这些视角能被并排摆出来，你才会第一次真正理解：

原来“判断”这件事，不只是信息处理，更是价值排序。

* * *

七、女娲最值得肯定的一点，是它没有把自己吹成“数字分身神话”
------------------------------

现在很多 AI 项目，一讲到“蒸馏一个人”，很容易滑向一种夸张叙事：  
仿佛真的可以把某个人完整复制出来。

但女娲在文档里反而非常克制。

它反复强调，Skill 有明确边界：

*   不能预测这个人面对全新问题时一定会怎么反应
    
*   不能替代真正的创造力和直觉
    
*   公开表达和真实想法之间可能有差距
    
*   信息只截止到调研当时，活人会变化，Skill 也会过时
    

我反而觉得，这种诚实，是它最像一个成熟项目的地方。

因为越是涉及“模拟认知”的事情，越应该警惕一种幻觉：  
以为抓到了一些表达习惯、一些历史材料，就等于“得到了这个人”。

并没有。

你得到的，最多只是一个尽量忠实、尽量结构化、尽量有边界感的认知近似体。

但即便只是“近似体”，它也已经足够有用。  
因为多数时候，我们需要的本来就不是一个真人复活，而是一个更好的思考支架。

* * *

结尾：未来最值钱的 AI，也许不是替你做事，而是替你减少低质量判断
---------------------------------

我觉得，女娲 skills 真正让人兴奋的地方，不只是它做出了一个有趣的开源项目，而是它把一个原本很模糊的问题，第一次具体地摆到了大家面前：

**如果思维方式也能被部分提炼、整理、调用，那么“学习高手”这件事，会不会被重新定义？**

过去，成长往往意味着你要自己去读很多书、踩很多坑、慢慢形成自己的方法。  
未来，也许你依然要读书、依然要踩坑，但中间会多出一种新的可能：

当你遇到一个问题时，  
你可以临时调用一个费曼式解释框架，  
一个芒格式判断框架，  
一个乔布斯式产品过滤器，  
一个塔勒布式风险扫描器。

它们当然不是那些人本人。  
但它们可能已经足够帮你，把问题重新看一遍。

而很多时候，人真正缺的，可能不是答案，  
而只是——**另一种看问题的方式。**

这大概就是女娲 skills 最迷人的地方。

* * *

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言