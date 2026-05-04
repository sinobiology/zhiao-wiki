     从“会回答”到“会执行”：OpenClaw 到底是什么 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

从“会回答”到“会执行”：OpenClaw 到底是什么
===========================

原创 知奥zhao 知奥ZHAO 2026-03-09 21:18

> 原文地址: [https://mp.weixin.qq.com/s/efoQDWEXkuup4Si3EwqsPA](https://mp.weixin.qq.com/s/efoQDWEXkuup4Si3EwqsPA)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/a3jlfa2zsXK8mst25kFZuU5t4WiaQzKrg4RNt7rwQesFIWpCUwmkyhgicYUkGue70Szs8nKxKAtOoPZ5RWagdlE0AaDT3GFxH0yn4OKbPoLxs/640?wx_fmt=png&from=appmsg)

文/知奥

  

写在前面

3月6日，深圳腾讯大厦楼下，近千人排起长队——不是为了演唱会，不是为了限量款，而是为了免费安装一款AI软件。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a3jlfa2zsXLq6eYm6fSStFq06ia6icFEwtVSzMAibmuMQjVxdiaZia7HWE0u6mqYFicicRY3uzASnc2icicKl9A8ib5F8Y1pzKia2q2A9cficOCGBRCicIzM/640?wx_fmt=jpeg)

这款软件叫 OpenClaw，国内用户给它起了个接地气的外号：“小龙虾”。

在这之前，社交平台上已经炸开了锅。“OpenClaw上门安装调试”的帖子随处可见，上门服务标价400-1500元，远程安装也要300元起步，有从业者宣称短短数日靠安装调试赚了26万。中国工程院院士高文感叹：“现在大家急得不得了，生怕没有养上'龙虾'。”

与此同时，腾讯、字节、百度几乎同步下场——腾讯推出WorkBuddy和内测中的QClaw，打通微信QQ直接操控电脑；字节火山引擎上线ArkClaw，开箱即用的云端版本；百度智能云出了一键可视化部署，声称“零基础小白也能搞定”。这些大厂不是在做慈善，它们嗅到了真实的商业机会。

工业和信息化部的反应也很快——发出了安全预警，提示OpenClaw在默认或不当配置情况下存在较高安全风险，可能引发网络攻击和信息泄露。

三件事同时发生：普通人排队抢装、大厂疯狂跟进、监管部门发出预警。

这种阵势，上一次出现还是ChatGPT横空出世的时候。

但和当年一样，热浪之下，真正说清楚“它是什么、怎么运作、该不该用、怎么用才安全”的声音，少得可怜——多的是贩卖焦虑的推文和鼓励你赶紧上车的课程。

这篇文章，就是要把这些问题一次讲清楚。

  

先问你一个问题：

你有没有遇到过这样的情况——你让AI帮你把昨天的会议录音整理成报告发给领导，它噼里啪啦给了你一套详细操作步骤，然后你花了一个小时，照着步骤，自己一步步点击、粘贴、排版、发送？

AI说了很多，活还是你干的。

这不是AI不够聪明。这是它的工作方式决定的天花板。

绝大多数AI助手，包括ChatGPT、Kimi、文心一言，本质上都是“用嘴皮子工作”——它们通过特定的“对接接口”（技术术语叫API）与外部软件沟通，就像一个只会打电话的秘书：邮件系统给了电话号码，它能帮你发邮件；表格系统开了接口，它能帮你改数据——但如果某个软件没有提供这条“电话线”，它就束手无策。

而OpenClaw，走了一条完全不同的路。

  

01 | 核心突破：从“帮你出主意”到“帮你真的干”

OpenClaw的核心理念，可以用一句话说清楚：

它不只是回答你，而是常驻在你的设备上，拿到你电脑的“执行权限”，真的替你去做事。

具体怎么工作？

你在手机上发一条飞书消息：“帮我把今天的日历整理一下，发一份摘要到我邮箱。”

普通AI：回复一段建议，告诉你可以怎么整理，然后等你自己去操作。

OpenClaw：真的去读了你的日历，提炼出今天的安排，写了一封摘要邮件，发到了你的邮箱——全程不需要你动手。

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXLicv18faGAgiafT081U7pzBjEGtUvspYQm95yazoeFvSPL7fahe4vJ46O9YykP1XicdPewUgwsSiaB6KKvuiaOyINyGAzWF8bY7SicI/640?wx_fmt=jpeg&from=appmsg)

它实现这一切，靠的是两个关键设计：

第一，常驻在你的机器上，不是“聊完就走”。 OpenClaw是一个持续运行在你电脑上的程序，官方的定位是“运行在你自己设备上的个人AI助手”，强调“你的机器、你的数据、你的密钥”。它不是云端的一次性对话，而是始终在线的本地代理。

第二，拿到了“执行层”的真实权限。 它可以直接操作文件系统（读写文件）、控制浏览器（打开页面、点击、填表）、执行系统命令（shell命令）、收发消息（邮件、日历、WhatsApp、Telegram、飞书）。这些不是“模拟操作”，而是真实的系统级执行权限。

你通过手机上的聊天软件发指令，它在电脑上真的执行——这就是OpenClaw让人感到“像有个人在帮我盯着电脑”的底层原因。

  

02 | 为什么现在才出现？它会不会只是昙花一现？

听到“AI能帮你真的在电脑上干活”，很多人的第一反应是：这靠谱吗？不会是昙花一现的噱头吧？

先说“为什么以前没有”。

“让AI像助手一样持续帮你工作”这个念头，在AI领域存在了很久。不是没人想到，而是以前有一道绕不开的门槛：AI没有“手”。

普通AI生活在对话框里，说完就走，没有能力真正碰你的文件、你的浏览器、你的系统命令。就像一个聪明的顾问，能给你出主意，但没有办公室门禁卡，进不了任何地方实际操作。

这道门槛，最近两年被几件事同时打开了：大语言模型的推理和任务规划能力强到足以拆解复杂指令；浏览器自动化、文件系统访问、消息渠道桥接这些执行工具成熟到可以稳定调用；开发者社区开始把“给AI装执行权限”当成一个可以工程化落地的方向，而不只是概念。

OpenClaw做的事，是把这些拼在一起——消息渠道作为入口，AI作为大脑，本地工具包作为手，造出了一个可以持续运行、真实执行任务的本地代理。

再说“会不会昙花一现”。

OpenClaw开源之后，国内外大量开发者和公司开始在它的基础上构建产品——Kimi、猎豹、阿里通义各自做出了面向不同用户的版本。当这么多商业力量同时押注一件事，它就不太可能悄悄消失了。

更可能的走向是：它会越来越稳、越来越好用，门槛越来越低。

这里有一个值得多想一步的问题：大厂为什么抢得这么急？

因为谁控制了“执行层”，谁就控制了用户的电脑桌面。过去十年，流量入口是搜索框、是App、是微信公众号；下一个入口，可能就是“你在哪里发指令、让AI去帮你干活”的那个对话框。一个能真正执行任务的本地代理，商业价值比单纯做一个聊天网页高出几个数量级——这才是腾讯、字节、百度同步押注的真实逻辑。“对话框即入口”的时代，可能正在被“执行层即入口”取代。

  

03 | 开源生态：一套“发动机”，驱动了一批“汽车”

OpenClaw是一个开源项目——核心代码免费公开，任何人都可以拿来改造。

你可以把OpenClaw原版理解为一套裸奔的“发动机底盘”——核心能力（消息渠道桥接+本地执行+技能扩展）都在，但你得自己装壳子、调参数、学操作。各大公司看到了这个底盘，纷纷套上了不同的“车身”。

为什么会分化出这么多版本？背后的逻辑其实很简单：底盘一样，但各家想卖给的人不一样。 月之暗面手里有自家的大模型，它希望更多用户用上Kimi，所以做了云端版，让你不用折腾直接用；猎豹移动做安全工具出身，它的用户最在意数据不外泄，所以做了本地版；阿里通义的客户主要用钉钉、飞书，所以CoPaw原生接入了这套生态。不同的商业判断，造就了不同的产品形态。

目前市面上比较主流的几款产品：

Kimi Claw（月之暗面出品） 定位：省心派。部署在云端服务器上，你无需折腾任何配置，打开网页就能用。代价是你的操作数据和屏幕内容需要传到Kimi的服务器处理。

EasyClaw / 元气AI（猎豹移动出品） 定位：隐私派。做成了桌面软件，像装普通APP一样安装，强调所有操作在本地电脑完成，数据不上传云端。

CoPaw（阿里通义出品） 定位：国内生态派。原生适配钉钉、飞书等办公软件，对于主要使用国内工具链的用户，接入更顺畅。

MaxClaw（MiniMax出品） 定位：与Kimi Claw类似，也是云端托管服务，差异主要在于背后使用的大模型不同。

选哪个，取决于你最在意什么：怕麻烦→云端版；怕数据外泄→本地桌面版；主要用国内办公软件→CoPaw。

  

04 | 高权限的另一面：不得不正视的安全问题

前面说OpenClaw能“在你电脑上真实执行任务”——这句话有多强大，安全风险就有多真实。

它拿到的是系统级别的真实权限：它能读写你的任何文件、控制浏览器访问任意网站、执行系统命令、通过消息渠道收发内容。这不是ChatGPT那种“在对话框里回复几句”的权限，这更像是把你电脑的管理员钥匙交给了另一个“人”。

有一个数据可以让你感受到这件事的严肃程度：公开报道提到，2026 年 1 月底已有超过 2 万个 OpenClaw 实例直接暴露在公网上，任何人都可以访问，其中大量存在高危漏洞。这不是极端情况，这是大多数“随手部署”的用户的真实处境。

这背后，有三类风险值得了解：

风险一：配置不当，变成公开后门。许多用户部署时图省事，把服务直接暴露在公网，相当于把大门敞开着。只要有人知道你的地址，就能直接操控这个拥有高权限的AI，对你的电脑为所欲为。这是最容易踩、也最常见的坑。

风险二：恶意插件（Skills）。OpenClaw有一套插件生态，各种第三方开发的功能包。但这个生态审核宽松，公开审计曾在 2，857 个 skills 中识别出 341 个恶意项——你主动安装了，等于主动装了木马。只要对来源保持谨慎，这个风险完全可以规避。

风险三：指令注入，最隐蔽，最难防。你让它看网页，网页也可能反过来“骗”它。页面里藏一段看不见的诱导文本，AI 可能把那段话误当成上级命令执行——比如悄悄把你桌面上的文件发送到某个陌生网址。这类攻击无声无息，事后你可能都不知道发生过什么。

  

05 | 安全上手：给想尝试的人的实用建议

如果你确实想用OpenClaw来自动化一些日常工作（比如公众号运营、文件整理、数据汇总），有几条安全底线值得牢记：

给它一台专用的电脑，别和主力机混用。如果条件允许，用一台独立的电脑（比如一台专用的Mac mini）来跑OpenClaw，不要和你存放重要文件、涉及公司数据的主力机混用。这是把风险“圈起来”最直接的方式。

让AI在你家里干活，别让它把你的东西带出去。尽量避免使用需要把屏幕截图和指令发送到云端服务器的方案。通过Ollama等工具在本地部署大模型，所有数据处理在自己的电脑上完成，是最彻底的隐私保护。

装插件务必谨慎，宁缺毋滥。插件只从官方或极高可信度的来源安装，数量宁少勿多，安装前最好让懂技术的人看一眼代码。

发布按钮，永远自己按。在配置里为“发布文章”“执行命令”“删除文件”这类高风险操作开启手动确认——AI替你准备好，但真正按下发布键的，是你自己。这一步，不要省。

![](https://mmbiz.qpic.cn/mmbiz_jpg/a3jlfa2zsXK3YEJQVOuUVr8jC3ctLvjDSCzOjiao7xwtvQaNdFVialuCHFhrkfRXS9p0q8iaPtDFtN7TIonpfHcCP5S8icmx9vXN61seOI63hao/640?wx_fmt=jpeg&from=appmsg)

说到底，使用 OpenClaw 不只是一次技术尝试，更是一场关于“人机协同边界”的管理实验。你要像管理一个能力很强、但刚入职的员工一样管理它——给它任务，但不给它无限的授权。权限最小化，是这场实验里最重要的管理原则。

  

尾声：一个“半自动伙伴”，而不是“全自动神灵”

OpenClaw代表的，是AI与数字世界交互方式的一次根本性升级——从“调用接口”到“直接操作”，从“提建议”到“亲自干”。

但它目前最准确的定位，是一个强大的半自动伙伴。

让它处理那些重复的、有明确步骤的、消耗时间但不需要真正判断力的任务——选题调研、格式整理、素材搬运、初稿起草。而真正需要品味、判断、创造的部分，还是要你来。

效率，靠它提；决策，靠自己。

想象一下：你每天早上打开电脑，OpenClaw已经帮你整理好了今天的选题候选、抓取了相关资料、起草了初稿框架。你喝着咖啡，看一眼，改几处，按下发布。

这不是科幻，这是它现在能做到的事。

如果你想迈出第一步，有一个简单的路径可以参考：初学者先从云端版的 Kimi Claw 开始，不用折腾环境配置，直接体验“发一句话、AI帮你真的干活”是什么感觉；  

进阶玩家再考虑本地版，找一台旧电脑或闲置 Mac mini，慢慢折腾权限、技能包、隐私保护——这才是 OpenClaw 最有深度的玩法。

先上手，再优化。别让“还没搞懂”成为永远不试的借口。

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言