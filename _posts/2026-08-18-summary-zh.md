---
layout: default
title: "Horizon Summary: 2026-08-18 (ZH)"
date: 2026-08-18
lang: zh
---

> 从 31 条内容中筛选出 14 条重要资讯。

---

1. [Qwen 3.8 27B 在 AI 智能指数上与 GPT-5.6 Luna 持平](#item-1) ⭐️ 9.0/10
2. [Linux 7.3 内核改进显存超额分配性能](#item-2) ⭐️ 8.0/10
3. [Cursor 推出 Origin，一款面向代码托管的 AI 原生 GitHub 替代品](#item-3) ⭐️ 8.0/10
4. [调查追踪珍稀书籍运往亚马逊 AI 训练设施](#item-4) ⭐️ 8.0/10
5. [开发者在 264KB RAM 微控制器上运行扩散模型](#item-5) ⭐️ 8.0/10
6. [研究人员揭露稀疏注意力和 KV 缓存压缩研究中的方法学技巧](#item-6) ⭐️ 8.0/10
7. [利用铁路网络作为平板扫描仪拍摄全景照片](#item-7) ⭐️ 7.0/10
8. [亚马逊搜索机制转变如何降低用户体验并促使消费者流失](#item-8) ⭐️ 7.0/10
9. [使用专用工具恢复变砖的 Framework 笔记本电脑](#item-9) ⭐️ 7.0/10
10. [Fairphone 正式在美国直接销售 Gen 6+智能手机](#item-10) ⭐️ 7.0/10
11. [谷歌以 1000 万美元收购精神航空数据用于训练 AI](#item-11) ⭐️ 7.0/10
12. [Meta 申请智能眼镜人脸识别与自动录制专利](#item-12) ⭐️ 7.0/10
13. [Bluesky 如何在截图上动态渲染其标志](#item-13) ⭐️ 7.0/10
14. [SineKAN 将正弦激活函数引入柯尔莫哥洛夫-阿诺德网络](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Qwen 3.8 27B 在 AI 智能指数上与 GPT-5.6 Luna 持平](https://simonwillison.net/2026/Aug/17/qwen-38-27b-scores-52/) ⭐️ 9.0/10

阿里巴巴通义实验室发布了 Qwen 3.8 27B，这款 270 亿参数的开源模型在 Artificial Analysis 智能指数上获得了 52 分，与 GPT-5.6 Luna 持平，仅略低于 GLM-5.2（753B）和 DeepSeek V4 Pro（1.7T 参数）等更大规模的模型。 这一成就证明了模型效率的重大飞跃，表明相对较小且适合消费级硬件运行的模型能够匹敌庞大且资源密集型的同类模型，从而显著降低了本地部署 AI 的门槛。 该模型默认采用“极高”推理强度设置，若不将上下文窗口扩展至完整的 262,144 限制，在消费级硬件上会导致过度消耗 token 和生成时间过长。该模型采用 Apache 2.0 开源协议，具备视觉能力，并能有效运行如 17GB Q4_K_M 等量化版本。

rss · Simon Willison · 8月17日 23:58

**背景**: Artificial Analysis 智能指数是一项综合基准测试，用于评估语言模型在推理、编程、知识和多步骤任务完成方面的能力。在 AI 行业中，模型性能传统上随参数数量增加而提升，这使得较小规模的模型天生能力较弱。Qwen 3.8 27B 以极少的参数实现了顶尖分数，挑战了这一传统范式，凸显了训练技术和架构优化的进步。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://artificialanalysis.ai/evaluations/artificial-analysis-intelligence-index">Artificial Analysis Intelligence Index | Artificial Analysis</a></li>
<li><a href="https://huggingface.co/Qwen/Qwen3.8-27B">Qwen/Qwen3.8-27B · Hugging Face</a></li>
<li><a href="https://developers.cloudflare.com/workers-ai/models/qwen3.8-27b/">qwen3.8-27b (Qwen) · Cloudflare AI docs · Cloudflare Workers AI docs</a></li>

</ul>
</details>

**社区讨论**: 该新闻通过 Hacker News 分享，表明技术社区对该模型的效率及其开源发布表现出了浓厚的兴趣和认可。

**标签**: `#AI`, `#LLMs`, `#Model Efficiency`, `#Generative AI`, `#Qwen`

---

<a id="item-2"></a>
## [Linux 7.3 内核改进显存超额分配性能](https://pixelcluster.dev/VRAM-Overcommit/) ⭐️ 8.0/10

Linux 7.3 内核将合并上游补丁，显著改进显存（VRAM）管理，特别是优化了操作系统处理应用程序请求超出物理显存容量时的表现。这些由 Valve 工程师 Philip Vock 开发的补丁增强了 8GB 及以下显存 GPU 的后台显存管理，使游戏和 AI 工作负载在超额分配内存时能减少性能损失。 此次更新对 Linux 游戏玩家和 AI 开发者意义重大，因为它缓解了传统上因显存耗尽而导致的严重掉帧和系统冻结问题。通过优化内核处理内存超额分配的方式，Linux 在应对高内存需求应用方面提供了更流畅的体验，进一步缩小了与专有操作系统内存管理策略的差距。 这些改进允许应用程序在物理限制之外超额分配显存（例如在 8GB 显卡上使用 9GB），通过智能管理后台资源来减少帧时间波动。然而，尽管内核补丁改进了分配策略，最终效率仍依赖于应用程序向操作系统正确传达其内存驻留需求。

hackernews · flaburgan · 8月18日 07:51 · [社区讨论](https://news.ycombinator.com/item?id=49342719)

**背景**: 显存超额分配发生在软件尝试使用超出 GPU 物理容量的显存时，迫使操作系统在高速显存和较慢的系统内存之间交换数据。历史上，Linux 在此类事件中常因激进的内存不足（OOM）终止机制和系统冻结而表现不佳，而 Windows 则能更平稳地处理内存分页。Linux 内核的内存管理子系统（包括 OOM 终止机制）负责回收资源，但与标准系统内存相比，GPU 显存历来更难进行动态管理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.phoronix.com/news/Linux-7.3-Improving-vRAM-Mgmt">Linux 7.3 To Land Initial Code Improving vRAM Management ...</a></li>
<li><a href="https://pixelcluster.dev/VRAM-Overcommit/">VRAM Management Part 2: Beyond the Limits of Physical VRAM</a></li>
<li><a href="https://www.techpowerup.com/348178/valve-engineer-improves-linux-memory-management-for-gpus-with-8-gb-vram-or-less">Valve Engineer Improves Linux Memory Management for GPUs with ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪非常积极，用户称赞了文章的技术深度，并对 Linux 持续的性能改进表示兴奋，这与 Windows 用户的更新疲劳形成鲜明对比。讨论突出了 Linux 和 Windows 在 OOM 处理上的差异，同时也指出 macOS 在显存耗尽时表现出不同但可控的行为。部分用户强调，尽管内核改进至关重要，但应用程序本身最适合管理其内存优先级。

**标签**: `#Linux Kernel`, `#Memory Management`, `#VRAM`, `#Performance Optimization`, `#Systems Engineering`

---

<a id="item-3"></a>
## [Cursor 推出 Origin，一款面向代码托管的 AI 原生 GitHub 替代品](https://cursor.com/changelog/origin-code-hosting) ⭐️ 8.0/10

Cursor 推出了 Origin，这是一个面向代码托管的 AI 原生平台，目前正面向所有付费计划推出早期测试版，提供代码仓库、拉取请求、代码浏览和 GitHub 同步功能。该平台允许开发者通过几次点击将项目从 GitHub 复制过来，并自动同步上游更新。 此举使 Cursor 能够直接挑战 GitHub 在开发者基础设施领域的主导地位，尤其是在近期宕机事件凸显集中式代码托管风险之际。通过将代码托管与 AI 原生工作流集成，Cursor 旨在为 AI 代理和人类开发者简化整个开发生命周期。 Origin 目前处于仅限付费用户的早期测试阶段，尚不能完全替代 GitHub。该平台的名称“Origin”与 Git 标准的远程仓库命名约定重叠，引发了关于 LLM 在执行 git 命令时可能产生语义混淆的担忧。

hackernews · tomasreimers · 8月17日 17:02 · [社区讨论](https://news.ycombinator.com/item?id=49334209)

**背景**: GitHub 是托管和协作代码仓库的行业标准平台，被全球开发者和组织广泛使用。Cursor 最初由 Anysphere 开发，是一款 AI 驱动的代码编辑器，在被 SpaceX 收购后估值达到 600 亿美元。Origin 的推出反映了 AI 原生公司正不断向核心开发者基础设施扩展，以构建紧密集成的生态系统这一更广泛的趋势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cursor.com/changelog/origin-code-hosting">Origin Code Hosting · Cursor</a></li>
<li><a href="https://siliconangle.com/2026/08/17/cursor-launches-origin-code-hosting-service-to-compete-with-github/">Cursor launches Origin code hosting service to compete with GitHub - SiliconANGLE</a></li>
<li><a href="https://venturebeat.com/infrastructure/cursor-launches-origin-code-hosting-platform-as-github-outage-exposes-opening-in-ai-coding-race">Cursor launches Origin code hosting platform as GitHub outage exposes opening in AI coding race | VentureBeat</a></li>

</ul>
</details>

**社区讨论**: 社区反应褒贬不一，有人赞赏其对 GitHub 的颠覆，也有人对 AI 信任、数据隐私以及平台目前的测试版限制表示担忧。一个显著的争论集中在“Origin”这一命名选择上，它与 Git 默认的远程仓库名称冲突，可能会混淆 AI 代理。此外，鉴于该平台尚处早期阶段且存在报告的性能问题，用户对其 600 亿美元的估值提出了质疑。

**标签**: `#AI`, `#Code Hosting`, `#GitHub Alternative`, `#Software Engineering`, `#Developer Tools`

---

<a id="item-4"></a>
## [调查追踪珍稀书籍运往亚马逊 AI 训练设施](https://simonwillison.net/2026/Aug/17/we-tracked-a-shipment-of-rare-books-it-ended-at-an-amazon-ai-tra/) ⭐️ 8.0/10

404 Media 的调查记者通过 Biblio 平台订购了一本珍稀书籍并放入 Apple AirTag，成功追踪到该书籍被送往拉斯维加斯亚马逊设施的 VGT3 区域。亚马逊员工的在线讨论证实，该地点正在对大量书籍进行破坏性扫描以获取 AI 训练数据。 该调查提供了确凿的物理证据，表明大型 AI 公司正在获取并销毁实体书籍以构建训练数据集，从而绕过了传统的网络抓取。这引发了关于版权、合理使用以及为机器学习销毁珍稀书籍的文化影响的重大伦理和法律问题。 追踪结果显示目的地为拉斯维加斯东北部的 LAS8 亚马逊设施，其标志是一只拿着书的恐龙。该调查方法依赖于隐藏在 Biblio 市场上一位匿名且对价格不敏感的买家订购的约 1000 本书籍中的一枚 Apple AirTag。

rss · Simon Willison · 8月17日 15:21

**背景**: 随着 AI 模型能力的提升，公司越来越寻求超越公开网络内容的高质量、未受污染的训练数据。实体书籍，尤其是珍稀或绝版书籍，提供了难以通过数字方式获取的独特文本数据。破坏性书籍扫描涉及使用自动化机器切掉书脊以便快速逐页数字化，这一过程会永久销毁原始实体副本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ainave.com/tech-news/ai-companies-are-buying-and-destroying-antique-books-for-training-data-what-builders-need-to-know">Antique Books AI Training Data: Ethics and Legal Risks</a></li>
<li><a href="https://futurism.com/artificial-intelligence/ai-companies-destroying-rare-books">AI Companies Are Buying Antique Books, Ingesting Their ...</a></li>

</ul>
</details>

**标签**: `#AI Training Data`, `#Investigative Journalism`, `#Copyright Ethics`, `#Amazon AI`, `#Data Sourcing`

---

<a id="item-5"></a>
## [开发者在 264KB RAM 微控制器上运行扩散模型](https://www.reddit.com/r/MachineLearning/comments/1vrk7t5/trained_an_diffusion_model_that_runs_on_264kb_of/) ⭐️ 8.0/10

一位开发者成功在仅有 264KB SRAM 的 Shrike lite 微控制器上训练并部署了一个用于生成 32x32 像素图像的扩散模型。他们还在板载 FPGA 上创建了两个并行的 INT8 MAC 引擎并采用 16 位累加，但系统最终遇到了内存瓶颈，导致 FPGA 加速版本的速度反而慢于仅使用 MCU 的版本。 这一成果展示了 TinyML 和模型压缩的极限，证明了扩散模型等复杂生成式 AI 可以在资源极度受限的边缘设备上运行。它凸显了微控制器上硬件加速的实际挑战，即内存带宽和 I/O 瓶颈可能会抵消并行计算引擎带来的性能优势。 由于高 I/O 操作触及内存墙，FPGA 加速版本生成每张图像耗时约 220 秒，而仅使用 MCU 的版本仅需约 70 秒。重度量化和严格的内存限制导致生成的图像充满噪点且有时看起来很奇怪，但仍有一些输出在视觉上颇具趣味。

reddit · r/MachineLearning · /u/PandaBean18 · 8月18日 09:26

**背景**: 扩散模型是一类生成式 AI，通常以极高的计算和内存需求著称，往往需要在强大的 GPU 上运行。TinyML 专注于在内存和处理能力极其有限的微控制器上部署机器学习模型，通常需要激进模型压缩和量化技术。Shrike lite 是一款开源开发板，结合了 RP2040 微控制器和小型 FPGA，旨在为嵌入式项目提供易于使用的硬件加速方案。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/fcpage/shrike-lite">GitHub - fcpage/shrike-lite: Low cost microcontroller + FPGA ...</a></li>
<li><a href="https://store.vicharak.in/?product=shrike">Shrike-lite (RP2040 + 1KLUT FPGA) – Vicharak Store</a></li>
<li><a href="https://hanlab.mit.edu/topics/tinyml">TinyML - MIT HAN Lab</a></li>

</ul>
</details>

**标签**: `#TinyML`, `#Diffusion Models`, `#Edge AI`, `#Hardware Optimization`, `#Model Compression`

---

<a id="item-6"></a>
## [研究人员揭露稀疏注意力和 KV 缓存压缩研究中的方法学技巧](https://www.reddit.com/r/MachineLearning/comments/1vqqqcs/how_to_make_any_sparse_attention_kv_compression/) ⭐️ 8.0/10

这篇评论意义重大，因为它指出了广泛存在的基准测试污染和评估缺陷，这些缺陷误导了机器学习社区关于效率优化真实有效性的认知。它敦促研究人员采用更严格的评估标准，这将最终促成更可靠且真正高效的大语言模型架构。 作者详细列举了具体的技巧，例如使用带有无关上下文的合成任务、为新方法调整超参数而保持基线不变，以及使用自定义 Triton 内核优化实现速度以掩盖增加的计算工作量。他们还警告不要仅依赖 RULER 等聚合指标，因为这些指标可能会掩盖在 NIAH-MK3 等压力测试中的失败。

reddit · r/MachineLearning · /u/korec1234 · 8月17日 12:18

**背景**: 稀疏注意力机制和 KV 缓存压缩是降低大语言模型（LLM）处理长序列时计算和内存成本的关键技术。像“大海捞针”（NIAH）测试和 RULER 这样的基准测试通常用于评估这些方法在压缩下保持信息检索能力的效果。然而，随着该领域的成熟，确保这些评估免受污染和方法学偏见的影响变得越来越重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://medium.com/@vishal09vns/sparse-attention-dad17691478c">Demystifying Sparse Attention: A Comprehensive Guide from Scratch | by VISHAL SINGH | Medium</a></li>
<li><a href="https://github.com/gkamradt/needle-in-a-haystack">Needle In A Haystack - GitHub</a></li>
<li><a href="https://arxiv.org/pdf/2603.20397">KV Cache Optimization Strategies for Scalable and Efficient ...</a></li>

</ul>
</details>

**标签**: `#Sparse Attention`, `#KV Cache Compression`, `#ML Benchmarking`, `#Research Methodology`, `#Large Language Models`

---

<a id="item-7"></a>
## [利用铁路网络作为平板扫描仪拍摄全景照片](https://philo.gay/linecam/) ⭐️ 7.0/10

一个创意编程项目将铁路网络重新用作移动平台，通过线扫描摄影技术，在列车沿轨道移动时拼接连续的图像条带，从而拍摄出宽幅的平板式全景图像。 该项目展示了硬件破解、计算机视觉与艺术表达的创新结合，证明了日常基础设施可以被重新利用于高分辨率成像和创意应用。 该技术依赖于线扫描摄影原理，即随时间重复捕获单行像素以构建二维图像，并利用列车稳定的运动作为自然的扫描机制。

hackernews · otherayden · 8月18日 12:43 · [社区讨论](https://news.ycombinator.com/item?id=49344825)

**背景**: 线扫描相机传统上使用单行传感器和相对运动来捕获高分辨率的二维图像，通常应用于工业检测、卫星成像和文档扫描。与一次性捕获完整画面的面阵相机不同，线扫描系统按顺序构建图像，使其非常适合连续或移动的拍摄对象。该项目创造性地改编了这一原理，将铁路网络和行驶的列车用作扫描平台。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Line-scan_camera">Line-scan camera - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Strip_photography">Strip photography - Wikipedia</a></li>
<li><a href="https://www.nextscan.com/line-scan-cameras-vs-area-scan-cameras-microfilm-scanning/">Line Scan Cameras vs. Area Scan Cameras – Microfilm Scanning - nextScan</a></li>

</ul>
</details>

**社区讨论**: 社区成员分享了历史先例，指出早在 2008 年 Ward Cunningham 等人就进行过类似实验，同时也强调了独立的实现方式和艺术应用。用户赞扬了该项目在实用性与艺术性之间的巧妙结合，部分人讨论了该技术如何抽象化背景并将注意力集中在主体上。

**标签**: `#photography`, `#creative-coding`, `#computer-vision`, `#hardware-hacking`, `#line-scan`

---

<a id="item-8"></a>
## [亚马逊搜索机制转变如何降低用户体验并促使消费者流失](https://seths.blog/2026/08/the-amazon-tax/) ⭐️ 7.0/10

一项分析指出，亚马逊的搜索和推荐系统已从以用户为中心的发现模式转变为平台驱动的引导模式，优先考虑亚马逊的商业利益而非用户意图。这种搜索质量的下降正促使长期用户转向本地商店和 Etsy 等替代平台。 这一转变凸显了一个更广泛的行业趋势，即主导平台为了收入和广告位优化，而非真正的用户发现，最终降低了信任度并推动了消费者流失。这标志着电子商务可能出现一个转折点，因为用户正在积极寻求优先考虑真实产品发现的替代方案。 该平台的算法现在严重偏向赞助列表和语义引导，这些引导会左右购买决策，实际上将搜索变成了最大化平台收入而非定位确切商品的工具。用户报告称，必须使用广告拦截器和替代发现方法才能在杂乱的界面中导航。

hackernews · herbertl · 8月18日 13:22 · [社区讨论](https://news.ycombinator.com/item?id=49345263)

**背景**: 亚马逊的推荐系统历史上依赖于基于用户购买历史和相似用户行为的项对项协同过滤来推荐产品。随着平台规模的扩大和广告成为主要收入来源，算法逐渐演变为纳入机器学习模型，以平衡用户相关性和赞助展示等商业激励。这种演变反映了科技平台的一个更广泛模式，即搜索功能从中立工具转变为货币化的参与工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amazon.science/the-history-of-amazons-recommendation-algorithm">The history of Amazon's recommendation algorithm</a></li>
<li><a href="https://www.baeldung.com/cs/amazon-recommendation-system">How Does the Amazon Recommendation System Work? - Baeldung</a></li>

</ul>
</details>

**社区讨论**: 社区成员普遍同意亚马逊的搜索已退化为一个平台驱动的引导系统，优先考虑广告而非真正的发现，许多用户正积极转向竞争对手或本地商店。一些评论者指出这是主要科技平台的普遍趋势，而其他人则强调大量广告通常意味着其他地方存在更好的替代品。

**标签**: `#platform-economics`, `#search-algorithms`, `#user-experience`, `#e-commerce`, `#tech-critique`

---

<a id="item-9"></a>
## [使用专用工具恢复变砖的 Framework 笔记本电脑](https://quantum5.ca/2026/08/16/fixing-bricked-amd-7040-series-framework-13-laptop-with-20-tools/) ⭐️ 7.0/10

一篇详细的技术指南展示了如何使用专用硬件工具和手动 BIOS 刷写技术来恢复一台变砖的 Framework Laptop 13（AMD 7040 系列）。该文章提供了逐步说明，以绕过导致设备无法启动的失败固件更新。 该指南强调了现代笔记本电脑中硬件可修复性和用户可访问固件恢复的关键重要性。它强化了模块化设计的价值，并赋予用户在制造商软件更新失败时避免电子垃圾的能力。

hackernews · jp_sc · 8月18日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49345220)

**背景**: “变砖”的笔记本电脑是指完全无响应的设备，通常是由于 BIOS 损坏或固件更新失败所致。BIOS（基本输入输出系统）是在启动期间初始化硬件的底层软件；如果它失败，系统将无法启动。Framework 笔记本电脑专门以模块化和可修复性为设计理念，具有易于访问的组件和标准化零件，以支持维修权运动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Framework_Laptop">Framework Laptop</a></li>
<li><a href="https://grokipedia.com/page/Framework_Laptop_13">Framework Laptop 13</a></li>
<li><a href="https://www.wikihow.com/Flash-a-Laptop-BIOS">How to Safely Flash the BIOS in a Windows Laptop: Easy Guide</a></li>

</ul>
</details>

**社区讨论**: 社区讨论凸显了用户对制造商对变砖设备责任的广泛不满，用户将 Framework 的可修复性与 ThinkPad 和 Dell 等企业笔记本电脑进行了积极比较。评论者强调 BIOS 更新失败仍然很常见，并认为制造商应为官方更新延长保修期，否则应对有缺陷的固件承担法律责任。几位用户指出，如果没有可访问的恢复方法，原本功能完好的硬件将变成电子垃圾。

**标签**: `#Hardware Repair`, `#Firmware`, `#Laptop Engineering`, `#Right to Repair`, `#BIOS`

---

<a id="item-10"></a>
## [Fairphone 正式在美国直接销售 Gen 6+智能手机](https://www.fairphone.com/nl/stories/the-fairphone-gen-6-is-all-about-giving-you-more) ⭐️ 7.0/10

Fairphone 已正式在美国开始直接销售其 Gen 6+智能手机，重点在于增强内部硬件和长期可用性，而非堆砌功能。该设备保持了该公司行业领先的易维修标准，同时提供有意的升级以延长手机的使用寿命。 此次发布为美国消费者提供了直接购买高可维修性和注重隐私的智能手机的渠道，挑战了计划性淘汰的行业常态。它支持硬件可持续性的更广泛趋势，并让用户对其设备的寿命拥有更多控制权。 Gen 6+型号支持完整的 T-Mobile 频段，包括关键的 LTE 频段 12 和 71 以及 5G 频段 n71，确保城市外地区的可靠覆盖。其摄像头模块与标准 Gen 6 相同，该模块已实现与 postmarketOS 的社区驱动兼容性，尽管 GrapheneOS 因过去的隐私和更新处理问题表达了兴趣降低。

hackernews · Vinnl · 8月18日 12:42 · [社区讨论](https://news.ycombinator.com/item?id=49344811)

**背景**: Fairphone 是一家荷兰电子公司，以设计注重道德采购、易维修和长期软件支持的模块化智能手机而闻名。与频繁发布带有渐进式升级新机型的主流制造商不同，Fairphone 专注于通过可更换组件和透明供应链来延长设备寿命。该公司历史上一直通过第三方零售商在美国销售设备，因此直接销售对美国买家来说是一个重大转变。

**社区讨论**: 社区反应既对直接在美国销售表示热情，也对设备的技术能力进行了严格审查。用户确认了完整的 T-Mobile 频段支持并指出了 postmarketOS 的摄像头兼容性，而其他人则指出 GrapheneOS 因过去的隐私和更新处理问题兴趣降低。一些人澄清说，Fairphone 设备此前已通过第三方卖家在美国销售，新的变化是直接购买。

**标签**: `#hardware`, `#repairability`, `#privacy`, `#mobile`, `#sustainability`

---

<a id="item-11"></a>
## [谷歌以 1000 万美元收购精神航空数据用于训练 AI](https://www.theregister.com/ai-and-ml/2026/08/18/google-buys-crashed-airline-spirits-data-at-auction-because-ai/5288962) ⭐️ 7.0/10

谷歌在破产拍卖中赢得了精神航空的大量业务数据和软件代码，同意支付 1000 万美元收购该数据集。该数据集包含数百万封电子邮件、客户服务通话、聊天记录和运营文档，但明确排除了乘客档案和忠诚度计划数据。 此次收购凸显了企业数据集作为训练企业 AI 模型的宝贵资产正日益商品化。这也引发了关于历史客户交互数据如何被去标识化并被科技巨头重新利用的重大隐私担忧。 该交易涉及法院批准的程序，由谷歌选定的第三方“去标识化代理”负责在数据传输前剥离个人身份信息。这 1000 万美元的购买涵盖了 ServiceNow 工单和机上 Wi-Fi 销售详情等运营和客户服务记录，但不包括直接的乘客支付或档案信息。

hackernews · pseudolus · 8月18日 10:13 · [社区讨论](https://news.ycombinator.com/item?id=49343559)

**背景**: 当公司申请破产时，其资产（包括知识产权和数据）通常会在拍卖中出售以偿还债权人。在 AI 时代，包含真实世界交互、日志和通信的大规模历史数据集已成为训练和微调机器学习模型的高度抢手资源。然而，客户交互数据的出售受到 CCPA 和 GDPR 等隐私法规的严格审查，需要严格的去标识化协议以防止个人信息泄露。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.axios.com/2026/08/17/google-spirit-airlines-bankruptcy">Google buys Spirit Airlines emails, chats, documents out of bankruptcy</a></li>
<li><a href="https://skift.com/2026/08/17/google-scoops-up-spirits-data-in-bankruptcy-sale-to-train-ai/">Google Scoops Up Spirit Airlines' Data in Bankruptcy Sale to Train AI</a></li>
<li><a href="https://www.thetraveler.org/googles-10m-spirit-airlines-data-buy-raises-ai-privacy-questions/">Google’s $10M Spirit Airlines data buy raises AI privacy questions</a></li>

</ul>
</details>

**社区讨论**: 社区成员对去标识化过程的有效性表示怀疑，并对如此广泛的个人交互数据被商品化感到不安。一些用户强调了所涉记录的庞大数量，而另一些人则质疑标准法律条款是否足以在这些交易中真正保护个人隐私。

**标签**: `#AI/ML`, `#Data Privacy`, `#Corporate Data`, `#Tech Industry`, `#Data Acquisition`

---

<a id="item-12"></a>
## [Meta 申请智能眼镜人脸识别与自动录制专利](https://www.privacyguides.org/news/2026/08/17/meta-files-patent-for-facial-recognition-automatic-recording-of-people/) ⭐️ 7.0/10

Meta 已申请一项智能眼镜专利，该专利具备人脸识别和自动录制功能，可在未经明确同意的情况下识别并录制个人。此前已有研究发现 Meta AI 应用中存在未经用户同意即部署的休眠人脸识别管道。 该专利加剧了围绕可穿戴 AI 技术的隐私与伦理担忧，可能使公共场所的非自愿监控常态化。这可能会严重影响智能眼镜的公众接受度，并引发针对 Meta 的监管审查或法律挑战。 该专利概述了自动识别和录制眼镜附近人员的技术，引发了关于同意和数据使用的质疑。批评者认为该技术在社交上不可接受，可能导致广泛的隐私侵犯，而部分人则质疑此类功能的商业可行性。

hackernews · DeepLogin · 8月18日 12:23 · [社区讨论](https://news.ycombinator.com/item?id=49344654)

**背景**: 人脸识别技术利用 AI 算法根据图像或视频中的面部特征来识别个人。智能眼镜（如 Meta 与 Ray-Ban 的合作产品）将摄像头和 AI 助手集成到可穿戴眼镜中。在消费级设备中部署此类技术引发了关于隐私权、同意权以及 AI 监控伦理边界的持续争论。

**社区讨论**: 社区情绪普遍负面，用户强烈表达了对隐私侵犯、非自愿监控以及 Meta 智能眼镜社交不可接受性的担忧。评论者强调了 Meta 在隐私方面的争议历史，质疑其对 Ray-Ban 等合作伙伴的品牌影响，并分享了凸显公众对该技术不适感的真实遭遇。

**标签**: `#Privacy`, `#Facial Recognition`, `#AI Ethics`, `#Smart Glasses`, `#Meta`

---

<a id="item-13"></a>
## [Bluesky 如何在截图上动态渲染其标志](https://timmarinin.net/2026/bluesky-screenshots/) ⭐️ 7.0/10

一项技术分析揭示，Bluesky 在 iOS 上使用了一个将 isSecureTextEntry 属性设置为 true 的隐藏 UITextField，该设置会在截图时清空应用内容，并动态叠加 Bluesky 的标志。 这一实现引发了关于用户控制权与应用品牌化之间的重大争论，突显了移动操作系统如何允许开发者出于增长黑客目的拦截和修改截图。 该技术依赖于 iOS 在屏幕捕获期间隐藏安全文本字段的原生行为，有效地将系统级隐私功能用作动态品牌化的画布。负责此功能的源文件被显著地命名为 GrowthHack.tsx。

hackernews · gavide · 8月17日 22:20 · [社区讨论](https://news.ycombinator.com/item?id=49338459)

**背景**: iOS 和 Android 等移动操作系统为开发者提供了限制或修改截图的 API，主要用于保护银行数据或流媒体内容等安全和 DRM 目的。开发者可以将特定的 UI 元素标记为安全，导致操作系统在捕获的图像中将其清空。Bluesky 重新利用了这种安全机制来插入其标志，将隐私功能转变为营销工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://timmarinin.net/2026/bluesky-screenshots/">How Bluesky draws its logo on screenshots</a></li>
<li><a href="https://recorder.easeus.com/screen-recording-tips/how-to-take-screenshots-in-restricted-apps.html">Why Some Apps Block Screenshots (And What Still Works ...</a></li>

</ul>
</details>

**社区讨论**: 社区情绪普遍负面，用户批评这种做法是对用户控制权的敌视，并滥用了操作系统级别的截图钩子。虽然有人承认这比永久性水印的侵入性更小，但许多人认为截图应严格反映用户屏幕上显示的内容，而不应受到应用的干扰。

**标签**: `#UI/UX`, `#Mobile Development`, `#Growth Hacking`, `#User Privacy`, `#Web Development`

---

<a id="item-14"></a>
## [SineKAN 将正弦激活函数引入柯尔莫哥洛夫-阿诺德网络](https://www.reddit.com/r/MachineLearning/comments/1vqdode/r_sinekan_kolmogorovarnold_networks_using/) ⭐️ 7.0/10

研究人员推出了 SineKAN，这是一种经过同行评审的柯尔莫哥洛夫-阿诺德网络（KAN）变体，它用重新加权的正弦函数网格取代了传统的 B 样条激活函数。该论文已发布于 arXiv（编号 2407.04149）并发表在 MDPI Mathematics 期刊上，同时提供了开源实现，并在基准视觉任务上评估了该模型的性能。 该方法通过利用周期性正弦函数解决了常见 KAN 模型在尺寸和速度上的限制，有望提高模型的表达能力和计算效率。它为神经网络架构研究提供了有意义的增量贡献，为需要高精度和可解释性的任务提供了一种实用的替代方案。 SineKAN 用正弦激活网格取代了可学习的 B 样条网格，与传统 KAN 相比，这可以减少参数量并提高训练速度。该实现在 GitHub 上开源，模型已在数值和视觉基准上进行了评估，但其更广泛的采用和可扩展性仍有待充分验证。

reddit · r/MachineLearning · /u/jacobgorm · 8月17日 00:46

**背景**: 柯尔莫哥洛夫-阿诺德网络（KAN）是一种受柯尔莫哥洛夫-阿诺德表示定理启发的神经网络架构，该定理指出任何多元连续函数都可以表示为单变量连续函数和加法的有限组合。与使用固定激活函数和线性权重的传统多层感知机（MLP）不同，KAN 在网络的边上放置可学习的单变量函数，通常使用 B 样条实现。B 样条是一种分段多项式函数，广泛用于平滑插值和逼近，但计算成本较高且占用内存较大。用正弦函数替代它们利用了周期函数可以用较少参数高效逼近复杂模式的数学特性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2407.04149">[2407.04149] SineKAN: Kolmogorov-Arnold Networks Using Sinusoidal Activation Functions</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kolmogorov-Arnold_Networks">Kolmogorov-Arnold Networks</a></li>
<li><a href="https://en.wikipedia.org/wiki/B-spline">B-spline - Wikipedia</a></li>

</ul>
</details>

**标签**: `#Kolmogorov-Arnold Networks`, `#Neural Architecture`, `#Activation Functions`, `#Deep Learning`, `#Machine Learning Research`

---