     我不会写代码，但我用AI做出了3个数学动画 | 一次「养马」的完整记录 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

我不会写代码，但我用AI做出了3个数学动画 | 一次「养马」的完整记录
===================================

原创 知奥zhao 知奥ZHAO 2026-05-06 23:34

> 原文地址: [https://mp.weixin.qq.com/s/8tpX5ymzEt-dRwrM99sXDA](https://mp.weixin.qq.com/s/8tpX5ymzEt-dRwrM99sXDA)

![](https://mmbiz.qpic.cn/mmbiz_png/a3jlfa2zsXJhNia0aLmU0EIqOfib3kmGSsiclaOsVNwNrPeicnRHwhicOGMncLTjwkCQCG2PmaqgtSxxs5ibRSD43NiaWwF1niclwCyFmqfZGxCDfUc/640?wx_fmt=png&from=appmsg)

  

文/知奥

  

* * *

如果你最近关注 AI 圈，可能已经注意到一个有趣的转向。圈子里养什么的都有，但从去年年底开始，越来越多人从「养龙虾」转向了「养马」。

「龙虾」是 OpenClaw——2025 年 GitHub 上最火的 AI Agent 项目之一，309k Stars，执行力极强。你给它明确的指令，它干活非常利索，生态里也有很多现成的技能可以调用。但它有一个致命的短板：金鱼记忆。你上周教它怎么处理报表，这周再让它做，你得从头教一遍。

「马」是 Hermes（爱马仕）——OpenClaw 的全面架构升级版。它最核心的差异化优势，就一个词：自进化。

怎么个自进化法？它不是干完活就忘了。每次任务完成后，它会自动分析：这次完成得怎么样？踩了什么坑？怎么修好的？然后把经验写成一份专属的技能文件存起来。下次遇到类似任务，它直接调用经验——不仅准确率更高，连 Token 消耗都大幅降低。

换句话说，OpenClaw 是执行力超强的管家，但每次都要从头教。Hermes 是会动脑子的学徒——越用越懂你，越用越顺手。

五一假期最后一天，我也赶时髦跟着课程学习Hermes 的本地部署和实操案例：自动剪视频、做数学动画、做网站……

做数学动画现在最好的技能就是Manim。那条 3Blue1Brown 的视频我看了两遍——不是因为内容难懂，是因为我清楚地知道：这种视频，我一行代码都写不出来。

但现在不一样了。现在我有一匹「马」。

* * *

装 Hermes 的时候，客厅里儿子正在看电视。他今年上初二，物理刚开了个头，数学刚学了勾股定理。

装好 Manim 环境的那一刻，我脑子里冒出来的第一个念头不是「好，可以开始做视频了」，而是——「给儿子露一手」。

我走到客厅，问他：「你们物理最近学了什么？」他说浮力。我又问：「数学呢？」他说勾股定理。

好。选题有了。

接下来的大半天，我做了三个视频。安装环境花的时间最长——Python 版本不对、SSL 证书坏了、LaTeX 装不上、dvisvgm 要源码编译……一个坑接一个坑。但有意思的是，环境一旦跑通，后面的速度越来越快。阿基米德原理是第一个，磕磕绊绊；勾股定理是第二个，顺手多了；到 Transformer 架构，从说需求到出视频，不到十分钟。

这个阿基米德原理视频，虽然比较粗糙，但也算是一个小小的作品了，毕竟这是养马的第一个产出。

儿子看完说了一句话：「爸，这个比我们老师讲的清楚多了。」

那一刻我意识到，我做的这件事，不只是「用 AI 做了个视频」。我做的是：一个爸爸，用自己的方式，把课本上那些抽象概念，翻译成儿子能看见的东西。

而这件事，一个不会写代码的人，以前根本做不到。

* * *

01 从养龙虾到养马：记忆才是壁垒

先说一个细节，你可能就能理解 Hermes 和 OpenClaw 的本质区别。

装 Manim 环境的过程里，我们踩了五个坑。系统 Python 太旧、Homebrew 的 SSL 证书是坏的、LaTeX 安装包 404、dvisvgm 缺失要源码编译……整个过程持续了大概 20 分钟，Hermes 负责解决每一个报错，我只负责批准。

如果用的是 OpenClaw，这次装完就完了。下次换台机器，还是一模一样的五个坑，它一个都不记得。

但 Hermes 不一样。任务完成后，它把整个排障过程自动存档——每个坑是什么、怎么排查的、怎么解决的——写成了一份 macOS 配置指南。顺带把 skill 里的 setup 脚本也修了 bug。

这就是记忆系统的威力。Hermes 有三层记忆：短期记忆管当前对话，持久记忆管跨会话的事实（比如我的偏好是专业高效型沟通），Skill 级记忆管可复用的经验。

那五个坑的经验，现在就在 skill 里。下次任何人要在 macOS 上装 Manim，它直接读那份指南，不会再踩一遍。

OpenClaw 给你的是执行力，Hermes 给你的是积累。这是两种完全不同的东西。

* * *

02 我做了什么，AI 做了什么

装好环境，我开始做第一个视频——阿基米德原理。

整个流程是这个样子：

Plan 阶段。 Hermes 先出了一份分镜设计——五个场景，经典 3B1B 配色，叙事弧线是「悖论→排水→力平衡→浮或沉→Eureka!」。我看了一遍，说：把公式阶段加强。它改了。

Code 阶段。 Hermes 写出完整的 Python 脚本，每个场景一个独立的类。200 多行代码，三角形、正方形、箭头、公式、淡入淡出、位移变换。我的角色不是写代码——是判断。「这个场景节奏太慢」「那个箭头颜色不够突出」「旁白比画面长了两秒」。

渲染阶段。 95 秒，5 个场景，1920×1080，60 帧。中文旁白用 macOS 自带的语音合成，ffmpeg 精确对齐到帧。

第一个视频做好之后，我又做了两个：勾股定理和 Transformer 架构。三个项目，同一套流程：Plan → Code → Render → Stitch → Audio。

到第三个项目，从说需求到出视频，不到 10 分钟。不是我变快了，是我和 Hermes 之间形成了一套共同语言——它记住了我的审美偏好、配色习惯、叙事节奏。我不需要再解释什么叫分镜、什么叫调色板。

这就是「自进化」的实质——不是 Hermes 突然变聪明了，是它变得越来越适合我了。

* * *

03 协作的本质：不是 AI 帮你做，是你和 AI 一起做

做完阿基米德原理的视频，第一次播放的时候，我一直在想一个问题：这东西到底是我做的，还是 AI 做的？

后来想清楚了。如果 AI 独立做，它会交出一个技术上正确的视频——构图、色彩、节奏都 OK。但不会有我在 Plan 阶段提出的「悖论开场」——那是我觉得阿基米德最打动人的地方：二十万吨的钢船浮着，五克的石子却沉了。这个矛盾，比公式本身更值得被看见。

AI 给了执行，我给了判断。两样东西加起来，才是一个完整的作品。

这个过程里，角色分工很清楚：

\- 我做的是：描述想要什么、判断好不好、反馈怎么改

\- AI 做的是：设计方案、写代码、调试环境、渲染合成

这个分工的本质没有变——变的是另一端的响应速度和成本门槛。

以前，从「我有一个想法」到「我有一个视频」，中间隔着四道门槛：学会 Python、学会 Manim、学会 LaTeX、学会 ffmpeg。现在，这四道门槛 AI 帮你跨过去了。

剩下的那部分——你想要什么、你觉得好不好——从来都是人的事。

* * *

04 三个项目，同一套 Pipeline

勾股定理的叙事是：从几何直觉到公式抽象。

「所有直角三角形的边都遵循同一个关系——这不是需要背诵的公式，而是可以用眼睛看到的几何事实。」

这次用上了 LaTeX 公式渲染——a²+b²=c²，再落到具体数字：9+16=25。公式的质感立刻上了一个档次。

Transformer 架构的挑战最大。它不是几何概念，是抽象架构——自注意力、多头、编码器-解码器。Hermes 的解法是用 Neon Tech 配色让抽象结构变得可读：暗黑背景上，青色是注意力，品红是前馈网络，绿色是编码器，琥珀是解码器。

三个视频做下来，最深的感受不是 AI 有多能干，而是：

一旦你有了一个可复用的 Pipeline，创意的成本会降到让你不敢相信的程度。

而这套 Pipeline 本身，也被 Hermes 写成了 skill。下次要做新的动画——傅里叶变换、梯度下降、神经网络——它直接调用这套流程，不需要重新磨合。

这就是 Hermes 最让我信服的地方：它不是在替你干活，它是在和你一起，搭一套越用越顺手的系统。

* * *

05 给所有「不会写代码的人」

这篇文章不是教程。网上有更好的 Manim 教程。

这篇文章是一个记录：一个不会写代码的人，怎么用 AI 做出了三个数学动画。记录这个过程里，几个最关键的认知转变。

技术不是瓶颈。 以前我觉得「做视频」的瓶颈在技术——我不会写代码，所以我做不到。但真正的瓶颈从来都不是技术，而是你想做什么、你想怎么做、你判断好坏的标准是什么。技术是执行层的事，AI 可以负责。「想要什么」和「够不够好」，只有你能决定。

Plan 是协作的合同。 不要跳过 Plan 阶段直接让 AI 写代码。先写一份清晰的分镜设计——场景怎么排、配色用什么、每个画面想表达什么。这份 Plan 是你和 AI 之间的合同。合同越详细，返工越少。

选对人马很重要。 OpenClaw 能干活，但干完就忘。Hermes 能干活，而且越干越懂你。如果只是偶尔用 AI 做一件小事，选哪个都行。但如果你想持续和 AI 协作、积累经验、搭一套越用越顺手的系统——记忆才是壁垒。

可复用比一次做好更重要。 三个项目走下来，我发现最关键的事不是做出一个完美的视频，是建立一套可以反复使用的 Pipeline。Plan → Code → Render → Stitch → Audio——少了任何一个环节，下次还得重新摸索。

* * *

尾声

从看视频到出视频，我用了假期最后一天。

这不是在说 AI 多强大。这是在说：以前技术是瓶颈，现在想象力和判断力是瓶颈。

一旦你能把脑子里那个模糊的「想要这样的效果」，变成一份清晰的 Plan，你和一个会写代码的人之间，差距就只剩一个问题：

你想不想做。

那个问题的答案，在第一次看到成品视频的那一刻，已经很清楚了。

* * *

我的「马」现在养在本地终端里。每次完成一个新项目，它就自动存档一份经验、更新一份 skill、变得更适合我一点。它不是 OpenAI 的通用模型，它是我自己喂出来的、带着我的审美和判断习惯的专属助手。

这种感觉很难描述。但如果你也养过马，你懂我在说什么。

* * *

项目文件

三个 Manim 动画项目的源码、分镜设计和成品视频，已开源在本地目录中。如果你也养了一匹马，拿这些去喂它，看看它能帮你做出什么。

~/manim-projects/  
archimedes/    # 阿基米德原理：浮力 = 排开水的重量  
pythagorean/   # 勾股定理：a² + b² = c²  
transformer/   # Transformer 架构：自注意力 × 多头 × 编解码器

* * *

免责声明： 本文为个人实践经历分享，所有项目均来自作者亲身操作，基于【前哨AI小课】第五季 Tina 老师课程《Hermes本地部署：打造自进化的AI员工》（2026.05.03）所学方法。本文提及 Manim、3Blue1Brown、Hermes、OpenClaw 等工具和项目，仅基于个人使用经验，不构成商业推荐。本文独立撰写，作者与文中提及的任何工具、平台、课程均无商业利益关系（感谢 Tina 老师的课程启发，此处为致谢，非广告）。

* * *

往期推荐：

\- [《日更235天不如AI编程一天？| 不懂代码，24小时造出自己的数字大脑》](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488213&idx=1&sn=f195d4aeddbd8dc9207239975a169406&scene=21#wechat_redirect)

\- [《AI才是完美主义者和拖延症的天然解药》](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488015&idx=1&sn=9c4dc23d1853c7277dfe58b338f910e5&scene=21#wechat_redirect)

\- [《我不会写代码，但我做出了一个 App：一次对"自然语言编程"的祛魅》](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247487938&idx=1&sn=821245016d014c84d81bc99c0529f12b&scene=21#wechat_redirect)

\- [《AI最可怕的，不是快，而是开始像项目经理一样工作》](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247487813&idx=1&sn=28459ffd5ce16b0ef9e37fe8530b6331&scene=21#wechat_redirect)

\- [《从"先打基础"到"先解决问题"：AI时代的学习革命》](https://mp.weixin.qq.com/s?__biz=MzI2MDYyMzgwMw==&mid=2247488141&idx=1&sn=64b86bda2a8f07f8343fcda42d9b08c0&scene=21#wechat_redirect)

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言