     罗胖点名的那篇文章，我用 Gemini + NotebookLM 把它“吃”透了 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

罗胖点名的那篇文章，我用 Gemini + NotebookLM 把它“吃”透了
========================================

原创 知奥zhao 知奥ZHAO 2026-01-03 20:08

> 原文地址: [https://mp.weixin.qq.com/s/eUx6rTYUEUCd4kNCiPmMWA](https://mp.weixin.qq.com/s/eUx6rTYUEUCd4kNCiPmMWA)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9FjMWpD9hN0vRNP72I2njHAO375Zod3vxzY7wVhZO1KiaKxTNGo7icNFQ/640?wx_fmt=jpeg&from=appmsg)

**罗胖点名的那篇文章，我用 Gemini + NotebookLM 把它“吃”透了**

  

文/知奥

  

**0****1**

**扎心的真相：你是在驱动 AI，还是被 AI 替代？**

最近我的公众号后台有读者问我，文章的配图是用什么软件做的，我于是回答用Gemini的nano Banana。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9KetCPGTtkP3aficWLTp3bljFqxNOzz7m2x9crZSG2IzX35jbQvZg2IQ/640?wx_fmt=jpeg&from=appmsg)

其实我觉得这个事情并没有讲透，本来我的公众号也在做AI领域的科普，例如：[极速调研秘籍：AI如何帮我1天完成新品战略规划？](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247484116&idx=1&sn=5580c9910b405b7a00543aeed3fc1300&scene=21#wechat_redirect)[](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247484083&idx=1&sn=00ceef5df1adfc1d9eb0b270076c15e1&scene=21#wechat_redirect)我一直认为AI是一个[研究平权工具](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247485688&idx=1&sn=f3a3f9558bc90c158fbe465645f182ee&scene=21#wechat_redirect)，所以今天我准备把自己用AI处理具体事情的经历写成教程。

在刚刚结束的 2026 罗胖《时间的朋友》跨年演讲中，他特别提到了《预测之书》里和菜头的一篇文章，叮嘱大家一定要优先阅读。我还没等实体书到手，和菜头老师就把这篇《[赛博袁天罡发布2026新预言](https://mp.weixin.qq.com/s?__biz=MjM5MjAzODU2MA==&mid=2652806638&idx=1&sn=666d2c27adf40c41042501426be2a822&scene=21#wechat_redirect)》**发到了他的公众号“槽边往事”里。**

看完之后，我深感震撼。文章的核心观点其实很扎心：

*   **人与人的竞争本质未变：** AI 时代并没有改变人类社会“人与人竞争”的古老命题 。AI 的效能取决于人类给出的指令和提问的质量，竞争的关键在于谁能问出正确的问题并下达正确的指令。
    
*   **“人肉 AI”的黄昏：** 过去组织中的大多数人充当的是“执行者”角色，按照流程行事，而这类工作将被 AI 高效替代。
    
*   **向“决策者”转型：** 个人必须从“执行者”转变为“决策者”，学会在宏观上认识事物的全景与运行规律，而不再是死记硬背知识点。
    
*   **未来的五种人：** 社会需要能下达指令的人、能问对问题的人、发现错误的“看门人”、现实中的执行者，以及最关键的——能真正承担责任的人。
    

我强烈建议大家阅读原文，但在碎片化时代，很多人扫两眼就收藏吃灰了。为了不让好思想被埋没，也为了回应读者的好奇，今天我拿这篇文章做范例，手把手教大家如何利用 **Gemini + NotebookLM**，把干货文章拆解、转化成你自己能吸收、能传播的各种形式。

**0****2**

**我的分享哲学：为什么我不再相信“信息差”？**

在进入教程前，我想多说两句。

我不是一个喜欢藏着掖着的人。无论是 AI 的使用、投资的思考，还是读书的洞见，我一直深深地认为，这个时代靠“信息差（我知道，你不知道的）”来保持优势是不现实的。

恰恰相反，我认为**真诚地分享有价值的内容，反而是最具有性价比的一种成长形式，因为“教是最好的学”。** 

所以今天，我把前期使用 AI 的心得体会和具体操作步骤全部分享出来。

**0****3**

**实战教程：手把手教你“打捞”知识海洋**

第一步：用 NotebookLM 建立“不跑偏”的知识库

AI 最大的问题是容易“一本正经地胡说八道”。为了让 AI 精准还原思想，我们要先用 **NotebookLM** 建立封闭的“知识库”。

1.  **打开网址：** https://notebooklm.google.com
    
2.  **上传原文：** 将文章内容复制粘贴进去。这里要注意， NotebookLM无法读取微信公众号文章的分享链接，核心原因是腾讯的限制和地区网络限制（你懂的）。
    
3.  **意义：** 这样 AI 的所有输出都将基于你提供的“资料库”，而不是在互联网上乱抓。
    
    ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9zXibzDycNK5E16Gu0w8Iu0fH1WRzC7yY5hjTNcn0aaw9sB6X51Kr7Yg/640?wx_fmt=jpeg&from=appmsg)
    

第二步：由点及面，多维度产出

有了精准的输入，接下来就是“变戏法”的时间。可以看到把文章复制输入后就建立了一个“笔记本”，目前这个笔记本里只有一篇和菜头的文章，如果后续想用和菜头的文章建立一个“知识库”，就可以不断输入他的其他文章，NotebookLM可以基于你建立的知识库进行精准输出。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9Pa472gsCibAGBKsbkrUaJyqiaREBMGfBqh7KJVPrFVTnFhoKk21tFR1g/640?wx_fmt=jpeg&from=appmsg)

在上图界面的右侧可以看到，基于这篇文章可以输出不同的学习方式，音频、视频、思维导图、信息图、演示文稿等等。可以满足不同学习爱好者的学习方式，使用也很方便，那就是想生成什么就点击对应的按钮即可，有些选项可以设置偏好，但我一般都是直接点击，效果已经足够好了。

  

**1、思维导图：** 

自动生成逻辑框架，一键导出 PNG，快速掌握全文结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9fShUpM2nkFHtC5fia9uHG9rIuVORCFAHZdtvNsH67IQmeSwwaxCoZqg/640?wx_fmt=png&from=appmsg)

**2、信息图表（读者问的配图就在这里）：** 

这是最令我惊喜的功能。AI工具会自动抓取文章结构，自动构图生成逻辑清晰的信息图，也就是相当于一张图就把文章的主要内容讲清楚了，特别适合快速掌握全文结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9xeIian7CEJRkcg02zdqbkD0sQyGp72uUGaeTvoyPl8GGLHKXSGDmdibg/640?wx_fmt=png&from=appmsg)

_实际上现在好多公众号开始用这种方式讲解化工原理、初中物理等严肃知识，基本上一键就能生成AI漫画，让很多晦涩难懂的知识瞬间亲民起来。用来把最新的英文文献进行漫画式讲解也是不错的办法。例如下面这几个例子：_

_例子1：_ 我曾用它将复杂的论文《《Biosynthesis of artificial starch and microbial protein from agricultural residue（从农业残留物生物合成人造淀粉）》生成信息图，瞬间让晦涩的知识亲民起来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9NnO2FyronPz0zukMI7yRZcTOd9o3kE5sKngWZjqCDFUHlBXB1Kb1Ng/640?wx_fmt=png&from=appmsg)

*   例子2：合成氨工艺技术详解
    
    ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9Dhc1RlQiaHvWUdDjHbsGYiaqW810ibZTqvYj0cNLia8BOtwvsC0yN4r7Mw/640?wx_fmt=jpeg&from=appmsg)
    
    如果说最有用的功能，我觉得信息图简直是“降维打击”一般的存在。有了这个功能，给文章配图就是最简单的应用了。实际上意味着所有的知识都可以重做一遍，这个工具是所有做知识培训的人的“外挂”。
    
    3、音频与视频：我都是直接点击一键生成，没有用提示词。
    

*   **视频**：点击一键生成。生成了8分钟的视频讲解，我看了一下绝对是高水准。
    
      
    
*   音频：一键生成了16分钟音频博客，试听了一下男女两个人对谈，非常自然，而且都是口语化表达，逻辑清晰，很好理解。非常适合上下班通勤的时候开车听。
    
      
    

4、报告

在右侧的选项卡中，还可以生成“报告”，点开“报告”这个选项，里面有很多种报告样式：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9Z0Z3p3jib3V0V3Zg2yFkjsJ0Ffr6z9wJsfsM9BUbfNVjgwgaosbCTJw/640?wx_fmt=jpeg&from=appmsg)

  

我直接点击了“博文”，生成的就是一篇风格类似于公众号的文章。看下图，是不是你想写自己的公众号文章也简单多了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_14@2x.png)。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9Jtrwn8ia2oQfdq3xuCqV9taxmiacE5utxDz7CUE2nrJZmqdj8HncY1KA/640?wx_fmt=jpeg&from=appmsg)

第三步：Gemini 统领全局，完成“个性化输出”

最后，我把以上所有拆解出的精华交给 **Gemini** 进行最后的文案润色。目前网页版的Gemini已经支持直接导入NotebookLM的笔记本知识库内容了。网页版可以登录网址：https://gemini.google.com/app，用iPhone的话也可以下载手机版，不过需要美区的ID，手机版功能稍弱，不支持导入NotebookLM。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ogQWzRFB37AWHB2zCMt3PsRaanSicviby9UBhJ9dWeq7AakYfu3GeooSWbxujhjOneXU3dm6q7liboibJj20IFMwkw/640?wx_fmt=jpeg&from=appmsg)

这就是你现在看到的这篇文章——它不是 AI 盲目生成的，而是我作为“决策者”，下达了明确指令后由 AI 辅助完成的深度内化。

Gemini或ChatGPT等AI工具都会主动调用跨对话记住的显式信息（如你明确要求它记住的偏好、个人信息）和从对话历史中提炼的隐式模式（如你的写作风格、常讨论的主题），来定制个性化的回答，所以这些工具给人的感觉是，越用越懂你。

最后这篇文章还需要一张封面图，于是我给Gemini说：“给这篇文章配封面图，2.35:1”，就有了文章开头的封面图。到这里，一篇完整的文章就输出了。

  

**0****4**

**结语：思考，才是你唯一的护城河**

我知道，把这些工具、路径甚至具体的 Gemini的详细使用方法（如 Nano Banana）摊开来讲，依然会有人对“人+AI 辅助”的写作嗤之以鼻：“这不就是靠工具吗？”

但我更想请你思考：工具是平权的。面对同样的 AI，为什么有人能“打捞”出深耕行业的真知灼见，而有人却只能得到一段平庸的“片儿汤话” ？

和菜头在文中说得极透：AI 的无所不能需要一个前提，那就是必须有一个人给出正确的指令，问出那个关键的问题 。如果你心中没有预设的“好图”，脑中没有对底层运行规律的深潜，你给出的指示便毫无焦点。

竞争的本质从未改变，改变的是人类与机器结合后的新能力 。就像汽车取代马车时，威胁马车夫利益的从来不是汽车，而是学会了开车的司机 。

在接下来的 1500 天里，我们每个人都公平地拥有这个缓冲期 。你可以选择继续做一个只满足于流程、在现实中“移动箱子”的执行者 。

但我更希望我的读者，能利用这三五年的“心理缓冲期”，学会驾驭这些工具，从只会执行指令的“人肉 AI”，进化成能够定义问题的“决策者”。

**在这个时代，工具本身往往不是壁垒，“如何用好工具去处理复杂信息”才是。** 

思考，才是你唯一的护城河。

* * *

### 💡 补充说明：关于如何开启你的 AI 之旅

如果看到这里你还有疑问：在中国大陆究竟如何才能用上 Gemini？

由于网络环境和合规性要求，具体的“技术细节”不便在文章中公开讲解。简单来说，你需要完成以下三个步骤：

1.  **网络环境准备：** 确保拥有稳定的网络接入工具。
    
2.  **账号准备：** 注册一个谷歌邮箱（Gmail）账号。
    
3.  **正式开启：** 使用该账号登录 Gemini 官网。
    

**“工欲善其事，必先利其器。”** 具体的搜索关键词我已经给到大家了，建议大家发挥“决策者”的主动性自行探索方法。如果确实遇到阻碍，欢迎关注我并在后台**私信**，我会单独为你解答。

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言