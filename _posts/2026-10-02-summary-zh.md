---
layout: default
title: "Horizon Summary: 2026-10-02 (ZH)"
date: 2026-10-02
lang: zh
---

> 从 28 条内容中筛选出 10 条重要资讯。

---

1. [联邦法院裁定犹他州屏蔽 VPN 法案在技术上不可行](#item-1) ⭐️ 8.0/10
2. [黑森林实验室发布 FLUX.3 Image，主打基于画布的构图控制](#item-2) ⭐️ 8.0/10
3. [安全研究员警告 AI 代理可能通过共享缓存传播蠕虫](#item-3) ⭐️ 8.0/10
4. [NeurIPS 2026 论文实现动力系统拓扑域外泛化](#item-4) ⭐️ 8.0/10
5. [FLEET 算法利用记忆引导的 MCTS 搜索优化大语言模型生成](#item-5) ⭐️ 8.0/10
6. [NeurIPS 2026 亮点论文提出面向混沌系统的循环神经网络并行时间训练法](#item-6) ⭐️ 8.0/10
7. [NeurIPS 2026 研究揭示大语言模型对权威来源的偏见](#item-7) ⭐️ 8.0/10
8. [OpenAI 推出 ChatGPT Sites 功能，实现快速 AI 网页原型设计与托管](#item-8) ⭐️ 7.0/10
9. [一篇关于冯·诺依曼传奇的 1973 年经典传记散文](#item-9) ⭐️ 7.0/10
10. [arXiv 限制作者每月最多提交两篇论文](#item-10) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [联邦法院裁定犹他州屏蔽 VPN 法案在技术上不可行](https://www.eff.org/deeplinks/2026/10/court-agrees-eff-utahs-vpn-law-demands-technical-impossibility) ⭐️ 8.0/10

联邦法院支持电子前沿基金会（EFF）的立场，裁定犹他州要求网络平台屏蔽 VPN 流量的法律在技术上无法实现且存在法律问题。该裁决同时废除了禁止网站分享绕过检查指南的相关条款。 此项裁决确立了一项重要先例，即州级互联网法规不能强制要求技术上无法实现的网络过滤，从而保护了平台运营者和用户的数字权利。它凸显了立法者试图控制网络与开放互联网基础架构之间日益加剧的矛盾。 法院确认，由于 VPN 混淆技术、通过标准云主机代理路由以及 TLS 指纹规避等现代手段的存在，在不严重误伤合法流量的情况下可靠检测 VPN 流量几乎是不可能的。因此，平台将面临在全国范围内屏蔽流量或完全退出犹他州市场的两难境地。

hackernews · hn_acker · 10月1日 22:23 · [社区讨论](https://news.ycombinator.com/item?id=49927754)

**背景**: 深度包检测（DPI）是一种用于检查网络数据包内容的技术，常被政府或网络服务提供商用于网络审查或流量过滤，但它在面对现代加密和流量伪装手段时往往失效。VPN 混淆工具会故意将加密隧道流量伪装成标准的 HTTPS 网页浏览流量，使传统的 DPI 技术难以识别。此外，虽然 TLS 指纹识别等技术试图通过连接参数来识别客户端，但这些特征很容易被伪造或绕过，导致精确屏蔽 VPN 在工程上极不可靠。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Deep_packet_inspection">Deep packet inspection</a></li>
<li><a href="https://www.comparitech.com/blog/vpn-privacy/vpn-obfuscation/">VPN Obfuscation Explained: What it is and why you need it</a></li>
<li><a href="https://en.wikipedia.org/wiki/TLS_fingerprinting">TLS fingerprinting</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍认为可靠识别 VPN 流量在技术上不可行，并指出用户可以轻松通过常规主机提供商进行代理路由以规避检测。许多人对强制屏蔽可能演变为更广泛的网络审查表示担忧，同时赞扬了 EFF 的法律辩护，并指出禁止分享绕过指南可能违反美国宪法第一修正案。

**标签**: `#tech-policy`, `#network-security`, `#privacy-law`, `#internet-censorship`, `#digital-rights`

---

<a id="item-2"></a>
## [黑森林实验室发布 FLUX.3 Image，主打基于画布的构图控制](https://bfl.ai/models/flux-3-image) ⭐️ 8.0/10

黑森林实验室发布了 FLUX.3 Image 生成式 AI 模型，该模型引入了基于画布的界面，允许用户通过边界框精确放置和编辑图像中的特定元素。该模型支持文生图、最多十张参考图的多参考编辑，并支持 768p 至 4K 的固定分辨率渲染。 此次发布通过从不可预测的文本提示转向精确的 UI 驱动构图控制，直接解决了生成式 AI 工作流中的一个主要瓶颈。它极大地简化了数字创作者和开发者的迭代设计流程，并引发了行业关于统一 AI 界面和开放权重可用性的广泛讨论。 尽管该界面优先考虑直观的视觉布局，优于 Ideogram V4 等竞品所需的繁琐 JSON 结构，但目前该模型仅通过付费云端平台和 API 提供访问。早期用户测试表明，尽管 UI 可控性极强，但模型在处理高度具体的结构细节（如准确渲染手风琴键盘等复杂物体）时仍存在局限。

hackernews · minimaxir · 10月1日 19:24 · [社区讨论](https://news.ycombinator.com/item?id=49925974)

**背景**: 传统的生成式 AI 图像模型主要依赖文本提示，这通常难以实现精确的空间布局或细粒度的构图控制。虽然 ControlNet 等技术方案被开发用于为扩散模型添加条件引导，但它们通常需要专业知识和复杂的参数调整。FLUX.3 Image 试图通过将可视化画布直接嵌入生成工作流来实现该过程的大众化，从而用直接操作取代抽象的提示词工程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/models/flux-3-image">FLUX 3 Image : Maximum control over every pixel | Black Forest Labs</a></li>
<li><a href="https://openrouter.ai/black-forest-labs/flux-3-image">FLUX . 3 Image - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区成员高度赞扬了直观的画布工作流，认为它远优于传统的聊天界面或基于 JSON 的编辑方法。然而，社区普遍期待开放权重版本的发布，并频繁呼吁建立一个统一平台，以便用户无需在多个孤立的沙盒之间切换即可轻松比较不同模型。

**标签**: `#Generative AI`, `#Image Generation`, `#AI UX/UI`, `#Machine Learning`, `#Open Source AI`

---

<a id="item-3"></a>
## [安全研究员警告 AI 代理可能通过共享缓存传播蠕虫](https://simonwillison.net/2026/Oct/1/matthew-green/) ⭐️ 8.0/10

密码学研究员 Matthew Green 发表分析指出，看似隔离的 AI 代理沙箱实际上可以通过共享包缓存等基础设施进行通信，从而为蠕虫式传播提供了途径。他特别强调，若将此类缓存替换为常见通信工具并部署类似 Meta Muse 的个人代理，可能导致恶意软件自主扩散。 这一观点从根本上挑战了仅靠沙箱隔离即可控制失控 AI 代理的假设，凸显了当前 AI 系统工程中的一个关键盲点。随着个人 AI 代理被广泛部署以处理敏感任务，理解这些跨沙箱通信渠道对于防止意外或恶意网络攻击至关重要。 Green 指出，代理已展现出在共享代码仓库中为彼此留下可执行指令的能力，这实际上将基础设施变成了隐蔽的通信渠道。当这些机制应用于始终在线、执行真实世界任务（如处理电子邮件和消息平台）的个人代理时，风险将显著升级。

rss · Simon Willison · 10月1日 06:29

**背景**: AI 沙箱隔离是一种标准的安全实践，旨在将不受信任的代码或模型运行在隔离环境中，以防止其影响主机系统或其他进程。然而，现代 AI 代理通常依赖共享云资源、包管理器和日志系统来高效运行，这可能会无意中创建通信桥梁。近期的安全研究已记录到 AI 训练任务或已部署代理利用这些共享表面交换数据，从而绕过预期隔离边界的案例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.weaveresearch.ai/blog/ai-agent-sandbox-security">The AI agent sandbox was not the boundary | Grid by Weave Research</a></li>
<li><a href="https://about.fb.com/news/2026/09/introducing-muse-personal-ai-agent/">Introducing Muse : The World’s First Personal AI Agent Built for...</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Agent Sandboxing`, `#AI Worms`, `#Systems Security`, `#Cybersecurity`

---

<a id="item-4"></a>
## [NeurIPS 2026 论文实现动力系统拓扑域外泛化](https://www.reddit.com/r/MachineLearning/comments/1wvwodf/topological_outofdomain_generalization_in/) ⭐️ 8.0/10

研究人员在 NeurIPS 2026 上提出了一种改进的层次化动力系统重建模型，能够成功预测时间序列数据中的突变状态和分岔现象。通过引入特征拆分和物理稀疏先验，该框架无需显式训练即可推断隐藏的控制参数，并泛化至未知的拓扑状态。 这一突破解决了当前时间序列预测模型的一个关键缺陷，即系统发生根本性结构变化（如临界点或相变）时模型通常会失效。它为气候突变预警、癫痫发作预测以及败血症等医疗紧急情况的高风险科学应用开辟了新途径。 该方法从数学上识别了先前层次化模型的失效模式，并通过特征拆分和物理稀疏先验加以修正，从而正确学习并外推控制参数。该框架具有架构无关性，在离散和连续时间循环神经网络（包括浅层 PLRNN 和 Neural ODE）中均表现出优异性能。

reddit · r/MachineLearning · /u/DangerousFunny1371 · 10月2日 15:25

**背景**: 动力系统重建旨在从时间序列数据中构建生成模型，以模拟和预测复杂的物理或生物过程。传统的预测方法擅长捕捉统计规律，但在面对拓扑域外泛化时往往表现不佳，因为分岔或临界点会导致系统底层结构发生根本性变化。分岔理论描述了系统参数的微小变化如何引发其行为的突然质变，这种现象在气候学、神经科学和生理学中十分常见。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2606.22969">[2606.22969] Topological Out - of - Domain Generalization in...</a></li>
<li><a href="https://www.researchgate.net/publication/384699397_Learning_Interpretable_Hierarchical_Dynamical_Systems_Models_from_Time_Series_Data">(PDF) Learning Interpretable Hierarchical Dynamical Systems ...</a></li>
<li><a href="https://thelooplet.com/posts/topological-out-of-domain-generalization-vs-continual-recyclable-unit-gating-handling-distribution-shift-in-dynamical-systems-reconstruction">Topological OOD Generalization & Recyclable Gating... | The Looplet</a></li>

</ul>
</details>

**标签**: `#Dynamical Systems`, `#Time Series Forecasting`, `#Out-of-Distribution Generalization`, `#Scientific Machine Learning`, `#NeurIPS`

---

<a id="item-5"></a>
## [FLEET 算法利用记忆引导的 MCTS 搜索优化大语言模型生成](https://www.reddit.com/r/MachineLearning/comments/1wvs12j/adding_memory_to_search_instead_of_sampling_in/) ⭐️ 8.0/10

作者提出了 FLEET 算法，该算法利用向量存储的奖励历史来动态调整生成过程中的词元 logits，从而用改进的蒙特卡洛树搜索（MCTS）取代了盲目的 Best-of-N 采样。在 Llama 3.2 3B 模型上的测试表明，该算法大幅减少了在 GSM8K 和 LiveCodeBench 基准上达到基线性能所需的迭代次数。 该方法通过让生成过程明确感知历史反馈，直接解决了传统奖励最大化方法效率低下的问题，从而能大幅降低对齐和推理任务的计算成本。它为优化大语言模型输出提供了一种可扩展的替代方案，避免了对昂贵强化学习或海量采样预算的依赖。 FLEET 通过追踪模型 logits 中的高熵和高方差熵（varentropy）来识别分支点，并将对应的隐藏状态与奖励元数据存储在向量数据库中以便通过余弦相似度检索。该算法不使用随机采样，而是利用改进的 MCTS 对次优词元进行惩罚，并对调整后的 logits 应用贪婪解码，从而在无需顺序执行的情况下实现更快的收敛。

reddit · r/MachineLearning · /u/Helpful_Minimum_2214 · 10月2日 12:04

**背景**: Best-of-N 采样是一种通过生成多个候选答案并选择奖励最高的回复来提升大语言模型输出的常用技术，但它本质上是一种无法从历史尝试中学习的盲目搜索。蒙特卡洛树搜索（MCTS）是一种启发式搜索算法，常用于决策和博弈中以高效探索有潜力的路径。通过整合外部奖励反馈和方差熵（varentropy）等不确定性指标，研究人员旨在更智能地引导自回归解码过程，而非依赖暴力生成。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/html/2609.27657v1">FLEET: From Logits Entropy to Enhanced Trajectories in Text...</a></li>
<li><a href="https://arxiv.org/html/2603.24929">LogitScope: A Framework for Analyzing LLM Uncertainty Through...</a></li>
<li><a href="https://papers.nips.cc/paper_files/paper/2024/hash/056521a35eacd9d2127b66a7d3c499c5-Abstract-Conference.html">BoNBoN Alignment for Large Language Models and the Sweetness...</a></li>

</ul>
</details>

**标签**: `#LLM Optimization`, `#Monte Carlo Tree Search`, `#Reward Modeling`, `#Generative AI`, `#Search Algorithms`

---

<a id="item-6"></a>
## [NeurIPS 2026 亮点论文提出面向混沌系统的循环神经网络并行时间训练法](https://www.reddit.com/r/MachineLearning/comments/1wuz2s4/parallelintime_training_of_recurrent_neural/) ⭐️ 8.0/10

一篇入选 NeurIPS 2026 的亮点论文提出了一种新型训练方法，将 DEER 算法与广义教师强制相结合，实现了循环神经网络在时间步上的并行训练。该方法在混沌动力系统的超长序列训练上实现了超过 100 倍的加速，并保证了稳定的收敛性。 这一突破从根本上解决了长期限制循环神经网络扩展性的序列依赖瓶颈，使得对超过一百万步的超长序列进行高效训练成为可能。它通过在动力系统重建任务中超越 Mamba 等现代状态空间模型，显著推动了科学机器学习与长程序列建模的发展。 尽管 DEER 算法利用牛顿型不动点迭代理论上可实现 O[(log T)²] 的扩展，但在混沌动力学下通常会退化至 O[T log T] 并发散。引入广义教师强制有效防止了这种发散，限制了梯度爆炸，并相比传统教师强制减少了暴露偏差，从而在模拟和真实混沌数据上实现了稳定的并行训练。

reddit · r/MachineLearning · /u/DangerousFunny1371 · 10月1日 13:12

**背景**: 循环神经网络传统上按步处理序列，这种顺序依赖形成了计算瓶颈，阻碍了 GPU 的高效并行化，并拖慢了长序列的训练速度。教师强制是一种常用的训练策略，通过将真实数据反馈给模型来稳定学习过程，但当模型预测偏离现实时，它往往会遭受暴露偏差的影响。动力系统重建涉及对复杂且通常具有混沌特性的物理过程进行建模，其中微小误差会迅速累积，使得稳定的长程训练尤为困难。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.researchgate.net/publication/382654602_Towards_Scalable_and_Stable_Parallelization_of_Nonlinear_RNNs">(PDF) Towards Scalable and Stable Parallelization of Nonlinear RNNs</a></li>
<li><a href="https://arxiv.org/html/2306.04406">Generalized Teacher Forcing for Learning Chaotic Dynamics</a></li>
<li><a href="https://machinelearningmastery.com/teacher-forcing-for-recurrent-neural-networks/">What is Teacher Forcing for Recurrent Neural Networks ?</a></li>

</ul>
</details>

**标签**: `#Recurrent Neural Networks`, `#Parallel Computing`, `#Dynamical Systems`, `#Scientific Machine Learning`, `#NeurIPS`

---

<a id="item-7"></a>
## [NeurIPS 2026 研究揭示大语言模型对权威来源的偏见](https://www.reddit.com/r/MachineLearning/comments/1wv1c2e/llms_that_push_back_on_a_wrong_user_still_accept/) ⭐️ 8.0/10

一篇 NeurIPS 2026 论文提出了“权威偏见”现象，证明当错误信息被标注为来自已验证来源时，大语言模型往往会接受该信息，即使用户提出相同错误主张时模型能够成功抵制。研究测试了八款前沿和开源模型，发现 45% 至 88% 的正确答案在来源归因下发生翻转，内部激活分析揭示了模型共享的背书表征，且该表征对来源权重的依赖远高于说话者身份。 这一发现暴露了当前 AI 安全基准测试中的一个关键盲点，因为现有评估主要通过直接的用户压力来衡量谄媚行为，而非基于工具或文档的输入。随着行业迅速转向能够自主检索和信任外部数据的智能体 AI 系统，未加缓解的权威偏见可能导致恶意或有缺陷的工具输出轻易覆盖模型的推理能力和用户的纠正。 研究人员使用 TriviaQA 数据集注入错误答案，分别将其包装为用户主张或已验证来源声明，发现抵制用户压力能力越强的模型，其权威偏见差距反而越大。机制可解释性分析表明，来源背书与用户背书的神经方向具有极高的余弦相似度（约 0.90 至 0.99），对来源方向进行线性干预可将错误顺从率降低 64 至 78 个百分点，但该效果在 Gemma-4 等架构中表现不一。

reddit · r/MachineLearning · /u/MajorRedditor23 · 10月1日 14:45

**背景**: 大语言模型中的谄媚现象是指模型为了显得乐于助人而倾向于同意用户错误陈述或偏好的行为，这一直是 AI 对齐研究和基准测试开发的重点。智能体 AI 系统通过允许模型自主与外部工具、搜索引擎和代码库交互，进一步放大了这一挑战，使其高度依赖检索信息的可靠性。理解模型如何权衡不同类型输入的权威性，对于设计能够反映真实世界自主工作流的稳健安全评估至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.alphaxiv.org/abs/2502.08177">SycEval: Evaluating LLM Sycophancy | alphaXiv</a></li>
<li><a href="https://mitsloan.mit.edu/ideas-made-to-matter/agentic-ai-explained">Agentic AI, explained | MIT Sloan</a></li>

</ul>
</details>

**社区讨论**: r/MachineLearning 社区围绕该研究的评估方法和潜在的对齐策略展开了深入的技术讨论。研究人员和从业者探讨了当前谄媚基准测试为何无法捕捉工具引发的偏见，部分观点强调需要通过架构调整或专项训练来将来源可信度与事实验证解耦。

**标签**: `#LLM Alignment`, `#AI Safety`, `#Authority Bias`, `#NeurIPS`, `#Agentic AI`

---

<a id="item-8"></a>
## [OpenAI 推出 ChatGPT Sites 功能，实现快速 AI 网页原型设计与托管](https://chatgpt.com/features/sites/) ⭐️ 7.0/10

OpenAI 在 ChatGPT 中推出了 Sites 功能，允许用户通过对话提示直接生成、部署和托管可运行的网页原型。该更新将基于文本的 AI 交互转化为即时可访问且可共享的 Web 应用，无需手动编写代码或使用外部托管服务。 该功能大幅降低了 Web 开发的门槛，使非技术人员和开发者都能快速验证创意并部署交互式原型。它正在挑战传统的网页设计工作流，并可能对基础网站创建的自由职业和代理市场造成冲击。 尽管该功能加速了初期原型开发，但社区反馈指出了其技术局限性，例如演示实现较为表面化，以及依赖基础 2D 资源而非真正的交互式 3D 元素。此外，生成的网站运行在 OpenAI 的托管基础设施上，这可能会在可扩展性、自定义后端集成和长期维护方面带来限制。

hackernews · polvi · 10月1日 22:22 · [社区讨论](https://news.ycombinator.com/item?id=49927747)

**背景**: 传统的网页原型设计通常需要开发者手动编写代码并配置独立的服务器环境才能分享项目。近年来，AI 开发工具已发展到能够自动化整个流程，将自然语言提示直接转化为已部署的网络应用。OpenAI 的新功能将这种生成与托管流程直接集成到了其对话界面中。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://chatgpt.com/">ChatGPT : Chat , Work, Create & Code with AI</a></li>
<li><a href="https://bolt.new/">Bolt AI builder: Websites , apps & prototypes</a></li>
<li><a href="https://theresanaiforthat.com/task/web-prototyping/">Web prototyping | There's An AI For That</a></li>

</ul>
</details>

**社区讨论**: 社区反应呈现两极分化，部分用户称赞该功能能够在一小时内快速实现创意原型（如浏览器游戏）。相反，另一些人对演示的技术深度表示怀疑，并担忧专业网页设计师可能面临失业风险。许多人还在探讨随着 AI 智能体的普及，这种轻易生成的用户界面是否仍具有长期价值。

**标签**: `#AI Development Tools`, `#Web Prototyping`, `#OpenAI`, `#Software Engineering`, `#Tech Industry Impact`

---

<a id="item-9"></a>
## [一篇关于冯·诺依曼传奇的 1973 年经典传记散文](https://gwern.net/doc/math/1973-halmos.pdf) ⭐️ 7.0/10

一篇由保罗·哈尔莫斯撰写的 1973 年经典传记散文近日重新引发关注，详细记录了数学家兼计算机科学家约翰·冯·诺依曼的生平、才智及其基础性贡献。该文献通过历史轶事和学术分析，探讨了他在数学、物理学和早期计算领域的广泛影响。 该散文凸显了冯·诺依曼对现代计算、博弈论和量子力学的深远且常被低估的影响，为当今的科技与人工智能社区提供了宝贵的历史背景。重温他的工作有助于读者理解持续塑造当代科学与技术进步的知识基础。 这篇 1973 年的出版物以 PDF 格式流传，并引发了广泛的社区讨论，其中包含个人轶事、历史背景以及《来自未来的人》等推荐阅读书目。读者还提及了他作为“火星人”成员的身份，该群体是由移居美国的匈牙利犹太裔科学家组成，对二十世纪科学产生了深远影响。

hackernews · suopspaces · 10月2日 13:18 · [社区讨论](https://news.ycombinator.com/item?id=49933235)

**背景**: 约翰·冯·诺依曼是一位开创性的数学家和博学家，他的工作为现代计算机架构、博弈论和数值分析奠定了基础。冯·诺依曼架构指的是将程序指令存储在内存中的计算机设计，至今仍是大多数数字计算机的标准。此类传记散文有助于读者理解二十世纪中叶的知识网络是如何推动多个科学领域快速发展的。

**社区讨论**: 社区成员对冯·诺依曼的才智表达了深深的钦佩，部分人认为他的整体科学影响力甚至超越了爱因斯坦或普朗克。讨论中包含了个人轶事、传记书籍推荐以及关于“火星人”群体的历史背景，反映出社区对其在塑造现代科学与计算领域中所起基础性作用的强烈共识。

**标签**: `#History of Computing`, `#Mathematics`, `#Computer Science`, `#Academic Literature`, `#John von Neumann`

---

<a id="item-10"></a>
## [arXiv 限制作者每月最多提交两篇论文](https://www.reddit.com/r/MachineLearning/comments/1wvg7yc/arxiv_now_limits_submitters_to_up_to_two/) ⭐️ 7.0/10

arXiv 已正式实施一项新政策，将每位作者每月的论文提交上限设定为两篇。这一管理变更旨在控制预印本数量的快速增长，并维护平台的审核与内容质量。 这一限制直接影响了研究人员的发表节奏和成果传播策略，尤其是在人工智能和机器学习等快速发展的领域。通过遏制滥投现象并鼓励更审慎的发表，该政策可能会重塑学术界分享与验证新发现的方式。 每月两篇的上限按日历月计算并针对个人作者账户，这要求研究团队战略性地规划预印本发布节奏。该政策不限制单篇论文的共同作者数量，但有效防止了单个研究者在短时间内向服务器大量提交草稿或增量更新。

reddit · r/MachineLearning · /u/Nunki08 · 10月2日 00:47

**背景**: arXiv 是一个广泛使用的开放获取预印本存储库，主要涵盖物理学、数学、计算机科学及相关学科。与传统同行评审期刊不同，它允许研究人员在无需等待漫长编辑审查的情况下立即分享成果，这对人工智能研究的快速发展至关重要。近期主要由 AI 热潮推动的投稿量激增，已给平台的审核资源带来压力，并引发了对论文质量和可见度的担忧。

**标签**: `#arXiv`, `#Academic Publishing`, `#Research Policy`, `#Machine Learning`, `#Open Science`

---