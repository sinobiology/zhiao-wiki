     《氨基酸进化》系列创作手记：一个发酵工程师的“人+AI协作”写作流程 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

《氨基酸进化》系列创作手记：一个发酵工程师的“人+AI协作”写作流程
==================================

原创 知奥zhao 知奥ZHAO 2026-01-31 20:58

> 原文地址: [https://mp.weixin.qq.com/s/tBXfvl4jDBsC9y6oKKd59A](https://mp.weixin.qq.com/s/tBXfvl4jDBsC9y6oKKd59A)

### 写在前面： 

转眼到了周六，也到了 2026 年 1 月的最后一天。我这周格外累，不是因为写不出来，而是因为——我给自己挖了个坑。

原计划只写《氨基酸进化》第 5 篇：缬氨酸。调研做完，先长出了一篇 15000 字的深度报告；让 AI 反复精简压缩，仍在 6000 字以上，而且总觉得“该有的细节少了”。于是我干脆给 AI 下了个更大胆的指令：**把一篇文章策划成一个小专题**。

当第一篇标题里出现“（1/5）”进度条时，我意识到这事没法停：只能一口气更完。

也正因为这次“连载事故”，我决定把《氨基酸进化》这个系列的创作过程，做一次公开复盘。

《氨基酸进化》系列是知奥公众号阅读量最高的系列。其中《蛋氨酸——生物发酵攻打的"最后堡垒"》一篇已经突破7000人次,至今保持着最高阅读量纪录。

今天系统复盘不是工具推荐,而是一次"人+AI协作"的完整流程展示——从选题策划到红线规避,从深度调研到风格转化。

如果你也在思考如何用AI提升创作效率,或许这个案例能给你一些启发。

  

01 起点：一本英文经典 + AI 读书能力，把我从“想读”推到“能写”

写这个系列的原点是一本经典的代谢工程书籍——《Amino Acid Biosynthesis – Pathways, Regulation and Metabolic Engineering》(氨基酸生物合成途径、调控和代谢工程)。

![Lightbox view of the cover for Amino Acid Biosynthesis – Pathways, Regulation and Metabolic Engineering](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37A3d9dLq9sSHU79a1zGoRpZicEQqI9jJXYrvawYPicW3zqnBoh0w1jgMbIUuM3BGPG314aceDUxjvOA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

因为全英文、信息密度又高，我一直没能完整通读，但又很清楚它的价值。刚好现在可以借助 NotebookLM 这类工具，把“读书 + 总结”这件事做得更高效。我先用 NotebookLM的知识库能力做书籍摘要与要点提取，再与 ChatGPT 反复对话，把这些要点“推演”成一个可连载的写作策划——也就是后来的《氨基酸进化》系列。

这里有个我越来越确信的结论：

AI 时代的好处不只是“你有想法，AI 帮你实现”；更多时候是“你本来没想法，聊着聊着它把你的想法逼出来”。

  

02 策划:我不是先写文章，而是先让 AI 写“系列说明书”

我最早的念头很简单：让 ChatGPT 把这本书解读一遍，方便自己学习。在对话中，ChatGPT 帮我快速梳理了全书的章节结构，并把价值点总结得很到位：它是跨学科整合的写法，既有工业导向，也有机制深度，还有方法论前沿。  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37BuicCUIaXbIsFr0lZQDHCmADdDeZB0347vPhLek7ic02xpvHKEWWogcQldVcsibdGVJHmBvBLQzPyzg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37BuicCUIaXbIsFr0lZQDHCmAzowu0mxz8k0g5yVsxuktE4sgHEMss6yzVlHUviaiaApGfO2qBEllpKkg/640?wx_fmt=jpeg&from=appmsg)

它的回答启发了我，这让我冒出一个更明确的想法，于是我给 AI 下了一个“策划指令”：

"我想做一个微信公众号的写作专题,分别以每一个氨基酸的生物合成、代谢调控及工业菌种开发的最新前沿为题。写一个系列。你帮我策划一下,每篇的内容框架,以及需要参考哪些资料。"

随后，ChatGPT 给出了 20 篇文章的选题框架：基本是一种氨基酸对应一篇，并且每篇都能用一句“主题句”概括其生理特点与工业价值，比如：

《谷氨酸:味精之外的生命代谢枢纽》

《苏氨酸:饲料里的隐形英雄》

......

这些主题句的好处是：一旦“题眼”立住，后面的结构、材料与故事线就有了落点。

  

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37BuicCUIaXbIsFr0lZQDHCmAo6hKyEakofT1vOiaOWwRqVuBHM8cNcj9u1FC38yV8a17z446j08WwMw/640?wx_fmt=jpeg&from=appmsg)

  

最让我心动的是，它给这个系列起的 Slogan：**“从生命的起点到工业的巅峰”**。

这这句话让我一下有了代入感——它刚好贴合我的职业身份。我们做研发，本质上就是把构成“生命起点”的氨基酸分子，想办法实现工业化，做到成本、规模与稳定性的“巅峰”。

在选题框架之后，ChatGPT 还给出了每篇文章的内容框架与“标准模板”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37BuicCUIaXbIsFr0lZQDHCmAyX0hibYXf7nYXgnSNx7rACzPZ9eNQ04CMWUkib0pNMGNeDWDSicJIlasA/640?wx_fmt=jpeg&from=appmsg)

  

**标准模板（我后续基本沿用）**：

*   **科学 + 产业的故事切入**：用一个产业现象或科学发现开场
    
*   **如何走到工业化**：生物合成、代谢调控、菌种开发、工艺路径
    
*   **工业化与竞争格局**：玩家、供需、专利、贸易与地缘变量
    
*   **未来展望与升华**：技术趋势 → 产业趋势 → 方法论/心法
    

更重要的是，它给了我一套“资料来源体系”：经典书籍、最新期刊论文、专利数据库、企业年报/公告等，并建议把素材沉淀成数据库。  
这对做系列写作非常关键：只要资料体系搭好，后面每一篇就不是“临时起意”，而是“按图施工”。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37BuicCUIaXbIsFr0lZQDHCmAyzRoNbuoNDmRJSiaLYFmBb55uRuykVaJFYUDIQPSf2UGmsuzWepHfIw/640?wx_fmt=jpeg&from=appmsg)

它还给出了输出节奏与配图风格建议（例如每周一篇、20 周完结）。这些建议我未必完全照做，但它确实把“系列化写作”的工程化思路一次性铺开了。

至此,这个系列的策划阶段基本完成,形成了一个全面的写作计划和方案。到这里，我才意识到：公众号写作不是“写一篇”，而是“建一个能持续产出的系统”。策划这一步，AI 是天生强项。

但必须强调：AI 给的是框架与素材路径；真正决定文章上限的，仍然是人的取舍、判断与责任。

  

03 调研:深度挖掘与交叉验证

有了策划案，接下来进入“创作执行”。我用最近的《缬氨酸》为例，讲讲一篇文章是怎么从 0 到 1 出来的。

首先是建立"AI First"的思维习惯。我在文章《[把你工作中的所有事都用AI先做一遍——AI的最高水平,理应成为你的最低水平](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247484202&idx=1&sn=40ce54be9ae84c24fa0b5e1277ab2470&scene=21#wechat_redirect)》里讲过,把你手头能做的事情让AI先做一遍,是这个时代的最基本素质,而且我的心得体会是"能动嘴的,绝不动手"。也就是说，能用语言明确需求AI做的，就尽量不要自己去做那些低价值的重复劳动，把人的精力留给判断与取舍。

这不是偷懒,而是效率革命。AI 时代的核心能力，不是“会不会用工具”，而是“会不会提问题、会不会定义任务”。

还是回到创作,我会用chatGPT 5.2 Thinking和Gemini 3这两个大模型做同题调研，原因很简单：交叉验证。同一个提示词喂给两个模型，能显著减少“单模型幻觉 + 单一信息源偏见”。当两边结论不一致时，我会回到原始出处（论文/专利/年报/公告）再确认——宁可删掉，也不硬写。

我当时用的提示词如下:

我要调研缬氨酸的课题,包括缬氨酸在动物营养方面的作用机理以及与其他氨基酸的相互关系、缬氨酸的生产方法演变、发酵法实现工业化生产的最早厂家、目前的市场竞争情况(产能规模、需求量、主要玩家、博弈关系)、实现高产缬氨酸的主要合成生物学方法、为什么缬氨酸可以实现完全厌氧生产,完全厌氧法和微好氧法的主要优劣势?缬氨酸的专利战、贸易战、地缘战?缬氨酸的历史地位及未来发展趋势。

如果你一开始不会写提示词，也不用被“提示词工程”吓住，照样可以问AI,让它告诉你提示词应该怎么写，示例如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37BuicCUIaXbIsFr0lZQDHCmA5sPMuaj6n1MxyiahFdBicBTaa2od901z942CRSlgU5XE44sFbKMMIsyA/640?wx_fmt=jpeg)

言归正传,现在两个大模型都给你做好了深度调研,接下来就可以根据调研内容发布公众号文章了吗?

中间至少还有两步:

**1.人工校准**：用你的经验指出“哪里不对/哪里不够产业化”，让 AI 继续追；

**2.公众号转化**：把“是什么”改写成“为什么”，让读者感到“这和我有关”。

补充调研的深浅，取决于你对这个话题的理解程度。AI 的公开资料来源往往更偏学术/机构叙事，而产业界尤其是工艺细节并不总是公开可得，这就可能出现“结论与主流实践脱节”的情况。  
这时你需要做的不是照单全收，而是明确提出：**工业界更关心的指标是什么？成本/稳定性/放大风险/合规边界分别怎么影响决策？**  

举个具体例子:AI调研缬氨酸时,会把"完全厌氧法"和"微好氧法"的优劣势讲得很学术——什么代谢通量、氧化还原平衡。但作为发酵工程师,我知道工业界更关心的是"哪个成本低""哪个稳定性好"。所以我会追问AI:"在实际生产中,完全厌氧法的染菌风险是不是更低?设备投资差多少?"

这个环节才真正体现“人的价值”：AI 更擅长回答“是什么”，而你需要对外输出“为什么”——以及“因此我应该怎么判断/怎么选择”。

  

04 转化:从调研报告到公众号文章

重点说说如何"把调研报告转化成公众号风格的内容"。

调研报告解决的是“是什么”，而公众号文章要解决的是“为什么”。它必须让读者感到：**我为什么要知道？这和我有什么关系？它能帮我做什么判断？**

在AI工具这么方便的时代,告诉读者"是什么"已经没有很大价值了,也就是说靠"信息差"吸引读者的逻辑已经不成立了,因为现在每个人手机里随便问一下豆包、元宝、Kimi任何一个AI工具都可以随时告诉你最全面的答案。

所以,公众号文章要想对读者有价值,一个必要的转变就是：**用问题驱动结构，而不是用知识点堆叠结构。。**

之前我在得到课程《做课的方法》里听过一句话，印象很深：世界不是由领域构成的，而是由挑战构成的。写作同理——把问题还原到场景里，读者才会觉得“这事跟我有关”。

比如写《蛋氨酸》时,我不是从"蛋氨酸的生物合成途径"开始讲(这是领域视角),而是从"为什么蛋氨酸是最后堡垒"开始讲(这是挑战视角)。读者关心的不是"蛋氨酸怎么合成",而是"为什么这么难合成,难在哪里?"。

这是我的《氨基酸进化》系列文章表达风格的主要出发点和创作心法。

当然现在已经有了AI工具,在表达风格上也已经可以实现自动化了。在表达风格上，我用的工具是 **GetDraft**（Get 笔记出版）。你把自己 10 篇以内的文章喂给它，它可以提取你的写作风格，形成一个“风格画像”，然后把后续内容改写成更一致的表达。  
我对“风格自动化”的理解是：**让 AI 学我的写法，而不是让我被 AI 的腔调带跑。。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37Cuf3ibNeP4zPpSDHG7icGSTEIoeUIY7p5NFAgXPPcS8GBhwPJL1mT2eUwcgdANC5F7UpGXp4lWHk1Q/640?wx_fmt=jpeg&from=appmsg)

关于GetDraft工具的具体介绍可以参考这篇文章：[GetDraft上线：给你搭一个从复刻文风到审稿的AI写作天团](https://mp.weixin.qq.com/s?__biz=MjM5NjQyMjE1NA==&mid=2650742961&idx=1&sn=b12b60e6fd603cbfaff1161b80de9e5c&scene=21#wechat_redirect)

这里面还有一个好玩的点就是你可以让它提取任何一位你欣赏的作家的风格,然后给它一个话题,然后就可以按照该作家的风格表达出来。所以AI时代能动嘴的尽量不动手,真的不是一句空话。

这一步的意义是：当你系列化写作时，读者记住的不是“知识点”，而是你的“叙事口味”。风格稳定，系列才会形成品牌。

  

05 边界：写行业内容，必须学会“不惹事”的自我保护

素材与表达解决之后，写行业内容还必须处理一个现实问题：**边界**。  
我给自己定的第一条底线叫“不惹事”。

这是我在得到线下《[做课的方法](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247485103&idx=1&sn=47c6155f263c4228ff687cec66c2830a&scene=21#wechat_redirect)》中学到的。作为行业的从业者,我们写行业内部的现象、问题、知识、方法的时候,往往面临这样痛苦的选择,那就是讲得太细,容易触碰商业机密与责任边界；讲得太浅容易让读者觉得没有价值。

我的做法是"上提一档"或"退后一步":

*   我不讲技术开发的具体方法,而讲这个事情背后的技术逻辑
    
*   我不讲某个企业具体做法的对错,而是讲在宏观博弈的大框架下这种做法产生的后果和对未来趋势的影响
    

举个具体例子:

写某个企业的技术路线时,我不会写到可复现的具体步骤、参数或“细到能照做”的构建细节，而只写到策略层：削弱竞争通路、强化关键节点、优化辅因子平衡、提高碳流分配效率等——讲的是**技术逻辑**。

写某个企业的战略决策时,我不会对某个企业下“对/错”的结论，而是讨论在宏观博弈框架下，它可能带来的短期收益与长期约束——讲的是**趋势与后果**。

这样尽可能把一些责任提前规避掉。当然,毕竟要有所取舍,所以在我的《氨基酸进化》的文章中,很多细颗粒度数据我会做区间化或模糊化处理，对企业与个人的评价也会用更审慎的表述——这是一种必要的自我保护。

总之,我在之前的文章中讲过,要做到叫好、叫座、不惹事。之前对"不惹事"还没有体感,但是随着影响力提高，边界意识会从“可选项”变成“必修课”。不惹事，才是账号能长期存在的底层条件。

  

06 争议:AI写的算不算原创?

第二个绕不过去的问题是：AI 辅助写作算不算原创？

这是大家一直纠结的问题。我理解有些读者对 AI 辅助写作会有顾虑：担心内容空泛、担心缺少责任主体、担心事实不可追溯。

但我对“原创”的理解不是有没有AI参与，而是**主线选择、证据取舍、行业判断、叙事结构与最终表述**是否由作者承担责任。

AI 确实能把散落在知识海洋里的信息连接起来，但真正产生价值的，是作者用自己的问题意识与行业经验，把这些关联“打捞”成可行动的判断。

语言模型放在那里不产生价值；它必须被一个作者使用，才会变成作品。

就像钢琴放在那里不会自己弹出《月光奏鸣曲》,AI模型放在那里也不会自己写出《氨基酸进化》。钢琴需要演奏家,AI需要有专业判断力的创作者。

我更愿意把 AI 看成“加速器”：它加速信息整理与表达打磨，但**事实可追溯、判断由我负责、边界由我守住**。  

所以我的结论是：**AI 参与写作并不自动否定原创**。关键在于：作者是否对关键结论负责、是否能给出可追溯的依据、是否形成了稳定的结构与表达风格。  

  

结语:

以上就是《氨基酸进化》系列从“起点—策划—调研—转化—红线”到最终成文的一次复盘。我希望喜欢这个系列的读者，能看见它背后的方法与取舍。

最后作为一个工科男，我会把这篇手记总结成一条可复现的闭环SOP：

*   **选题一句话**：你要回答谁的什么问题？
    
*   **双模型深研**：同提示词交叉验证，先获取尽可能多的材料信息。
    
*   **人工校准**：指出脱节点，让 AI 补充调研、调整方向。
    
*   **公众号转化**：把“是什么”重写成“为什么 + 场景化问题”。
    
*   **风格统一 + 边界控制**：用风格提取工具统一语气；同时守住“不惹事”的红线。
    

我一直更愿意把方法公开出来。因为在 AI 时代，每个人都有能力更高效地表达自己认可的东西——而真正拉开差距的，是你的问题意识、判断力与长期主义的输出习惯。

如果这种表达能对行业、对读者有一定的价值,我就已经心满意足了。

这篇文章,也是我用AI协作完成的。如果你读到这里,觉得有所收获,那就是对"人+AI协作"最好的证明。在未来的创作中,我会继续探索这种协作的边界。

路上见。

  

往期推荐:

*   《[蛋氨酸——生物发酵攻打的"最后堡垒"](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247485730&idx=1&sn=b06565b4206528456b141616a075d7c7&scene=21#wechat_redirect)》
    
*   《[谷氨酸:味精之外的生命与工业双枢纽](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247485574&idx=1&sn=b9fdcf1d0b70b6082da6e8aaea65aab4&scene=21#wechat_redirect)》
    
*   《[赖氨酸的'诺曼底登陆':合成生物学如何改写百年战事](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247485644&idx=1&sn=4a4dd964f759800efcf89ae2c3a5afc5&scene=21#wechat_redirect)》
    
*   《[苏氨酸：一场原子经济性的“闪电战”](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247486366&idx=1&sn=eb9f2fba9efda8a3ad541e83ed71c91e&scene=21#wechat_redirect)》
    
*   《[缬氨酸(5/5) | 反倾销、专利战、去风险：谁在阻击中国缬氨酸？](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247486990&idx=1&sn=a819e7f2853cd24967d8e3725da9fce3&scene=21#wechat_redirect)》
    
*   《[内容创作为什么要“不惹事”？如何避免“踩坑”？](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247485223&idx=1&sn=0abb3ba597ddd130f3d62dd9ff3a6078&scene=21#wechat_redirect)》
    
*   《[把你工作中的所有事都用AI先做一遍——AI的最高水平，理应成为你的最低水平](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247484202&idx=1&sn=40ce54be9ae84c24fa0b5e1277ab2470&scene=21#wechat_redirect)》
    

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言