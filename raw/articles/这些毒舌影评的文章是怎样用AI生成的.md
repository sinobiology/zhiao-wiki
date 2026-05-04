     这些毒舌影评的文章是怎样用AI生成的 \* { margin: 0; padding: 0; outline: 0; } body { font-family: "PingFang SC", system-ui, -apple-system, BlinkMacSystemFont, "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei UI", "Microsoft YaHei", Arial, sans-serif; line-height: 1.6; } .\_\_page\_content\_\_ { max-width: 667px; margin: 0 auto; padding: 20px; text-size-adjust: 100%; color: rgba(0, 0, 0, 0.9); padding-bottom: 64px; } .title { user-select: text; font-size: 22px; line-height: 1.4; margin-bottom: 14px; font-weight: 500; } .\_\_meta\_\_ { color: rgba(0, 0, 0, 0.3); font-size: 15px; line-height: 20px; hyphens: auto; word-break: break-word; margin-bottom: 50px; } .\_\_meta\_\_ .nick\_name { color: #576B95; } .\_\_meta\_\_ .copyright { color: rgba(0, 0, 0, 0.3); background-color: rgba(0, 0, 0, 0.05); padding: 0 4px; margin: 0 10px 10px 0; } blockquote.source { padding: 10px; margin: 30px 0; border-left: 5px solid #ccc; color: #333; font-style: italic; word-wrap: break-word; } blockquote.source a { cursor: pointer; text-decoration: underline; } .item\_show\_type\_0 > section { margin-top: 0; margin-bottom: 24px; } a { color: #576B95; text-decoration: none; cursor: default; } .text\_content { margin-bottom: 50px; user-select: text; font-size: 17px; white-space: pre-wrap; word-wrap: break-word; line-height: 28px; hyphens: auto; } .picture\_content .picture\_item { margin-bottom: 30px; } .picture\_content .picture\_item .picture\_item\_label { text-align: center; } img { max-width: 100%; } .pay\_subscribe\_notice { margin: 30px 0; padding: 20px; background: #fffbe6; border: 1px solid #ffe58f; border-radius: 8px; } .pay\_subscribe\_badge { display: inline-block; padding: 4px 12px; background: #faad14; color: #fff; border-radius: 4px; font-size: 14px; font-weight: 500; margin-bottom: 12px; } .pay\_subscribe\_desc { font-size: 15px; line-height: 1.8; color: rgba(0, 0, 0, 0.7); margin-bottom: 12px; } .pay\_subscribe\_hint { font-size: 13px; color: rgba(0, 0, 0, 0.4); } .\_\_bottom-bar\_\_ { display: flex; justify-content: space-between; align-items: center; position: fixed; bottom: 0; left: 0; right: 0; height: 64px; padding: 8px 20px; background: white; box-sizing: border-box; border-top: 1px solid rgba(0, 0, 0, 0.2); } .\_\_bottom-bar\_\_ .left { display: flex; align-items: center; font-size: 15px; white-space: nowrap; } .\_\_bottom-bar\_\_ .right { display: flex; } .\_\_bottom-bar\_\_ .sns\_opr\_btn { display: flex; align-items: center; user-select: none; background: transparent; border: 0; color: rgba(0, 0, 0, 0.9); font-size: 14px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn:not(:last-child) { margin-right: 16px; } .\_\_bottom-bar\_\_ .sns\_opr\_btn > img { margin-right: 4px; }

这些毒舌影评的文章是怎样用AI生成的
==================

原创 知奥zhao 知奥ZHAO 2025-09-18 11:18 宁夏

> 原文地址: [https://mp.weixin.qq.com/s/\_GVbTxDWlWN45Fi965Mdrw](https://mp.weixin.qq.com/s/_GVbTxDWlWN45Fi965Mdrw)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37Biag5aqqbscM8wr4XhGEkexH3guyy7xBnPHW5Jfzw2SOPFegPYM99icTW26LCGUNAIAf6RkMTnEVGA/640?wx_fmt=png)

文：知奥

2025年3月28日到4月20日，整个公众号发表了14篇毒舌影评风格的文章，其实同期草稿箱里还有很多，已经删除不用了。这些文章都是用搭建的AI智能体自动生成的。

我在3月9日参加了“如何用好DeepSeek”的AI课程训练营，整个课程费用3200，课程目录如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37Biag5aqqbscM8wr4XhGEkex1iatEUa4MNO6PBFPNAnEJcQV7ewO0bBBibzvNibComYTIvBbDXF68Xic0A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37Biag5aqqbscM8wr4XhGEkex6X8iaTnCaW702IjYbIliauBk1RNW974F4eibKUFhrTY1QXfZNpnEkib7uQ/640?wx_fmt=png&from=appmsg)

其中用扣子搭建工作流就可以实现按照要求自动执行公众号发文。扣子（Coze）属于字节跳动旗下的AI智能体应用开发平台，其核心目标是让开发者能够低门槛、高效地创建和部署AI应用，网址是：www.coze.cn。

* * *

具体搭建好的智能体流程图是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37Biag5aqqbscM8wr4XhGEkex0b5uyWq84lJMqJibibq8IBanVvaiapUvFgVwEBtiax0hxgtXZMVE6Ip1Sw/640?wx_fmt=png&from=appmsg)

具体搭建的操作方法很简单，就是把各个模块用鼠标拖拽连接，然后对每个模块要完成的任务写提示词，核心还是你构建整体流程的设计思路。所以重点接收整个项目拆解的思路。

一、项目目标：微信公众号定期自动发送某一个电影的影评文章；

二、拆解目标：按照目标，输出文章应该包括以下几方面的要求

1.  定时发送；
    
2.  自动选取电影；
    
3.  有头部图片；
    
4.  有标题；
    
5.  有正文，针对电影的评论，毒舌风格；
    

  

* * *

三、组成模块及提示词：每个模块会根据目的需要选择负责执行指令的AI大模型，文字大模型或文生图大模型；

1.  输入模块：负责自动选取电影，并进行评价输出正文，提示词：你是一个自媒体创作者，文风犀利，每天会选取不同的热门电影进行犀利的评价。
    
2.  标题生成模块：负责根据第一个模块输出的文字生成标题，提示词：帮我提取文章的主标题，要求越标题党越好，要吸引眼球，更加靠近10W+阅读量公众号的取名方式。除了提供15字以内的主标题外，其他任何东西都不需要提供。
    
3.  头图生成模块：需要两步，先根据第一模块输出的文字主题生成一个文字生图片的提示词，第二步根据文生图提示词生产图片。提示词：根据内容，生成且只生成1个符合主题的文字生成图片的提示词，我比较喜欢写实风格带一些年代感的内容；
    
4.  自动排版模块：需要把模块1输出的文字进行排版，符合微信公众号的阅读习惯，提示词：使用HTML格式分装内容，你需要逐个检查每个字符，遇到中文句号“。”时，计数器加1。当计数器达到2时，在当前字符后添加<br><br，并重置计数器。原句号会被保留，仅在其后追加换行标签。用这种方式将全文格式改写为HTML格式禁用任何非HTML内容、禁止添加注释或说明文字、不要包含任何JavaScript代码、避免使用全角空格和不间断空格等异常字。
    
5.  自动发送微信公众号模块：
    
    ①Get access token插件：成为微信公众平台开发者，并获取access token（要实现将扣子中AI生成的内容自动化推送至微信公众号，需先注册成为微信公众平台开发者并获取接口调用凭证（Access Token），才能实现）
    
    ②add\_material插件：把对应素材放到微信公众号素材库；
    
    ③add\_draft插件：保存文章到草稿箱中；
    
    ④publish article：按时发送草稿箱内对应编号的文章；
    
      
    
      
    

* * *

 以上算是一个简略的教程，微信公众号与AI的结合，衍生出大量用AI批量管理的账号。这些AI账号可能会形成一个知识矩阵，每天根据不同主题发出大量AI生成的内容来测试流量，这已经形成了一个产业。

所以，AI时代会不会导致失业？这个问题是要一分为二的看，还是那句著名的话：取代你的不是AI，而是会使用AI的人。

另外，不要在意这些AI账号的内容有没有营养，跟人类创作相比有多么低级。实际上这些都不重要，因为现在信息爆炸的时代，99%的内容都淹没在信息的汪洋大海之中，即使是你亲自写的内容也大概率没人看，那我们持续维护一个公众号的意义何在？

因为写作是最好的输出，写作的过程中可以帮你理清思路，提升思考的逻辑性。写作也是最好的记录，无论你记录什么内容，都是更加丰富了你作为人的体验和回忆。等你老了以后，看到这些自己记录的文字，回想起当时写下它们时的感受，或许感慨当年的幼稚、或许感谢当时的努力、或许感动当时的自己、或许感恩一路的知己，无论是什么情绪，你应该感谢当年自己的记录给岁月赋予了独特的意义，让多少年以后隔空相望的两个自己，真切地明白了茫茫宇宙中渺小的自己是怎么磕磕绊绊地一路走来的，这也许就是写作的最大意义。

给时间以生命，而不是给生命以时间。

  

  

![](http://mmbiz.qpic.cn/sz_mmbiz_png/ogQWzRFB37AGictiaFhibAUtib0zhic9OwXF8KDicVs9YLhHyzt8wAu2thtt2UfGRMCcd1nThwpNuIHYGTtVZhkcib1UQ/0?wx_fmt=png) 知奥ZHAO

 ![](data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E%3C!-- Icon from Lucide by Lucide Contributors - https://github.com/lucide-icons/lucide/blob/main/LICENSE --%3E%3Cg fill='none' stroke='%23888888' stroke-linecap='round' stroke-linejoin='round' stroke-width='2'%3E%3Cpath d='M2.062 12.348a1 1 0 0 1 0-.696a10.75 10.75 0 0 1 19.876 0a1 1 0 0 1 0 .696a10.75 10.75 0 0 1-19.876 0'/%3E%3Ccircle cx='12' cy='12' r='3'/%3E%3C/g%3E%3C/svg%3E) 阅读![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath fill-rule='evenodd' clip-rule='evenodd' d='M16.154 6.797l-.177 2.758h4.009c1.346 0 2.359 1.385 2.155 2.763l-.026.148-1.429 6.743c-.212.993-1.02 1.713-1.977 1.783l-.152.006-13.707-.006c-.553 0-1-.448-1-1v-8.58a1 1 0 0 1 1-1h2.44l1.263-.03.417-.018.168-.015.028-.005c1.355-.315 2.39-2.406 2.58-4.276l.01-.16.022-.572.022-.276c.074-.707.3-1.54 1.08-1.883 2.054-.9 3.387 1.835 3.274 3.62zm-2.791-2.52c-.16.07-.282.294-.345.713l-.022.167-.019.224-.023.604-.014.204c-.253 2.486-1.615 4.885-3.502 5.324l-.097.018-.204.023-.181.012-.256.01v8.218l9.813.004.11-.003c.381-.028.72-.304.855-.709l.034-.125 1.422-6.708.02-.11c.099-.668-.354-1.308-.87-1.381l-.098-.007h-5.289l.26-4.033c.09-1.449-.864-2.766-1.594-2.446zM7.5 11.606l-.21.005-2.241-.001v8.181l2.45.001v-8.186z' fill='%23000'/%3E%3C/svg%3E) 赞 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cpath d='M0 0h24v24H0z'/%3E    %3Cpath fill='%23576B95' d='M13.707 3.288l7.171 7.103a1 1 0 0 1 .09 1.32l-.09.1-7.17 7.104a1 1 0 0 1-1.705-.71v-3.283c-2.338.188-5.752 1.57-7.527 5.9-.295.72-1.02.713-1.177-.22-1.246-7.38 2.952-12.387 8.704-13.294v-3.31a1 1 0 0 1 1.704-.71zm-.504 5.046l-1.013.16c-4.825.76-7.976 4.52-7.907 9.759l.007.287c1.594-2.613 4.268-4.45 7.332-4.787l1.581-.132v4.103l6.688-6.623-6.688-6.623v3.856z'/%3E  %3C/g%3E%3C/svg%3E) 分享 ![](data:image/svg+xml;charset=utf8,%3Csvg xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='24' height='24' viewBox='0 0 24 24'%3E  %3Cdefs%3E    %3Cpath id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-a' d='M0 0h24v24H0z'/%3E  %3C/defs%3E  %3Cg fill='none' fill-rule='evenodd'%3E    %3Cmask id='a62bde5b-af55-42c8-87f2-e10e8a48baa0-b' fill='%23fff'%3E      %3Cuse xlink:href='%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-a'/%3E    %3C/mask%3E    %3Cg mask='url(%23a62bde5b-af55-42c8-87f2-e10e8a48baa0-b)'%3E      %3Cg transform='translate(0 -2.349)'%3E        %3Cpath d='M0 2.349h24v24H0z'/%3E        %3Cpath fill='%23576B95' d='M16.45 7.68c-.954 0-1.94.362-2.77 1.113l-1.676 1.676-1.853-1.838a3.787 3.787 0 0 0-2.63-.971 3.785 3.785 0 0 0-2.596 1.112 3.786 3.786 0 0 0-1.113 2.687c0 .97.368 1.938 1.105 2.679l7.082 6.527 7.226-6.678a3.787 3.787 0 0 0 .962-2.618 3.785 3.785 0 0 0-1.112-2.597A3.687 3.687 0 0 0 16.45 7.68zm3.473.243a4.985 4.985 0 0 1 1.464 3.418 4.98 4.98 0 0 1-1.29 3.47l-.017.02-7.47 6.903a.9.9 0 0 1-1.22 0l-7.305-6.73-.008-.01a4.986 4.986 0 0 1-1.465-3.535c0-1.279.488-2.56 1.465-3.536A4.985 4.985 0 0 1 7.494 6.46c1.24-.029 2.49.4 3.472 1.29l.01.01L12 8.774l.851-.85.01-.01c1.046-.951 2.322-1.434 3.59-1.434 1.273 0 2.52.49 3.472 1.442z'/%3E      %3C/g%3E    %3C/g%3E  %3C/g%3E%3C/svg%3E) 推荐 ![](data:image/svg+xml,%3Csvg width='25' height='24' viewBox='0 0 25 24' fill='none' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M22.242 7a2.5 2.5 0 0 0-2.5-2.5h-14a2.5 2.5 0 0 0-2.5 2.5v8.5a2.5 2.5 0 0 0 2.5 2.5h2.5v1.59a1 1 0 0 0 1.707.7l1-1a.569.569 0 0 0 .034-.03l1.273-1.273a.6.6 0 0 0-.8-.892v-.006L9.441 19.1l.001-2.3h-3.7l-.133-.007A1.3 1.3 0 0 1 4.442 15.5V7l.007-.133A1.3 1.3 0 0 1 5.742 5.7h14l.133.007A1.3 1.3 0 0 1 21.042 7v4.887a.6.6 0 1 0 1.2 0V7z' fill='%23000' fill-opacity='.9'/%3E%3Crect x='14.625' y='16.686' width='7' height='1.2' rx='.6' fill='%23000' fill-opacity='.9'/%3E%3Crect x='18.725' y='13.786' width='7' height='1.2' rx='.6' transform='rotate(90 18.725 13.786)' fill='%23000' fill-opacity='.9'/%3E%3C/svg%3E) 留言