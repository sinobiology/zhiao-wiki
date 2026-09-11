     公众号配图是怎么做的？我的 ChatGPT Image2.0 实操教程 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

公众号配图是怎么做的？我的 ChatGPT Image2.0 实操教程
===================================

原创 知奥zhao 知奥ZHAO 2026-06-16 23:43 宁夏

> 原文地址: [https://mp.weixin.qq.com/s/pep8ulkUlBBGPLavgjwczg](https://mp.weixin.qq.com/s/pep8ulkUlBBGPLavgjwczg)

文/知奥

最近有人在后台私信问我：文章里的配图是怎么做的？

这个问题其实我以前零散写过，但没有专门写成一篇完整教程。

比如在《[生物绘图对决：我用7道专业考题，实测了爆火的Image 2.0与老将Nano Banana Pro](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488127&idx=1&sn=628175ab5ae085ebcc0095f041b9d88d&scene=21#wechat_redirect)》里，我测试过 Image 2.0 在生物制造、工程制图、工艺流程图上的表现。当时的结论是：**GPT Image 2.0 在工程制图、科学图表、工艺流程图等结构化任务上，已经非常适合做专业内容配图。**

后来在《[用GPT Image2.0+Seedance2.0，满足孩子篮球明星梦](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488305&idx=1&sn=29e0442f8ef257c21ab6014d9b1621c9&scene=21#wechat_redirect)》里，我又写过另一种玩法：先用 GPT Image2.0 生成完整分镜，再用 Seedance 2.0 把静态图做成短片。

但如果你问的是：**一篇公众号文章里的封面图、正文图、解释图，到底怎么从0到1做出来？**

那这篇文章就是完整回答。

先说结论：我现在做公众号配图，主要用的是 ChatGPT 的 Image2.0 模型。更准确地说，它在 ChatGPT 里叫 **ChatGPT Images 2.0**。OpenAI 官方帮助文档里说，ChatGPT Images 可以直接在对话中创建和编辑图片，也可以上传已有图片后用自然语言描述修改；它还支持生成不同宽高比的图片。

2026年4月21日的 ChatGPT 发布说明中，也明确提到 ChatGPT Images 2.0 是 ChatGPT 里的新图像生成模型。如果是通过 API 调用，OpenAI 开发者文档里当前写的是 \`gpt-image-2\`；本文主要讲普通用户在 ChatGPT 页面里怎么做公众号配图。

* * *

一、先补一个最基础的问题：怎么进入 ChatGPT
-------------------------

有些朋友问“公众号配图是怎么做的”，其实并不是不会用，而是第一步就卡住了：在国内环境下，可能连 ChatGPT 的网站都打不开，或者打开以后无法正常注册、登录。

先说官方入口。

ChatGPT 的官网是：

> https://chatgpt.com

如果已经有账号，可以直接进入：

> https://chatgpt.com/auth/login

正常情况下，打开网页以后，点击 Log in 或登录，输入邮箱、手机号，或者选择 Google、Microsoft、Apple 等方式登录。登录以后，在对话框里输入问题就可以使用。

如果要用我这篇文章里说的配图功能，流程也很简单：登录 ChatGPT 后，新建一个对话，把文章草稿粘贴进去，让它先帮你审核文章；文章定稿以后，再让它给出配图建议；建议确认后，直接让它生成图片。

不过这里必须说清楚一点：ChatGPT 并不是在所有国家和地区都能正常使用。OpenAI 官方帮助中心有一个支持国家和地区列表，也明确说明，如果所在地区不受支持，可能会遇到无法注册、无法登录、无法访问服务等问题。

所以如果你在国内打不开官网，或者注册登录时提示地区不支持，这不是你操作错了，而是访问环境和服务支持范围的问题。我的建议是：只使用官方入口，不要随便相信所谓“国内镜像站”“代充账号”“共享账号”，尤其不要在陌生网站输入自己的邮箱、密码和支付信息。

能正常进入 ChatGPT 以后，后面的步骤其实就很简单了。

但真到我自己使用的时候，并没有那么复杂。

我很少单独去研究提示词，也不会先设计一大套参数。我的方法更像是把 ChatGPT 当成一个长期合作的编辑：先让它读文章、审文章、理解文章，等文章定稿以后，再让它顺手给出配图建议。建议没问题，就直接让它生成一组图。

所以这篇文章不是“提示词教程”，而是我真实使用流程的复盘。

* * *

二、先把文章草稿交给 ChatGPT 审核
---------------------

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a3jlfa2zsXLdTHSQEyiaXyqgWnpCjicZ565XjTUI1XnIH6Cba5aBSoBY1Nf2gqic0PkavgUn2yRiapCTgKUEjXuAiaJUFIyTHhopC3vKaIdiclXgY/640?from=appmsg)

我的第一步通常不是做图，而是写文章。

文章写完以后，我会把草稿直接粘贴给 ChatGPT，让它先帮我审核。

这个审核不是简单改错别字，而是让它从读者角度帮我看几件事：

1\. 文章逻辑有没有断裂。

2\. 有哪些地方表达不够清楚。

3\. 哪些段落太啰嗦。

4\. 标题和开头有没有吸引力。

5\. 专业表述有没有明显问题。

这一步其实已经为后面的配图打基础了。

因为 ChatGPT 在审核文章的过程中，已经读过全文，知道文章的主题、结构、重点、情绪和读者对象。它不是在完全不了解文章的情况下凭空画图，而是在已经理解文章的基础上给出配图方案。

这就是我觉得它好用的地方。

* * *

三、文章先定稿，再考虑配图
-------------

我一般不会在文章还没写完的时候就急着做图。

因为文章还在改，逻辑还在变，配图也很容易跟着变。

所以我的顺序通常是：

草稿 → ChatGPT 审核 → 自己修改 → 基本定稿 → 再做配图。

等文章定稿以后，再让 ChatGPT 看全文，它给出的配图建议就会更稳定。

这个时候我通常会直接说：

> 这篇文章已经基本定稿了，请根据文章内容给出公众号配图建议，包括封面图和正文配图。

有时候我甚至不会写这么完整，只是说：

> 给这篇文章做一组适合公众号的配图建议。

因为前面它已经读过文章、审过文章，对上下文是有记忆的。

* * *

四、先看配图建议，不急着生成
--------------

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXISYGNnpOrBJpEsKank8Wdw61LqGt8iciaaOzKIkQHKibcZiaFictsic30XibLt2aTj7ibcR1UXthOPbAXKqmX87Yy7iaZSR6tiaqSatLIkw/640?from=appmsg)

ChatGPT 一般会先给出一组配图方案。

比如：

1\. 封面图：用什么主题，表达什么情绪。

2\. 正文第一张图：放在开头，概括全文。

3\. 正文第二张图：解释核心概念。

4\. 正文第三张图：展示流程、结构或对比关系。

5\. 结尾图：强化文章最后的结论。

这一步我会先看建议是否合适。

如果建议偏了，我就直接告诉它哪里不对。比如：

> 第二张图太概念化了，我希望更像信息图，不要做成氛围图。

或者：

> 这篇文章偏专业，不要生成太科幻的图，尽量做成清晰的中文解释图。

或者：

> 封面可以有冲击力，但正文图要以解释清楚为主。

这一步很重要，但它并不复杂。

本质上就是：先让它说说准备怎么画，我觉得方向对了，再让它动手。

* * *

五、建议没问题，就直接生成一组图
----------------

配图建议确认以后，我一般会直接让它生成。

通常就是一句话：

> 这个配图方案可以，请直接生成这一组图片。

然后 ChatGPT 就会按刚才的建议生成一组图。

如果是封面，我会提醒它适合公众号封面；如果是正文图，我会提醒它适合手机端阅读。但很多时候，前面的配图建议里已经包含这些要求了，不需要再单独写一堆提示词。

这也是我现在使用 Image2.0 最明显的感受：

**以前做图像生成，像是在和一个只会画图的软件沟通；现在更像是在和一个读过文章的编辑沟通。**

它先理解文章，再提出配图建议，最后把建议变成图片。

所以真正的关键不是提示词，而是上下文。

* * *

六、生成以后，我只做三件事
-------------

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXImUqKic0HZadIOx9FxPF8RQiaehEcicJZmLWwtlcEzlljVBIFCgYSZNNAiaMSJEgLcjjicTzjteBHK98ryHOyvic7fjSECtgR8icA7Ws/640?from=appmsg)

图片出来以后，我一般只做三件事。

第一，看它是否符合文章。

有些图很好看，但和文章重点不一致，这种我不会用。

第二，看中文字是否清楚。

公众号是手机端阅读，图里的字如果太小、太密、太花哨，实际效果就不好。

第三，看专业内容是否有硬伤。

尤其是我写氨基酸、发酵、生物制造、产业链这些内容时，图里如果出现化学结构、代谢通路、工艺流程，就不能只看美观，还要看是否靠谱。

如果我不能确认某个结构是否准确，我宁愿让它画成抽象示意，也不让它画一个看起来很专业但实际错误的东西。

另外，OpenAI 现在也在生成图片里加入来源标识信号。官方帮助文档说，ChatGPT、Codex 和 API 生成的图片会包含 C2PA 元数据和 SynthID 水印，用来帮助判断图片是否可能来自 OpenAI 工具。不过这只能说明来源信号，不代表图片内容一定准确，也不代表图片未经修改。

* * *

七、我为什么不太强调提示词
-------------

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXIJf4DlaXJTPyj94lWhlVJp7vq09YIIboyHwWlZzdMmxEc986Ps1s0j5MktPZhpftMak5eQKSZd4Ohc5hupRHwIa928GcCzd5M/640?from=appmsg)

很多教程会把AI绘图讲成提示词工程：光线、镜头、构图、风格、材质、比例，列一大堆。

这些当然有用。

但对我来说，公众号配图的核心不是把某一句提示词写得多漂亮，而是让模型真正理解文章。

如果它没有读过文章，即使提示词写得再复杂，也很容易生成一张“好看但无关”的图。

如果它已经完整读过文章，参与过文章审核，知道这篇文章的主题、逻辑、重点和语气，那么你只要说“请给这篇文章配图”，它往往就能给出还不错的方案。

所以我的真实经验是：

**不要把配图当成一个孤立任务，而要把它放进写作流程里。**

从草稿审核开始，ChatGPT 就已经在理解文章；到定稿以后，让它给配图建议，只是顺着这条上下文继续往下走。

这比单独写提示词省事，也更符合我现在的工作习惯。

* * *

八、一个真实流程
--------

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXK9HhORCT83XO7vMLh4EXB52wrR6tGYtIbfianx3z3TsT7NYCqF83yMoA9kLxnKOiac1I2CnlcfIDk8oInwUwiaZPB0WmicRfqAEicY/640?from=appmsg)

如果用最简单的话概括，我现在做公众号配图就是五步：

1\. 把文章草稿粘贴给 ChatGPT。

2\. 让它审核文章，提出修改建议。

3\. 根据建议把文章改到基本定稿。

4\. 让它根据定稿文章提出配图建议。

5\. 配图建议没问题后，让它直接生成一组图。

整个过程没有什么神秘的提示词。

如果非要说“技巧”，就是两点：

第一，不要一上来就让它画图，要先让它读懂文章。

第二，不要把第一版图直接当最终结果，要自己判断是否符合文章、是否适合手机端阅读、是否存在专业错误。

* * *

九、我的真实心得
--------

Image2.0 最强的地方，不是“画得更漂亮”，而是它可以在理解文章以后，把文章里的概念、结构和情绪变成图片。

这对公众号作者非常重要。

因为公众号文章最缺的从来不是装饰图，而是把复杂内容讲清楚的图。

过去我们写专业文章，经常会遇到一个尴尬：文字写了很多，但读者还是很难在脑子里形成结构。

现在，AI图像模型的价值就在这里。

它可以把一段文字变成图，把一个概念变成结构，把一个流程变成路径，把一个抽象判断变成读者能看见的东西。

当然，它不是万能的。

它会犯错，会自信，会把不存在的结构画得像真的一样。

所以我的态度一直是：**AI负责把想法快速推到现实里，人负责判断什么是对的。**

这也是我现在做公众号配图的核心方法：

先让它读文章，再让它审文章；文章定稿以后，再让它提配图建议；建议方向没问题，再让它生成一组图；最后由我来挑选、校对和决定用不用。

如果只记住一句话，就是：

**公众号配图不是单独写提示词，而是让AI沿着文章上下文继续工作。**

这篇教程写完，以后再有人问我“你的公众号配图怎么做的”，我就可以直接把这篇发给他了。

* * *

相关阅读
----

1. [生物绘图对决：我用7道专业考题，实测了爆火的Image 2.0与老将Nano Banana Pro](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488127&idx=1&sn=628175ab5ae085ebcc0095f041b9d88d&scene=21#wechat_redirect)

2. [用GPT Image2.0+Seedance2.0，满足孩子篮球明星梦](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488305&idx=1&sn=29e0442f8ef257c21ab6014d9b1621c9&scene=21#wechat_redirect)

3、[AI炒股靠谱吗？我让12个AI真实跑了一遍](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488396&idx=1&sn=0c039602840420ae6d3c043c8b434bfd&scene=21#wechat_redirect)

4、[日更235天不如AI编程一天？| 不懂代码，24小时造出自己的数字大脑](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488213&idx=1&sn=f195d4aeddbd8dc9207239975a169406&scene=21#wechat_redirect)

5、[从“先打基础”到“先解决问题”：AI时代的学习革命](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488141&idx=1&sn=64b86bda2a8f07f8343fcda42d9b08c0&scene=21#wechat_redirect)

6、[AI才是完美主义者和拖延症的天然解药](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488015&idx=1&sn=9c4dc23d1853c7277dfe58b338f910e5&scene=21#wechat_redirect)

  

---

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言