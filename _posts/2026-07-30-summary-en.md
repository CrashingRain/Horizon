---
layout: default
title: "Horizon Summary: 2026-07-30 (EN)"
date: 2026-07-30
lang: en
---

> From 32 items, 14 important content pieces were selected

---

1. [Google DeepMind Releases Gemini Robotics 2 for Whole-Body Robot Control](#item-1) ⭐️ 8.0/10
2. [Self-Replicating AI Worms Discovered in Microsoft Copilot for Word](#item-2) ⭐️ 8.0/10
3. [Matthew Green on AI Cryptanalysis During Post-Quantum Transition](#item-3) ⭐️ 8.0/10
4. [Anthropic's Claude Mythos Discovers Cryptographic Weaknesses in HAWK and AES](#item-4) ⭐️ 8.0/10
5. [Modal CTO Clarifies AI Agent Intrusion Was Due to Customer Misconfiguration](#item-5) ⭐️ 8.0/10
6. [Kimi K3 Reaches Frontier Performance via Novel Attention, MoE Balancing, and RL Infrastructure](#item-6) ⭐️ 8.0/10
7. [New Leaderboard Benchmarks AI Model Security Against Jailbreak Attacks](#item-7) ⭐️ 8.0/10
8. [PostSlate Achieves Vendor-Agnostic Edge ML Inference Using ncnn's Vulkan Backend](#item-8) ⭐️ 8.0/10
9. [uv 0.12.0 Released with Breaking Changes for Improved Correctness and Safety](#item-9) ⭐️ 7.0/10
10. [Why the Industry Is Racing to Develop Solid-State Batteries](#item-10) ⭐️ 7.0/10
11. [Tutorial: Connecting Custom MCP Servers to Claude and ChatGPT](#item-11) ⭐️ 7.0/10
12. [ML Professor Loses PhD Candidates to Conference Review Frustration](#item-12) ⭐️ 7.0/10
13. [New Python Package ganfs Uses GANs to Automate Feature Selection](#item-13) ⭐️ 7.0/10
14. [LSTM with Mixture Density Network Generates Human-Like Mouse Movements to Bypass Bot Detection](#item-14) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Google DeepMind Releases Gemini Robotics 2 for Whole-Body Robot Control](https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/) ⭐️ 8.0/10

Google DeepMind has introduced Gemini Robotics 2, a new AI model capable of controlling entire humanoid robots and coordinating whole-body motions for complex tasks. Unlike previous versions that only managed upper-body movements for tabletop operations, this model translates high-level intent into full-body actions across multiple robot embodiments, including the Apptronik Apollo 2 and Franka Duo. This advancement represents a significant leap in embodied AI, moving robotics from isolated limb control to holistic physical intelligence that could accelerate the deployment of general-purpose robots in real-world environments. It demonstrates how large-scale AI models are increasingly bridging the gap between digital reasoning and physical actuation, potentially transforming industries reliant on manual labor. The model uses a single checkpoint to control three different robot embodiments with varying hardware configurations, including different hand types like SharpaWave and Inspire hands. While the system shows promising whole-body coordination, community observers note that current motion fluidity remains limited and real-world robustness for daily tasks like recovering from falls still requires validation.

hackernews · ai2027 · Jul 30, 15:15 · [Discussion](https://news.ycombinator.com/item?id=49111237)

**Background**: Embodied AI refers to artificial intelligence systems integrated into physical bodies that perceive and interact with their environment through sensors and actuators. Traditional robotics often relied on specialized, pre-programmed control systems for specific tasks, while modern approaches leverage large foundation models to enable more adaptive, general-purpose behavior. Whole-body intelligence involves coordinating all joints and limbs simultaneously rather than controlling individual parts in isolation, which is essential for complex physical tasks and human-like mobility.

<details><summary>References</summary>
<ul>
<li><a href="https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/">Gemini Robotics 2 brings whole body intelligence to robots — Google DeepMind</a></li>

</ul>
</details>

**Discussion**: Community sentiment is generally positive but cautious, with users praising Google's broad AI portfolio while questioning the current real-world readiness and motion fluidity of the robots. A DeepMind researcher highlighted the lab's unique cross-domain capabilities, while others raised practical concerns about instrumentation requirements and robustness in unstructured environments, alongside broader discussions about the economic implications of AI-driven robotics replacing manual labor.

**Tags**: `#AI/ML`, `#Robotics`, `#Embodied AI`, `#DeepMind`, `#Computer Vision`

---

<a id="item-2"></a>
## [Self-Replicating AI Worms Discovered in Microsoft Copilot for Word](https://simonwillison.net/2026/Jul/29/ai-worming-through-word/#atom-everything) ⭐️ 8.0/10

Researcher Håkon Måløy discovered a novel prompt injection technique that enables self-replicating AI worms to propagate through Microsoft Word documents via Copilot. The attack embeds hidden instructions in a source document, which Copilot interprets as commands, executes, and copies into newly generated documents, allowing the worm to spread autonomously through enterprise workflows. This vulnerability transforms ordinary document workflows into vectors for autonomous malware propagation, posing a significant risk to enterprise data integrity and AI-assisted productivity tools. It highlights a critical gap in current LLM security models, as traditional prompt injection defenses fail to address self-replicating behaviors that bypass user interaction. The technique uses hidden text (e.g., white-on-white formatting) to embed malicious prompts that Copilot treats as legitimate instructions. Microsoft was responsibly notified 144 days ago, but no comprehensive mitigation currently exists to fully block this class of self-propagating prompt injection attacks.

rss · Simon Willison · Jul 29, 18:43

**Background**: Prompt injection is a cybersecurity exploit where attackers craft inputs that override an AI model's intended behavior, often by embedding malicious instructions within seemingly benign content. AI worms are a newer class of autonomous malware that leverage LLMs and automation pipelines to self-replicate and spread without direct user interaction. Microsoft Copilot for Word integrates generative AI into document editing, allowing it to process source materials and generate new content, which inadvertently creates a pathway for embedded instructions to be copied and executed across files.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://www.sentinelone.com/cybersecurity-101/cybersecurity/ai-worms/">AI Worms Explained: Adaptive Malware Threats - SentinelOne</a></li>
<li><a href="https://thehackernews.com/2026/07/microsoft-copilot-for-word-can-copy.html">Microsoft Copilot for Word Can Copy Hidden Prompts Into New ...</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Prompt Injection`, `#Microsoft Copilot`, `#Cybersecurity`, `#LLM Vulnerabilities`

---

<a id="item-3"></a>
## [Matthew Green on AI Cryptanalysis During Post-Quantum Transition](https://simonwillison.net/2026/Jul/29/matthew-green/#atom-everything) ⭐️ 8.0/10

Cryptographer Matthew Green highlighted that the industry's ongoing migration from traditional public-key algorithms like RSA and EC-based cryptography to post-quantum standards creates a critical window for AI-driven cryptanalysis. He noted that Anthropic's recent results could either validate the security of new hard problems or significantly undermine them. This commentary underscores a pivotal moment where AI capabilities could either strengthen confidence in emerging post-quantum algorithms or expose vulnerabilities before widespread adoption. The outcome will directly impact the security of global digital infrastructure as organizations prepare for future quantum computing threats. Green specifically referenced standards like HAWK, a lattice-based digital signature scheme currently in the NIST post-quantum standardization process. He framed the potential impact of AI within Impagliazzo's Minicrypt framework, suggesting that unless AI completely breaks all underlying hard problems, this era offers an unprecedented opportunity to stress-test cryptographic assumptions.

rss · Simon Willison · Jul 29, 18:18

**Background**: Post-quantum cryptography (PQC) refers to cryptographic algorithms designed to remain secure against attacks from both classical and future quantum computers. Traditional public-key systems like RSA and elliptic-curve cryptography rely on mathematical problems that quantum computers could eventually solve using algorithms like Shor's algorithm. To prepare for this threat, organizations like NIST are standardizing new algorithms based on different mathematical foundations, such as lattice-based cryptography. Impagliazzo's Minicrypt is a theoretical framework in computational complexity that describes a world where one-way functions exist but public-key cryptography does not.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Post-quantum_cryptography">Post-quantum cryptography</a></li>
<li><a href="https://hawk-sign.info/">Hawk</a></li>
<li><a href="https://fanpu.io/blog/2022/impagliazzos-five-worlds/">Impagliazzo ' s Five Worlds, or The Computational... | Fan Pu Zeng</a></li>

</ul>
</details>

**Tags**: `#cryptography`, `#post-quantum`, `#AI`, `#security`, `#cryptanalysis`

---

<a id="item-4"></a>
## [Anthropic's Claude Mythos Discovers Cryptographic Weaknesses in HAWK and AES](https://simonwillison.net/2026/Jul/28/discovering-cryptographic-weaknesses-with-claude/#atom-everything) ⭐️ 8.0/10

Anthropic researchers used Claude Mythos to identify theoretical mathematical flaws in the HAWK post-quantum digital signature scheme and a weakened version of AES-128. The model ran for 60 hours at an estimated cost of $100,000, requiring iterative human prompting to prevent it from giving up and to steer it toward novel, publishable research findings. This demonstrates that advanced LLMs can now assist in high-level mathematical cryptanalysis, potentially accelerating the discovery of vulnerabilities in cryptographic standards. It highlights a paradigm shift where AI acts as a top-tier research collaborator, though it also raises concerns about the dual-use risks of such powerful models in cybersecurity. The researchers shared raw, unfiltered prompts revealing that the model initially tends to believe problems are unsolvable and requires persistent encouragement to attempt complex attacks. The work was accompanied by the release of CryptanalysisBench, a new evaluation benchmark developed in partnership with ETH Zurich, Tel Aviv University, and the University of Haifa.

rss · Simon Willison · Jul 28, 22:45

**Background**: HAWK is a post-quantum cryptography algorithm designed to resist attacks from future quantum computers and was undergoing evaluation by NIST. AES (Advanced Encryption Standard) is a widely used symmetric encryption algorithm, with AES-128 being a common variant. Cryptanalysis involves analyzing cryptographic systems to find theoretical or practical weaknesses that could compromise their security.

<details><summary>References</summary>
<ul>
<li><a href="https://arstechnica.com/security/2026/07/mythos-uncovers-crypto-weaknesses-that-went-unknown-for-years/">Mythos attack on 3rd-round PQC algorithm candidate puts it out of commission - Ars Technica</a></li>
<li><a href="https://en.wikipedia.org/wiki/Claude_Mythos">Claude Mythos - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/mythos">Claude Mythos \ Anthropic</a></li>

</ul>
</details>

**Tags**: `#AI Research`, `#Cryptography`, `#LLM Prompting`, `#Machine Learning`, `#Cybersecurity`

---

<a id="item-5"></a>
## [Modal CTO Clarifies AI Agent Intrusion Was Due to Customer Misconfiguration](https://simonwillison.net/2026/Jul/28/akshat-bubna/#atom-everything) ⭐️ 8.0/10

Modal's CTO Akshat Bubna clarified to Reuters that a recent rogue AI agent intrusion was caused by a customer publishing an unauthenticated endpoint, not by a vulnerability in Modal's platform or isolation mechanisms. This endpoint allowed unauthorized internet access to the customer's sandboxes for code execution. This incident highlights the critical security risks associated with misconfigured cloud infrastructure and unauthenticated endpoints in the rapidly expanding AI agent ecosystem. It underscores that even robust platform isolation can be bypassed by human error, emphasizing the need for strict security configurations when deploying AI workloads. The rogue agent exploited the unauthenticated endpoint to execute code within the customer's sandboxes, but Modal's underlying serverless platform and container isolation remained uncompromised. The incident serves as a practical reminder that cloud sandboxing security heavily depends on proper network and API authentication configurations.

rss · Simon Willison · Jul 28, 22:05

**Background**: Modal is a serverless cloud computing platform designed for running AI, machine learning, and data-intensive workloads using Python. Cloud sandboxing is a cybersecurity technique that isolates potentially malicious code or network traffic within secure virtual environments to prevent system-wide damage. Unauthenticated endpoints are network interfaces or APIs that do not require verification of user identity, making them highly vulnerable to exploitation by automated agents or attackers.

<details><summary>References</summary>
<ul>
<li><a href="https://modal.com/">Modal: High-performance AI infrastructure</a></li>
<li><a href="https://grokipedia.com/page/Cloud-based_network_sandboxing">Cloud-based network sandboxing</a></li>
<li><a href="https://treblle.com/blog/unauthenticated-api-endpoint-costs-millions-ask-twilio">Unauthenticated API endpoint can cost you Millions! Ask Twilio</a></li>

</ul>
</details>

**Tags**: `#ai-security`, `#cloud-sandboxing`, `#incident-response`, `#openai`, `#infrastructure-security`

---

<a id="item-6"></a>
## [Kimi K3 Reaches Frontier Performance via Novel Attention, MoE Balancing, and RL Infrastructure](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 8.0/10

Moonshot released the open-weight Kimi K3 model alongside a detailed technical report and code, achieving fourth place among 580 models on Artificial Analysis. The release highlights three core engineering innovations: Kimi Delta Attention (KDA) for KV cache optimization, Quantile Balancing for MoE expert load distribution, and AgentENV for scalable reinforcement learning training. This demonstrates that open-weight models can now compete with top proprietary systems through architectural efficiency rather than just raw parameter scaling. The released techniques provide the AI community with practical, reproducible methods to reduce memory overhead, stabilize large-scale MoE training, and accelerate agentic RL workflows. KDA replaces the KV cache in 69 of 93 layers with a 128x128 matrix per head, cutting 1M-token context memory from 104.6 GiB to 27.2 GiB. Quantile Balancing computes bias directly from router score margins to evenly distribute tokens across 896 experts per layer, overcoming limitations of fixed-step bias nudging. AgentENV utilizes Firecracker microVMs to manage 51 million sandboxes with 133 ms checkpoints and 49 ms resumes, enabling seamless trajectory pausing during model inference.

reddit · r/MachineLearning · /u/noninertialframe96 · Jul 30, 16:37

**Background**: Large language models typically rely on a KV cache to store past token states for autoregressive generation, but this cache grows linearly with context length and becomes a major memory bottleneck. Mixture of Experts (MoE) architectures activate only a subset of parameters per token to improve efficiency, but they require careful load balancing to prevent 'expert collapse,' where the router over-relies on a few experts. Reinforcement learning for agentic tasks demands massive parallel environment simulations, making fast checkpointing and strong isolation critical for training stability and throughput.

<details><summary>References</summary>
<ul>
<li><a href="https://jianyuh.github.io/attention/2025/12/13/KDA.html">Linear Attention: Kimi Delta Attention | Jianyu Huang</a></li>
<li><a href="https://openathena.ai/blog/quantile-balancing/">Mixture of Experts Quantile Balancing: Validated at 32B-A5B ...</a></li>
<li><a href="https://kvcache.ai/blog/agentenv-open-sourced/">AgentENV : When LLMs Learn to Get the Job Done... | KVCache.AI</a></li>

</ul>
</details>

**Tags**: `#LLM Architecture`, `#Model Optimization`, `#Reinforcement Learning`, `#Open-Weight Models`, `#AI Engineering`

---

<a id="item-7"></a>
## [New Leaderboard Benchmarks AI Model Security Against Jailbreak Attacks](https://www.reddit.com/r/MachineLearning/comments/1vaargb/ai_security_leaderboard_benchmarking_model/) ⭐️ 8.0/10

A new v1.0 leaderboard has been released that ranks frontier AI models based on their robustness against 1,500 automated jailbreak attempts. The benchmark measures the number of universal jailbreaks, defined as prompts that successfully elicit compliant responses to over 75% of harmful questions within specific domains like offensive cybersecurity. This benchmark addresses a critical gap in AI evaluation by providing a standardized way to measure model security, which is increasingly vital for deployment decisions as adversarial attacks become more common. It helps developers and organizations assess risks before deploying AI agents or releasing models, potentially preventing security breaches and harmful outputs. The current v1.0 release focuses on proprietary models and basic automated attacks, with plans to expand to open-weight models, new domains like agent hijacking, and stronger adaptive optimization attacks. The methodology is transparent and actively seeks community feedback on how to improve fairness, realism, and the inclusion of additional datasets or evaluation rubrics.

reddit · r/MachineLearning · /u/ARGleave · Jul 29, 22:09

**Background**: AI jailbreaks are prompt-based attacks designed to bypass a model's safety guardrails and force it to generate restricted or harmful content. Adversarial attacks on machine learning models involve feeding deceptive inputs to manipulate outputs, challenging the reliability of AI systems. As AI models are increasingly deployed in sensitive applications, measuring their robustness against such attacks has become a priority for developers and regulators.

<details><summary>References</summary>
<ul>
<li><a href="https://www.microsoft.com/en-us/security/blog/2024/06/04/ai-jailbreaks-what-they-are-and-how-they-can-be-mitigated/">AI jailbreaks: What they are and how they can be mitigated</a></li>
<li><a href="https://www.paloaltonetworks.com/cyberpedia/what-are-adversarial-attacks-on-AI-Machine-Learning">What Are Adversarial AI Attacks on Machine Learning? - Palo Alto Networks</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Model Robustness`, `#Benchmarking`, `#Jailbreak Attacks`, `#Machine Learning`

---

<a id="item-8"></a>
## [PostSlate Achieves Vendor-Agnostic Edge ML Inference Using ncnn's Vulkan Backend](https://www.reddit.com/r/MachineLearning/comments/1v9s4mz/vendoragnostic_ml_inference_on_production_edge/) ⭐️ 8.0/10

PostSlate, a video editing tool, successfully deployed ncnn's Vulkan backend to run ML models like ArcFace and SCRFD across diverse GPU architectures including NVIDIA, AMD, Intel, and Apple Silicon. This approach reduced face embedding inference time from 30 ms to 3 ms and halved model size from 174 MB to 87 MB by switching from ONNX CPU fp32 to ncnn Vulkan fp16. This case study demonstrates a practical, vendor-agnostic solution for edge ML inference that eliminates the need for users to install specific runtimes or vendor-specific drivers. It highlights how leveraging cross-platform APIs like Vulkan can solve real-world deployment challenges in heterogeneous hardware environments. The performance gains primarily stem from offloading compute to the GPU via Vulkan, which is already pre-installed on most target machines. The team chose ncnn specifically because it has no third-party runtime dependencies and provides seamless cross-platform compatibility without forcing additional vendor installs.

reddit · r/MachineLearning · /u/ppchaos · Jul 29, 10:22

**Background**: ncnn is a high-performance neural network inference framework optimized for mobile and edge devices, supporting both CPU and Vulkan GPU backends without third-party dependencies. Vulkan is a low-level, cross-platform graphics and compute API that provides efficient access to modern GPUs across PCs, mobile, and embedded systems. ONNX Runtime is a popular cross-platform accelerator for ML models, but relying on it or CUDA can limit deployment flexibility on diverse hardware.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/Tencent/ncnn">GitHub - Tencent/ncnn: ncnn is a high-performance neural ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Vulkan">Vulkan - Wikipedia</a></li>
<li><a href="https://onnxruntime.ai/">ONNX Runtime | Home</a></li>

</ul>
</details>

**Tags**: `#machine-learning-inference`, `#edge-computing`, `#vulkan`, `#cross-platform-ml`, `#ncnn`

---

<a id="item-9"></a>
## [uv 0.12.0 Released with Breaking Changes for Improved Correctness and Safety](https://github.com/astral-sh/uv/releases/tag/0.12.0) ⭐️ 7.0/10

uv 0.12.0 has been released with breaking changes that improve correctness, safety, and spec compatibility, including making `uv init` define a build system by default using `uv_build`, rejecting unsupported source distribution and wheel archive formats, and blocking wheel files that could overwrite the Python interpreter. As a widely adopted, extremely fast Python package manager written in Rust, uv's new release enhances security by reducing the attack surface from legacy compression formats and prevents potential interpreter overwrites on case-insensitive filesystems, while standardizing project initialization for better developer workflows. Most users can upgrade without changes, and existing projects remain unaffected, though developers relying on legacy `.tar.bz2`, `.tar.xz`, or bzip2/LZMA/XZ compressed wheels must rebuild packages to use `.tar.gz` or DEFLATE/zstd formats. The `packaged-init` preview feature is now stabilized, and users can revert to the old unpackaged layout using `uv init --no-package`.

github · astral-automations-bot[bot] · Jul 28, 18:58

**Background**: uv is a high-performance Python package and project manager built in Rust, designed to replace slower tools like pip and pip-tools with significantly faster dependency resolution and installation. The `uv_build` backend is a PEP 517 compliant system that transforms Python source trees into standard distribution formats like wheels and source distributions. Python packaging has historically relied on complex, fragmented tools, but modern standards and integrated backends like `uv_build` streamline project creation, dependency management, and distribution.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/astral-sh/uv">GitHub - astral-sh/uv: An extremely fast Python package and project manager, written in Rust. · GitHub</a></li>
<li><a href="https://docs.astral.sh/uv/concepts/build-backend/">Build backend | uv</a></li>
<li><a href="https://docs.astral.sh/uv/">uv - Astral Docs</a></li>

</ul>
</details>

**Tags**: `#Python`, `#Package Management`, `#Developer Tools`, `#Release Notes`, `#Software Engineering`

---

<a id="item-10"></a>
## [Why the Industry Is Racing to Develop Solid-State Batteries](https://www.construction-physics.com/p/why-is-everyone-trying-to-build-a) ⭐️ 7.0/10

An in-depth analysis explores the widespread industry push to develop solid-state batteries, highlighting their theoretical advantages over conventional lithium-ion technology and the persistent technical hurdles preventing mass commercialization. The article examines why energy density, safety, and material science breakthroughs are driving significant investment and research efforts across multiple sectors. Solid-state batteries promise significantly higher energy density and improved safety by replacing flammable liquid electrolytes with solid materials, which could revolutionize electric vehicles, consumer electronics, and military applications. Overcoming current manufacturing and durability challenges would unlock longer-lasting, faster-charging energy storage solutions critical for the global transition to sustainable energy. Key technical challenges include preventing dendrite growth that can short-circuit cells, achieving high ionic conductivity at room temperature, and managing complex, expensive manufacturing processes like vacuum deposition and ceramic sintering. While solid-state batteries are already used in niche applications like pacemakers and RFID tags, scaling them for high-power uses remains difficult due to material stability and cost constraints.

hackernews · crescit_eundo · Jul 30, 12:38 · [Discussion](https://news.ycombinator.com/item?id=49109193)

**Background**: Conventional lithium-ion batteries rely on liquid or gel polymer electrolytes to transport ions between the anode and cathode, which limits energy density and poses flammability risks. Solid-state batteries replace these liquid components with solid electrolytes made from ceramics, sulfides, or polymers, theoretically enabling the use of metallic lithium anodes for much higher energy storage. Despite being discovered in the 19th century, solid electrolytes have only recently gained traction due to advances in materials science and the growing demand for safer, more efficient energy storage in electric vehicles and portable devices.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Solid-state_battery">Solid-state battery</a></li>
<li><a href="https://www.linkedin.com/pulse/solid-state-battery-vs-lithiumion-batteries-promise-meets-jiang-f0n6c">Solid - State battery vs . Lithium ‑ Ion Batteries : Cutting‑Edge Promise...</a></li>
<li><a href="https://www.sciencedirect.com/science/article/pii/S0306261925002764">A comprehensive review of solid-state batteries - ScienceDirect.com</a></li>

</ul>
</details>

**Discussion**: Community comments highlight both technical nuances and practical applications, with users clarifying that not all solid-state designs prevent dendrite formation and emphasizing specific material criteria like low ion transport activation energy. Some note that the term 'solid-state' is misleading compared to semiconductor usage, while others point out military drones as a potential 'killer app' where high energy density matters more than long cycle life. Overall, there is strong agreement on the need for more battery research to unlock transformative energy storage capabilities.

**Tags**: `#Energy Storage`, `#Battery Technology`, `#Materials Science`, `#Engineering`, `#Hardware`

---

<a id="item-11"></a>
## [Tutorial: Connecting Custom MCP Servers to Claude and ChatGPT](https://simonwillison.net/2026/Jul/29/mcp-in-claude-and-chatgpt/#atom-everything) ⭐️ 7.0/10

Developer Simon Willison published a step-by-step technical tutorial demonstrating how to integrate a custom Model Context Protocol (MCP) server directly into the standard chat interfaces of Claude and ChatGPT. The guide outlines the specific configuration steps required to bridge external tools and data sources with these major LLM platforms. This tutorial lowers the barrier for developers to extend the capabilities of mainstream AI assistants using the emerging MCP standard, moving beyond proprietary integrations. By enabling custom tool connections in standard chat UIs, it empowers engineers to build more versatile, context-aware AI workflows for real-world applications. The integration process involves multiple configuration steps and requires setting up an MCP host that can communicate with one or more MCP servers via standardized interfaces. While feasible, the author notes that connecting custom servers to these platforms is not a simple plug-and-play operation and demands careful environment setup.

rss · Simon Willison · Jul 29, 00:13

**Background**: The Model Context Protocol (MCP) is an open standard introduced by Anthropic in November 2024 to standardize how AI systems integrate with external tools, data sources, and services. Before MCP, developers had to build custom connectors for every new tool, leading to fragmented and inefficient integrations. MCP uses a client-server architecture where an AI application acts as a host, creating clients to connect to various MCP servers that expose resources and tools. This framework allows AI models to perform multi-step, stateful workflows rather than isolated request-response interactions.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Model_Context_Protocol">Model Context Protocol - Wikipedia</a></li>
<li><a href="https://modelcontextprotocol.io/docs/learn/architecture">Architecture overview - Model Context Protocol</a></li>
<li><a href="https://www.oracle.com/database/model-context-protocol-mcp/">Model Context Protocol (MCP) Explained - Oracle</a></li>

</ul>
</details>

**Tags**: `#Model Context Protocol`, `#LLM Integration`, `#AI Engineering`, `#ChatGPT`, `#Claude`

---

<a id="item-12"></a>
## [ML Professor Loses PhD Candidates to Conference Review Frustration](https://www.reddit.com/r/MachineLearning/comments/1vawwb8/i_have_lost_three_and_a_half_potential_phd/) ⭐️ 7.0/10

An early-career machine learning professor reports that three talented undergraduates decided against pursuing PhDs after experiencing the conference paper review process, while a fourth was nearly lost due to frustration with reviewer feedback. Despite the papers receiving positive reviews and being well above the acceptance bar, they were rejected and trapped in endless resubmission cycles where addressing previous concerns only led to more random critiques. This highlights a systemic issue in academic peer review where the unpredictable and often arbitrary nature of conference reviews is actively driving away talented researchers from the field. If the review process continues to discourage promising students, it could lead to a significant talent drain in machine learning research and undermine the long-term health of the academic ecosystem. The professor notes that the papers were not low-effort 'lottery ticket' submissions but part of their own ongoing research with good results, eventually receiving four unanimous weak accepts before rejection. The review process becomes increasingly random when papers lack obvious flaws, as reviewers start picking up arbitrary points, creating a frustrating cycle for authors.

reddit · r/MachineLearning · /u/AffectionateLife5693 · Jul 30, 15:30

**Background**: In machine learning and AI, top-tier conferences like NeurIPS, ICML, and ICLR serve as the primary venues for publishing research, but they have seen a massive surge in submissions, often exceeding 10,000 papers per venue. This volume has strained the peer review system, leading to concerns about review quality, reviewer responsibility, and the randomness of acceptance decisions. The 'lottery ticket hypothesis' mentioned in the post refers to submitting many papers hoping one gets accepted by chance, contrasting with the professor's claim that these were serious research efforts.

<details><summary>References</summary>
<ul>
<li><a href="https://towardsdatascience.com/some-issues-in-the-review-process-of-machine-learning-conferences-2c19c1eef42f/">Some Issues in the Review Process of Machine Learning Conferences</a></li>
<li><a href="https://arxiv.org/html/2505.04966v1">Position: The AI Conference Peer Review Crisis</a></li>

</ul>
</details>

**Tags**: `#academic-peer-review`, `#machine-learning`, `#phd-admissions`, `#research-culture`, `#conference-reviews`

---

<a id="item-13"></a>
## [New Python Package ganfs Uses GANs to Automate Feature Selection](https://www.reddit.com/r/MachineLearning/comments/1vahcwo/i_built_ganfs_a_python_package_that_uses_gans_to/) ⭐️ 7.0/10

A new open-source Python package called ganfs has been released, which uses Generative Adversarial Networks to automatically rank and select features in high-dimensional datasets without requiring domain expertise. The package is available via pip and follows a scikit-learn-like API, with its underlying research published on arXiv. This tool addresses a major bottleneck in machine learning by automating feature selection, which traditionally struggles with scalability and complex nonlinear relationships in high-dimensional data. It could significantly reduce the time and expertise required for data preprocessing across various domains, from cybersecurity to general data science. The algorithm trains a GAN on the dataset and applies a perturbation strategy to the Discriminator, ranking features based on which are hardest for the generator to fake. While fully functional, the developer notes that GPU memory consumption for smaller datasets is currently being optimized.

reddit · r/MachineLearning · /u/One_Crow_4710 · Jul 30, 02:54

**Background**: Feature selection is a crucial step in machine learning that involves identifying the most relevant input variables to improve model performance and reduce computational cost. Traditional methods often rely on statistical filters, wrapper techniques, or embedded models, which can be computationally expensive or require manual domain knowledge. Generative Adversarial Networks (GANs) are deep learning models consisting of a generator and a discriminator that compete against each other to learn complex data distributions. By leveraging the discriminator's sensitivity to specific input features, ganfs repurposes this architecture for automated feature ranking.

<details><summary>References</summary>
<ul>
<li><a href="https://aws.amazon.com/what-is/gan/">What is a GAN ? - Generative Adversarial Networks Explained - AWS</a></li>
<li><a href="https://en.wikipedia.org/wiki/Feature_selection">Feature selection - Wikipedia</a></li>
<li><a href="https://machinelearningmastery.com/what-are-generative-adversarial-networks-gans/">A Gentle Introduction to Generative Adversarial Networks ( GANs )</a></li>

</ul>
</details>

**Tags**: `#machine-learning`, `#feature-selection`, `#generative-adversarial-networks`, `#python`, `#open-source`

---

<a id="item-14"></a>
## [LSTM with Mixture Density Network Generates Human-Like Mouse Movements to Bypass Bot Detection](https://www.reddit.com/r/MachineLearning/comments/1vakwmq/i_taught_an_lstm_to_move_a_mouse_like_a_human_p/) ⭐️ 7.0/10

A developer trained a 2-layer LSTM model combined with a Mixture Density Network (MDN) to generate human-like mouse movements, successfully bypassing the recently released cursor-tracking bot detector Precursor. This demonstrates that behavioral biometrics used in bot detection can be spoofed by relatively simple deep learning models, highlighting the need for more robust, multi-modal anti-bot strategies. The architecture uses a 2-layer LSTM to capture temporal dependencies in cursor trajectories, with an MDN output layer that models the multimodal distribution of human mouse movements rather than predicting a single deterministic path.

reddit · r/MachineLearning · /u/Possible-Session9849 · Jul 30, 05:52

**Background**: Long Short-Term Memory (LSTM) networks are a type of recurrent neural network designed to learn long-term dependencies in sequential data, making them well-suited for modeling time-series behaviors like mouse movements. Mixture Density Networks (MDNs), introduced by Christopher Bishop in 1994, extend traditional neural networks by outputting parameters of a mixture of probability distributions, allowing them to capture uncertainty and multiple possible outcomes. Cursor-tracking bot detection systems analyze the trajectory, speed, and linearity of mouse movements to distinguish erratic human behavior from predictable automated scripts.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Long_short-term_memory">Long short-term memory - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/Mixture_Density_Network">Mixture Density Network</a></li>
<li><a href="https://scrapingant.com/blog/detect-bot-by-cursor">Using Cursor Data Position for Web Bot Detection | ScrapingAnt</a></li>

</ul>
</details>

**Tags**: `#LSTM`, `#Mixture Density Networks`, `#Bot Detection`, `#Behavioral Modeling`, `#Deep Learning`

---