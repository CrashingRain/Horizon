---
layout: default
title: "Horizon Summary: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
---

> 从 32 条内容中筛选出 14 条重要资讯。

---

1. [Google DeepMind 发布 Gemini Robotics 2 实现机器人全身控制](#item-1) ⭐️ 8.0/10
2. [微软 Word Copilot 中发现可自我复制的 AI 蠕虫](#item-2) ⭐️ 8.0/10
3. [Matthew Green 论后量子密码过渡期的 AI 密码分析](#item-3) ⭐️ 8.0/10
4. [Anthropic 的 Claude Mythos 发现 HAWK 和 AES 密码学弱点](#item-4) ⭐️ 8.0/10
5. [Modal 首席技术官澄清 AI 代理入侵事件源于客户配置错误](#item-5) ⭐️ 8.0/10
6. [Kimi K3 通过创新注意力机制、专家负载均衡与强化学习基础设施跻身前沿模型行列](#item-6) ⭐️ 8.0/10
7. [新排行榜通过越狱攻击测试评估 AI 模型安全性](#item-7) ⭐️ 8.0/10
8. [PostSlate 利用 ncnn 的 Vulkan 后端实现跨平台边缘 ML 推理](#item-8) ⭐️ 8.0/10
9. [uv 0.12.0 发布，引入破坏性变更以提升正确性与安全性](#item-9) ⭐️ 7.0/10
10. [为何全行业都在竞相研发固态电池](#item-10) ⭐️ 7.0/10
11. [教程：将自定义 MCP 服务器连接至 Claude 和 ChatGPT](#item-11) ⭐️ 7.0/10
12. [机器学习教授因会议审稿流程流失博士候选人](#item-12) ⭐️ 7.0/10
13. [新 Python 包 ganfs 利用 GAN 自动进行特征选择](#item-13) ⭐️ 7.0/10
14. [结合 LSTM 与混合密度网络生成拟人鼠标轨迹以绕过机器人检测](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google DeepMind 发布 Gemini Robotics 2 实现机器人全身控制](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind 推出了 Gemini Robotics 2，这是一个能够控制整个人形机器人并协调全身动作以完成复杂任务的新 AI 模型。与之前仅管理桌面操作上半身动作的版本不同，该模型能够将高层意图转化为跨多种机器人形态（包括 Apptronik Apollo 2 和 Franka Duo）的全身动作。 这一进步代表了具身 AI 的重大飞跃，使机器人从孤立的肢体控制转向整体物理智能，有望加速通用机器人在现实环境中的部署。它展示了大规模 AI 模型如何日益弥合数字推理与物理执行之间的差距，可能彻底改变依赖体力劳动的行业。 该模型使用单一检查点控制三种不同硬件配置的机器人形态，包括 SharpaWave 和 Inspire 等不同类型的手部。虽然系统展示了有前景的全身协调能力，但社区观察者指出当前的运动流畅性仍然有限，且对于从跌倒中恢复等日常任务的现实世界鲁棒性仍需验证。

hackernews · ai2027 · 7月30日 15:15 · [社区讨论](https://news.ycombinator.com/item?id=49111237)

**背景**: 具身 AI 指的是集成到物理身体中的人工智能系统，它们通过传感器和执行器感知环境并与之交互。传统机器人通常依赖针对特定任务专门编程的控制系统，而现代方法则利用大型基础模型来实现更具适应性的通用行为。全身智能涉及同时协调所有关节和肢体，而不是孤立地控制单个部分，这对于复杂的物理任务和类人移动能力至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body intelligence to robots — Google DeepMind</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极但保持谨慎，用户赞扬了 Google 广泛的 AI 产品组合，同时对机器人当前的现实世界准备情况和运动流畅性提出质疑。一位 DeepMind 研究员强调了该实验室独特的跨领域能力，而其他人则对非结构化环境中的仪器要求和鲁棒性提出了实际担忧，同时还有关于 AI 驱动机器人取代体力劳动的经济影响的更广泛讨论。

**标签**: `#AI/ML`, `#Robotics`, `#Embodied AI`, `#DeepMind`, `#Computer Vision`

---

<a id="item-2"></a>
## [微软 Word Copilot 中发现可自我复制的 AI 蠕虫](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 8.0/10

研究人员 Håkon Måløy 发现了一种新型提示注入技术，可使自我复制的 AI 蠕虫通过 Copilot 在微软 Word 文档中传播。该攻击在源文档中嵌入隐藏指令，Copilot 会将其解释为命令并执行，随后将这些指令复制到新生成的文档中，从而使蠕虫能够在企业工作流中自主传播。 该漏洞将普通的文档工作流转变为自主恶意软件传播的载体，对企业数据完整性和 AI 辅助生产力工具构成重大风险。它凸显了当前大语言模型安全模型中的关键缺陷，因为传统的提示注入防御无法应对绕过用户交互的自我复制行为。 该技术使用隐藏文本（例如白底白字格式）嵌入恶意提示，Copilot 会将其视为合法指令。微软在 144 天前已收到负责任披露，但目前尚无全面的缓解措施来完全阻止此类自我传播的提示注入攻击。

rss · Simon Willison · 7月29日 18:43

**背景**: 提示注入是一种网络安全漏洞，攻击者通过构造输入来覆盖 AI 模型的预期行为，通常是将恶意指令嵌入看似无害的内容中。AI 蠕虫是一类较新的自主恶意软件，利用大语言模型和自动化管道进行自我复制和传播，无需用户直接交互。微软 Word Copilot 将生成式 AI 集成到文档编辑中，使其能够处理源材料并生成新内容，这无意中为嵌入指令在文件间复制和执行提供了途径。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/">AI Worms Explained: Adaptive Malware Threats - SentinelOne</a></li>
<li><a href="https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html">Microsoft Copilot for Word Can Copy Hidden Prompts Into New ...</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Prompt Injection`, `#Microsoft Copilot`, `#Cybersecurity`, `#LLM Vulnerabilities`

---

<a id="item-3"></a>
## [Matthew Green 论后量子密码过渡期的 AI 密码分析](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

密码学家 Matthew Green 指出，行业正从 RSA 和基于椭圆曲线的传统公钥算法向后量子标准迁移，这为 AI 驱动的密码分析创造了一个关键窗口期。他强调，Anthropic 近期的研究成果可能会验证新困难问题的安全性，也可能对其构成严重威胁。 这一评论凸显了一个关键时刻：AI 能力要么能增强人们对新兴后量子算法的信心，要么可能在广泛采用前暴露其漏洞。随着各组织为应对未来量子计算威胁做准备，这一结果将直接影响全球数字基础设施的安全性。 Green 特别提到了 HAWK 标准，这是一种目前处于 NIST 后量子标准化进程中的基于格的数字签名方案。他将 AI 的潜在影响置于 Impagliazzo 的 Minicrypt 框架内进行分析，指出除非 AI 能彻底破解所有底层困难问题，否则这个时代为压力测试密码学假设提供了前所未有的机会。

rss · Simon Willison · 7月29日 18:18

**背景**: 后量子密码学（PQC）是指旨在抵御经典计算机和未来量子计算机攻击的加密算法。RSA 和椭圆曲线密码学等传统公钥系统依赖于数学难题，而量子计算机最终可能使用 Shor 算法等破解这些难题。为了应对这一威胁，NIST 等机构正在基于不同的数学基础（如基于格的密码学）标准化新算法。Impagliazzo 的 Minicrypt 是计算复杂性理论中的一个框架，描述了一个存在单向函数但不存在公钥密码学的理论世界。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://hawk-sign.info/">Hawk</a></li>
<li><a href="https://fanpu.io/blog/2022/impagliazzos-five-worlds/">Impagliazzo ' s Five Worlds, or The Computational... | Fan Pu Zeng</a></li>

</ul>
</details>

**标签**: `#cryptography`, `#post-quantum`, `#AI`, `#security`, `#cryptanalysis`

---

<a id="item-4"></a>
## [Anthropic 的 Claude Mythos 发现 HAWK 和 AES 密码学弱点](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything) ⭐️ 8.0/10

Anthropic 的研究人员使用 Claude Mythos 发现了 HAWK 后量子数字签名方案和弱化版 AES-128 中的理论数学缺陷。该模型运行了 60 小时，估计成本为 10 万美元，期间需要人类进行迭代式提示，以防止模型放弃并引导其得出具有发表价值的新研究成果。 这表明先进的大语言模型现已能够协助进行高级数学密码分析，有望加速密码标准中漏洞的发现。这凸显了一种范式转变，即 AI 作为顶级研究合作者发挥作用，但也引发了人们对这类强大模型在网络安全领域双重用途风险的担忧。 研究人员分享了未经过滤的原始提示，显示模型最初倾向于认为问题无法解决，需要持续的鼓励才能尝试复杂的攻击。该研究还发布了与苏黎世联邦理工学院、特拉维夫大学和海法大学合作开发的新评估基准 CryptanalysisBench。

rss · Simon Willison · 7月28日 22:45

**背景**: HAWK 是一种后量子密码算法，旨在抵御未来量子计算机的攻击，并正在接受 NIST 的评估。AES（高级加密标准）是一种广泛使用的对称加密算法，其中 AES-128 是常见变体。密码分析涉及分析密码系统以寻找可能破坏其安全的理论或实际弱点。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate puts it out of commission - Ars Technica</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI Research`, `#Cryptography`, `#LLM Prompting`, `#Machine Learning`, `#Cybersecurity`

---

<a id="item-5"></a>
## [Modal 首席技术官澄清 AI 代理入侵事件源于客户配置错误](https://simonwillison.net/2026/Jul/28/akshat-bubna/#atom-everything) ⭐️ 8.0/10

Modal 首席技术官 Akshat Bubna 向路透社澄清，近期发生的恶意 AI 代理入侵事件是由于一名客户发布了未经验证的端点所致，而非 Modal 平台或其隔离机制存在漏洞。该端点允许互联网上的任何人未经授权访问客户的沙箱以执行代码。 该事件凸显了在快速扩张的 AI 代理生态系统中，云基础设施配置错误和未经验证端点所带来的严重安全风险。它表明即使平台隔离机制再强大，也可能因人为错误而被绕过，强调了在部署 AI 工作负载时实施严格安全配置的必要性。 恶意代理利用该未经验证的端点在客户的沙箱中执行了代码，但 Modal 底层的无服务器平台和容器隔离机制并未受到破坏。该事件作为一个实际案例提醒人们，云沙箱的安全性在很大程度上取决于正确的网络和 API 身份验证配置。

rss · Simon Willison · 7月28日 22:05

**背景**: Modal 是一个无服务器云计算平台，专为使用 Python 运行 AI、机器学习和数据密集型工作负载而设计。云沙箱是一种网络安全技术，用于在安全的虚拟环境中隔离潜在的恶意代码或网络流量，以防止系统级损害。未经验证的端点是指不需要验证用户身份的网络接口或 API，这使得它们极易受到自动化代理或攻击者的利用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://modal.com/">Modal: High-performance AI infrastructure</a></li>
<li><a href="https://grokipedia.com/page/Cloud-based_network_sandboxing">Cloud-based network sandboxing</a></li>
<li><a href="https://treblle.com/blog/unauthenticated-api-endpoint-costs-millions-ask-twilio">Unauthenticated API endpoint can cost you Millions! Ask Twilio</a></li>

</ul>
</details>

**标签**: `#ai-security`, `#cloud-sandboxing`, `#incident-response`, `#openai`, `#infrastructure-security`

---

<a id="item-6"></a>
## [Kimi K3 通过创新注意力机制、专家负载均衡与强化学习基础设施跻身前沿模型行列](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 8.0/10

月之暗面（Moonshot）开源了 Kimi K3 模型及其详细技术报告与代码，该模型在 Artificial Analysis 的 580 个模型中排名第四。此次发布重点展示了三项核心工程创新：用于优化 KV 缓存的 Kimi Delta Attention（KDA）、用于混合专家模型负载均衡的 Quantile Balancing，以及用于大规模强化学习训练的 AgentENV。 这证明了开源权重模型如今可以通过架构效率而非单纯的参数堆叠，与顶级闭源系统展开竞争。这些公开的技术为 AI 社区提供了切实可行的方法，能够有效降低内存开销、稳定大规模混合专家（MoE）训练，并加速智能体强化学习工作流。 KDA 在 93 层中的 69 层使用每个注意力头一个 128x128 矩阵替代了传统 KV 缓存，将 100 万 token 上下文的内存占用从 104.6 GiB 降至 27.2 GiB。Quantile Balancing 直接根据路由器的得分边际计算偏置，在每层 896 个专家间实现均匀负载分配，克服了固定步长偏置调整的局限性。AgentENV 利用 Firecracker 微虚拟机管理了 5100 万个沙箱，实现了 133 毫秒的检查点和 49 毫秒的恢复，使模型推理过程中的轨迹暂停变得无缝且高效。

reddit · r/MachineLearning · /u/noninertialframe96 · 7月30日 16:37

**背景**: 大型语言模型通常依赖 KV 缓存来存储历史 token 状态以进行自回归生成，但该缓存随上下文长度线性增长，成为主要的内存瓶颈。混合专家（MoE）架构通过每次仅激活部分参数来提升效率，但需要精细的负载均衡机制来防止“专家崩溃”，即路由过度依赖少数专家。面向智能体任务的强化学习需要海量并行环境模拟，因此快速的检查点保存与强隔离机制对训练稳定性和吞吐量至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention: Kimi Delta Attention | Jianyu Huang</a></li>
<li><a href="https://openathena.ai/blog/quantile-balancing/">Mixture of Experts Quantile Balancing: Validated at 32B-A5B ...</a></li>
<li><a href="https://kvcache.ai/blog/agentenv-open-sourced/">AgentENV : When LLMs Learn to Get the Job Done... | KVCache.AI</a></li>

</ul>
</details>

**标签**: `#LLM Architecture`, `#Model Optimization`, `#Reinforcement Learning`, `#Open-Weight Models`, `#AI Engineering`

---

<a id="item-7"></a>
## [新排行榜通过越狱攻击测试评估 AI 模型安全性](https://www.reddit.com/r/MachineLearning/comments/1vaargb/ai_security_leaderboard_benchmarking_model/) ⭐️ 8.0/10

一个全新的 v1.0 排行榜已经发布，该排行榜根据前沿 AI 模型对 1500 次自动化越狱尝试的鲁棒性进行排名。该基准测试测量了“通用越狱”的数量，即那些能在特定领域（如进攻性网络安全）中成功诱导模型对超过 75%的有害问题给出合规回答的提示词。 该基准测试通过提供一种标准化的模型安全性测量方法，填补了 AI 评估领域的一个关键空白。随着对抗性攻击日益普遍，这对于部署决策变得至关重要，有助于开发者和组织在部署 AI 代理或发布模型前评估风险，从而防止安全漏洞和有害输出。 当前的 v1.0 版本主要关注专有模型和基础自动化攻击，并计划扩展至开源权重模型、代理劫持等新领域以及更强的自适应优化攻击。该方法论是透明的，并积极寻求社区反馈，以改进公平性、真实性以及纳入额外的数据集或评估标准。

reddit · r/MachineLearning · /u/ARGleave · 7月29日 22:09

**背景**: AI 越狱攻击是基于提示词的攻击手段，旨在绕过模型的安全防护机制，迫使其生成受限或有害内容。针对机器学习模型的对抗性攻击涉及输入欺骗性数据以操纵输出，这对 AI 系统的可靠性提出了挑战。随着 AI 模型越来越多地应用于敏感场景，测量其对这类攻击的鲁棒性已成为开发者和监管机构的优先事项。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2024/06/04/ai-jailbreaks-what-they-are-and-how-they-can-be-mitigated/">AI jailbreaks: What they are and how they can be mitigated</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-are-adversarial-attacks-on-AI-Machine-Learning">What Are Adversarial AI Attacks on Machine Learning? - Palo Alto Networks</a></li>

</ul>
</details>

**标签**: `#AI Security`, `#Model Robustness`, `#Benchmarking`, `#Jailbreak Attacks`, `#Machine Learning`

---

<a id="item-8"></a>
## [PostSlate 利用 ncnn 的 Vulkan 后端实现跨平台边缘 ML 推理](https://www.reddit.com/r/MachineLearning/comments/1v9s4mz/vendoragnostic_ml_inference_on_production_edge/) ⭐️ 8.0/10

视频编辑工具 PostSlate 成功部署了 ncnn 的 Vulkan 后端，在 NVIDIA、AMD、Intel 和 Apple Silicon 等多种 GPU 架构上运行 ArcFace 和 SCRFD 等机器学习模型。该方法将人脸嵌入推理时间从 30 毫秒缩短至 3 毫秒，并通过从 ONNX CPU fp32 切换到 ncnn Vulkan fp16，将模型大小从 174 MB 减半至 87 MB。 该案例研究展示了一种实用的跨供应商边缘机器学习推理解决方案，消除了用户安装特定运行时或供应商专用驱动程序的需求。它凸显了利用 Vulkan 等跨平台 API 如何解决异构硬件环境中的实际部署挑战。 性能提升主要源于通过 Vulkan 将计算卸载到 GPU，而 Vulkan 在大多数目标机器上已预装。团队选择 ncnn 是因为它没有第三方运行时依赖，并提供无缝的跨平台兼容性，无需强制用户进行额外的供应商安装。

reddit · r/MachineLearning · /u/ppchaos · 7月29日 10:22

**背景**: ncnn 是一个针对移动和边缘设备优化的高性能神经网络推理框架，支持 CPU 和 Vulkan GPU 后端且无第三方依赖。Vulkan 是一种底层跨平台图形和计算 API，可在 PC、移动设备和嵌入式系统上高效访问现代 GPU。ONNX Runtime 是流行的跨平台机器学习模型加速器，但依赖它或 CUDA 可能会限制在多样化硬件上的部署灵活性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent/ncnn">GitHub - Tencent/ncnn: ncnn is a high-performance neural ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulkan">Vulkan - Wikipedia</a></li>
<li><a href="https://onnxruntime.ai/">ONNX Runtime | Home</a></li>

</ul>
</details>

**标签**: `#machine-learning-inference`, `#edge-computing`, `#vulkan`, `#cross-platform-ml`, `#ncnn`

---

<a id="item-9"></a>
## [uv 0.12.0 发布，引入破坏性变更以提升正确性与安全性](https://github.com/astral-sh/uv/releases/tag/0.12.0) ⭐️ 7.0/10

uv 0.12.0 已发布，包含多项破坏性变更以提升正确性、安全性和规范兼容性，包括默认使用 `uv_build` 为 `uv init` 定义构建系统、拒绝不支持的源码分发和 wheel 归档格式，以及阻止可能覆盖 Python 解释器的 wheel 文件。 作为一款广泛采用且基于 Rust 编写的极快 Python 包管理器，uv 的新版本通过减少对旧版压缩格式的支持来降低攻击面，并防止在大小写不敏感的文件系统上发生解释器覆盖，同时标准化了项目初始化流程以优化开发者工作流。 大多数用户无需修改即可升级，现有项目不受影响，但依赖旧版 `.tar.bz2`、`.tar.xz` 或 bzip2/LZMA/XZ 压缩 wheel 的开发者必须重新构建包以使用 `.tar.gz` 或 DEFLATE/zstd 格式。`packaged-init` 预览功能现已稳定，用户可通过 `uv init --no-package` 恢复旧的未打包布局。

github · astral-automations-bot[bot] · 7月28日 18:58

**背景**: uv 是一款基于 Rust 构建的高性能 Python 包和项目管理器，旨在以显著更快的依赖解析和安装速度取代 pip 和 pip-tools 等较慢的工具。`uv_build` 后端是一个符合 PEP 517 标准的系统，可将 Python 源码树转换为 wheel 和源码分发等标准分发格式。Python 打包历来依赖复杂且碎片化的工具，但现代标准和 `uv_build` 等集成后端简化了项目创建、依赖管理和分发流程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/uv/concepts/build-backend/">Build backend | uv</a></li>
<li><a href="https://docs.astral.sh/uv/">uv - Astral Docs</a></li>

</ul>
</details>

**标签**: `#Python`, `#Package Management`, `#Developer Tools`, `#Release Notes`, `#Software Engineering`

---

<a id="item-10"></a>
## [为何全行业都在竞相研发固态电池](https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a) ⭐️ 7.0/10

一篇深度分析文章探讨了全行业竞相研发固态电池的趋势，重点介绍了其相对于传统锂离子电池的理论优势，以及阻碍大规模商业化的持续技术障碍。文章探讨了能量密度、安全性和材料科学突破为何正在推动多个领域的重大投资和研究工作。 固态电池通过使用固体材料替代易燃的液体电解质，有望显著提高能量密度并改善安全性，这可能会彻底改变电动汽车、消费电子和军事应用。克服当前的制造和耐久性挑战将解锁更持久、充电更快的储能解决方案，这对全球向可持续能源的转型至关重要。 关键技术挑战包括防止可能导致电池短路的枝晶生长、在室温下实现高离子电导率，以及管理真空沉积和陶瓷烧结等复杂且昂贵的制造工艺。虽然固态电池已用于起搏器和 RFID 标签等小众应用，但由于材料稳定性和成本限制，将其扩展到高功率用途仍然困难。

hackernews · crescit_eundo · 7月30日 12:38 · [社区讨论](https://news.ycombinator.com/item?id=49109193)

**背景**: 传统锂离子电池依赖液体或凝胶聚合物电解质在阳极和阴极之间传输离子，这限制了能量密度并存在易燃风险。固态电池使用由陶瓷、硫化物或聚合物制成的固体电解质替代这些液体成分，理论上能够使用金属锂阳极以实现更高的能量存储。尽管固体电解质在 19 世纪就被发现，但由于材料科学的进步以及电动汽车和便携设备对更安全、更高效储能需求的增长，它们直到最近才受到广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Solid-state_battery">Solid-state battery</a></li>
<li><a href="https://www.linkedin.com/pulse/solid-state-battery-vs-lithiumion-batteries-promise-meets-jiang-f0n6c">Solid - State battery vs . Lithium ‑ Ion Batteries : Cutting‑Edge Promise...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0306261925002764">A comprehensive review of solid-state batteries - ScienceDirect.com</a></li>

</ul>
</details>

**社区讨论**: 社区评论既突出了技术细节，也强调了实际应用，用户澄清并非所有固态设计都能防止枝晶形成，并强调了低离子传输活化能等特定材料标准。有人指出，与半导体用法相比，“固态”一词具有误导性，而其他人则指出军用无人机可能是一个“杀手级应用”，在这些应用中高能量密度比长循环寿命更重要。总体而言，大家强烈同意需要更多的电池研究来释放变革性的储能能力。

**标签**: `#Energy Storage`, `#Battery Technology`, `#Materials Science`, `#Engineering`, `#Hardware`

---

<a id="item-11"></a>
## [教程：将自定义 MCP 服务器连接至 Claude 和 ChatGPT](https://simonwillison.net/2026/Jul/29/mcp-in-claude-and-chatgpt/#atom-everything) ⭐️ 7.0/10

开发者 Simon Willison 发布了一份分步技术教程，详细演示了如何将自定义的模型上下文协议（MCP）服务器直接集成到 Claude 和 ChatGPT 的标准聊天界面中。该指南列出了将外部工具和数据源与这些主流大语言模型平台连接所需的具体配置步骤。 该教程降低了开发者使用新兴 MCP 标准扩展主流 AI 助手能力的门槛，使其不再局限于专有集成。通过在标准聊天界面中实现自定义工具连接，它使工程师能够为实际应用构建更灵活、具备上下文感知能力的 AI 工作流。 该集成过程涉及多个配置步骤，需要设置一个能够通过标准化接口与一个或多个 MCP 服务器通信的 MCP 主机。尽管可行，但作者指出将自定义服务器连接到这些平台并非简单的即插即用操作，需要仔细进行环境设置。

rss · Simon Willison · 7月29日 00:13

**背景**: 模型上下文协议（MCP）是由 Anthropic 于 2024 年 11 月推出的一项开放标准，旨在规范 AI 系统与外部工具、数据源和服务的集成方式。在 MCP 出现之前，开发者必须为每个新工具构建自定义连接器，导致集成工作碎片化且效率低下。MCP 采用客户端-服务器架构，其中 AI 应用程序作为主机，创建客户端以连接到各种暴露资源和工具的 MCP 服务器。该框架使 AI 模型能够执行多步骤、有状态的工作流，而不仅仅是孤立的请求-响应交互。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/learn/architecture">Architecture overview - Model Context Protocol</a></li>
<li><a href="https://www.oracle.com/database/model-context-protocol-mcp/">Model Context Protocol (MCP) Explained - Oracle</a></li>

</ul>
</details>

**标签**: `#Model Context Protocol`, `#LLM Integration`, `#AI Engineering`, `#ChatGPT`, `#Claude`

---

<a id="item-12"></a>
## [机器学习教授因会议审稿流程流失博士候选人](https://www.reddit.com/r/MachineLearning/comments/1vawwb8/i_have_lost_three_and_a_half_potential_phd/) ⭐️ 7.0/10

一位早期职业机器学习教授报告称，三名有才华的本科生在经历会议论文审稿流程后决定放弃攻读博士学位，第四名也因对审稿人反馈感到沮丧而险些流失。尽管这些论文获得了积极评价且质量远超录取标准，但仍被拒稿并陷入无休止的重新提交循环，解决上一轮的问题只会引来更多随机的批评。 这凸显了学术同行评审中的一个系统性问题，即会议评审的不可预测性和随意性正在积极地将有才华的研究人员赶出该领域。如果评审流程继续打击有前途的学生，可能会导致机器学习研究领域出现严重的人才流失，并损害学术生态系统的长期健康。 教授指出，这些论文并非低质量的“彩票式”投稿，而是其正在进行的研究的一部分且结果良好，最终在收到四个一致的弱接受意见后仍被拒稿。当论文没有明显缺陷时，审稿过程会变得越来越随机，因为审稿人开始挑出任意的问题，给作者造成了令人沮丧的循环。

reddit · r/MachineLearning · /u/AffectionateLife5693 · 7月30日 15:30

**背景**: 在机器学习和人工智能领域，NeurIPS、ICML 和 ICLR 等顶级会议是发表研究的主要场所，但这些会议的投稿量激增，每个会议通常超过一万篇论文。这种庞大的数量给同行评审系统带来了压力，引发了人们对评审质量、审稿人责任以及录用决定随机性的担忧。帖子中提到的“彩票假设”指的是提交大量论文希望其中一篇能侥幸被录用，这与教授声称这些是严肃的研究工作形成了对比。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://towardsdatascience.com/some-issues-in-the-review-process-of-machine-learning-conferences-2c19c1eef42f/">Some Issues in the Review Process of Machine Learning Conferences</a></li>
<li><a href="https://arxiv.org/html/2505.04966v1">Position: The AI Conference Peer Review Crisis</a></li>

</ul>
</details>

**标签**: `#academic-peer-review`, `#machine-learning`, `#phd-admissions`, `#research-culture`, `#conference-reviews`

---

<a id="item-13"></a>
## [新 Python 包 ganfs 利用 GAN 自动进行特征选择](https://www.reddit.com/r/MachineLearning/comments/1vahcwo/i_built_ganfs_a_python_package_that_uses_gans_to/) ⭐️ 7.0/10

一个名为 ganfs 的开源 Python 包已发布，它利用生成对抗网络（GAN）自动对高维数据集中的特征进行排序和选择，无需领域专家知识。该软件包可通过 pip 安装，遵循类似 scikit-learn 的 API，其底层研究已发表在 arXiv 上。 该工具解决了机器学习中的一个主要瓶颈，通过自动化特征选择，克服了传统方法在高维数据中可扩展性差和难以捕捉复杂非线性关系的问题。它有望显著降低从网络安全到通用数据科学等各个领域在数据预处理方面所需的时间和专业知识。 该算法在数据集上训练 GAN，并对判别器应用扰动策略，根据生成器最难伪造的特征来对它们进行排名。虽然软件包功能完整，但开发者指出目前仍在优化针对较小数据集的 GPU 内存消耗问题。

reddit · r/MachineLearning · /u/One_Crow_4710 · 7月30日 02:54

**背景**: 特征选择是机器学习中的关键步骤，旨在识别最相关的输入变量以提高模型性能并降低计算成本。传统方法通常依赖统计过滤、包装技术或嵌入模型，这些方法可能计算成本高昂或需要人工领域知识。生成对抗网络（GAN）是一种深度学习模型，由相互竞争的生成器和判别器组成，用于学习复杂的数据分布。ganfs 通过利用判别器对特定输入特征的敏感性，重新利用该架构实现了自动特征排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/gan/">What is a GAN ? - Generative Adversarial Networks Explained - AWS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Feature_selection">Feature selection - Wikipedia</a></li>
<li><a href="https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/">A Gentle Introduction to Generative Adversarial Networks ( GANs )</a></li>

</ul>
</details>

**标签**: `#machine-learning`, `#feature-selection`, `#generative-adversarial-networks`, `#python`, `#open-source`

---

<a id="item-14"></a>
## [结合 LSTM 与混合密度网络生成拟人鼠标轨迹以绕过机器人检测](https://www.reddit.com/r/MachineLearning/comments/1vakwmq/i_taught_an_lstm_to_move_a_mouse_like_a_human_p/) ⭐️ 7.0/10

一名开发者训练了一个结合混合密度网络（MDN）的 2 层 LSTM 模型，用于生成拟人化的鼠标移动轨迹，并成功绕过了近期发布的基于光标追踪的机器人检测系统 Precursor。 该成果表明，用于机器人检测的行为生物特征可以被相对简单的深度学习模型伪造，凸显了开发更稳健的多模态反机器人策略的必要性。 该架构使用 2 层 LSTM 来捕捉光标轨迹中的时间依赖性，并在输出层采用 MDN 来对人类鼠标移动的多模态分布进行建模，而不是预测单一确定性路径。

reddit · r/MachineLearning · /u/Possible-Session9849 · 7月30日 05:52

**背景**: 长短期记忆网络（LSTM）是一种循环神经网络，专为学习序列数据中的长期依赖关系而设计，非常适合对鼠标移动等时间序列行为进行建模。混合密度网络（MDN）由 Christopher Bishop 于 1994 年提出，它通过输出概率混合分布的参数来扩展传统神经网络，使其能够捕捉不确定性和多种可能的结果。基于光标追踪的机器人检测系统通过分析鼠标移动的轨迹、速度和线性度，来区分不规则的人类行为与可预测的自动化脚本。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Long_short-term_memory">Long short-term memory - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Mixture_Density_Network">Mixture Density Network</a></li>
<li><a href="https://scrapingant.com/blog/detect-bot-by-cursor">Using Cursor Data Position for Web Bot Detection | ScrapingAnt</a></li>

</ul>
</details>

**标签**: `#LSTM`, `#Mixture Density Networks`, `#Bot Detection`, `#Behavioral Modeling`, `#Deep Learning`

---