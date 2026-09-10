---
layout: default
title: "Horizon Summary: 2026-09-10 (EN)"
date: 2026-09-10
lang: en
---

> From 32 items, 17 important content pieces were selected

---

1. [Microsoft Officially Adopts Rust as a Tier-1 Programming Language](#item-1) ⭐️ 9.0/10
2. [DeepSeek Releases V4.1 Flash with New Architecture and Aggressive Pricing](#item-2) ⭐️ 9.0/10
3. [Calif Research Demonstrates AI-Assisted Zero-Click WeChat Worm in Two Days](#item-3) ⭐️ 9.0/10
4. [OpenAI Claims AI Model Solved Navier-Stokes Millennium Prize Problem](#item-4) ⭐️ 9.0/10
5. [Researchers Question OpenAI's Use of Unpublished Math in Model Training](#item-5) ⭐️ 8.0/10
6. [Shopify transitions from React Native back to native iOS and Android development](#item-6) ⭐️ 8.0/10
7. [Terence Tao Warns AI May Deplete Open Research Problems](#item-7) ⭐️ 8.0/10
8. [348M Parameter Model Achieves 99.4% Accuracy on GPT-3 Arithmetic Benchmarks](#item-8) ⭐️ 8.0/10
9. [Fly Connectome Fails to Learn Pong, Revealing Critical Simulation Flaws](#item-9) ⭐️ 8.0/10
10. [Essay Theorizes Software Development Drives People Insane](#item-10) ⭐️ 7.0/10
11. [Cognition Launches SWE-2 Model Rivaling GPT-Astra and Fable 5.1](#item-11) ⭐️ 7.0/10
12. [PlanetScale Launches Neki, a Closed-Source Sharded Postgres Tool](#item-12) ⭐️ 7.0/10
13. [Raymond Chen Reveals Windows XP Default User Picture Selection Algorithm](#item-13) ⭐️ 7.0/10
14. [Sony Faces Lawsuit Over Digital Game Ownership Claims](#item-14) ⭐️ 7.0/10
15. [OpenAI Releases ChatGPT Images 2.5 with Improved Precision and Speed](#item-15) ⭐️ 7.0/10
16. [Stanford Professor Launches Free 'Probability for AI' Course with 1:10 Teaching Ratio](#item-16) ⭐️ 7.0/10
17. [Clarifying What Sante's 83.83 Score on DiagnosisArena-MCQ Actually Measures](#item-17) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Microsoft Officially Adopts Rust as a Tier-1 Programming Language](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

Microsoft has officially designated Rust as a tier-1 programming language, placing it alongside C++, C#, and TypeScript for internal development. This status provides internal engineering teams with a fully supported, paved path for local development, tooling, and production deployment. This move signals a major industry shift toward memory-safe systems programming, as Microsoft aims to reduce the high volume of memory-safety vulnerabilities that historically plague its software portfolio. It validates Rust's maturity and will likely accelerate enterprise adoption across the broader tech ecosystem. Achieving tier-1 status means Rust now receives first-class support within Microsoft's internal engineering infrastructure, including seamless integration with MSVC tooling and standardized deployment pipelines. The designation focuses on greenfield development and strategic modernization rather than immediate legacy code replacement.

hackernews · mmastrac · Sep 10, 13:39 · [Discussion](https://news.ycombinator.com/item?id=49643546)

**Background**: Rust is a general-purpose systems programming language designed to provide memory safety and thread safety without sacrificing performance, primarily through its ownership and borrowing model. Historically, systems software has been dominated by C and C++, which lack built-in memory safety guarantees and are prone to vulnerabilities like buffer overflows and null pointer dereferences. Microsoft has previously highlighted that roughly 70% of its security vulnerabilities stem from memory safety issues, prompting a strategic push toward safer alternatives.

<details><summary>References</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust (programming language) - Wikipedia</a></li>
<li><a href="https://spectrum.ieee.org/memory-safe-programming-languages">The Move to Memory-Safe Programming - IEEE Spectrum</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly positive, with users emphasizing Rust's maturity as a serious competitor to C++ and C# for systems programming. Commenters highlighted strategic benefits like reducing CVEs through memory safety, discussed ambitious goals to automate the conversion of legacy C code to Rust, and noted the significance of official MSVC integration.

**Tags**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Enterprise Software`

---

<a id="item-2"></a>
## [DeepSeek Releases V4.1 Flash with New Architecture and Aggressive Pricing](https://twitter.com/deepseek_ai/status/2097930608790167907) ⭐️ 9.0/10

DeepSeek has released DeepSeek-V4.1-Flash, an open-weight model featuring a new Causal Encoder–Decoder architecture with only 8B active input and 16B active output parameters, alongside native multimodal visual understanding. The release introduces extremely competitive API pricing, including a cache hit rate of just $0.003 per million tokens. This release significantly lowers the memory and cost barriers for deploying AI agents, potentially making long-context API usage economically viable by reducing KV cache memory fourfold. It also highlights a growing trend of technical transparency and aggressive pricing competition among leading AI labs. The model achieves its efficiency through four key architectural techniques: CED split, CSA2, FP4 quantization, and SWA elimination, reducing per-token memory to 890 bytes. While the original V4 Flash was 284B parameters, this new version scales to 552B parameters, trading local deployability for higher benchmark performance.

hackernews · Liwink · Sep 10, 06:11 · [Discussion](https://news.ycombinator.com/item?id=49639090)

**Background**: Open-weight models provide trained parameters for public use but typically do not include the full training data or code, distinguishing them from fully open-source AI. LLM API pricing is usually calculated per million tokens for input and output, with costs often dominated by context transfer in long-running tasks. KV cache memory is a critical bottleneck for AI agents, as storing conversation history directly impacts both latency and operational expenses.

<details><summary>References</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster, more efficient.</a></li>
<li><a href="https://www.techtimes.com/articles/327163/20260910/deepseek-v41-flash-cuts-agent-memory-costs-fourfold-new-architecture.htm">DeepSeek V4.1-Flash Cuts Agent Memory Costs Fourfold With New Architecture</a></li>
<li><a href="https://api-docs.deepseek.com/updates/">Change Log | DeepSeek API Docs</a></li>

</ul>
</details>

**Discussion**: Community members praise DeepSeek's detailed technical reports and fearless innovation compared to competitors' safety-focused documentation. Users are particularly surprised by the ultra-low cache pricing, debating whether network transfer costs will soon dominate API economics, while some note the model's increased size makes it less suitable for local deployment.

**Tags**: `#AI/ML`, `#Large Language Models`, `#Open Source`, `#Cloud Economics`, `#DeepSeek`

---

<a id="item-3"></a>
## [Calif Research Demonstrates AI-Assisted Zero-Click WeChat Worm in Two Days](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research released a demo of WeWorm, the first zero-click worm that spreads via WeChat calls across iOS and Android, compromising accounts without any user interaction. The team discovered the vulnerability and wrote the initial remote code execution (RCE) exploit in just two days using AI assistance, with the full worm built in one additional week. This breakthrough highlights a dramatic shift in exploit development speed and scale, demonstrating that AI can now automate most of the complex work previously requiring large teams and months of effort. It raises urgent concerns about the accessibility of advanced cyber weapons and the need for faster vulnerability patching in widely used communication platforms. The exploit triggers when a WeChat call is placed to a target device, succeeding even if the call is unanswered or declined, and was demonstrated spreading across a Pixel 10a and an iPhone 17e. Tencent was notified in July 2026 and implemented a server-side block confirmed on August 28, with no evidence of real-world exploitation.

rss · Simon Willison · Sep 10, 00:56

**Background**: A zero-click exploit allows attackers to compromise a device or application without requiring any action from the victim, making it one of the most dangerous types of cyber threats. Remote code execution (RCE) enables an attacker to run arbitrary commands on a target system, often serving as the foundation for worms that self-propagate across networks. WeChat is a widely used messaging and VoIP platform, and vulnerabilities in its call handling infrastructure can expose millions of users to automated account hijacking.

<details><summary>References</summary>
<ul>
<li><a href="https://calif.io/research/weworm">The first zero-click worm to spread through WeChat calls across iOS...</a></li>
<li><a href="https://thehackernews.com/2026/09/wechat-zero-click-worm-took-over.html">WeChat Zero-Click Worm Took Over Accounts on iPhone and Android via Incoming Calls</a></li>

</ul>
</details>

**Tags**: `#AI Security`, `#Zero-Click Exploit`, `#Cybersecurity`, `#AI-Assisted Development`, `#Mobile Security`

---

<a id="item-4"></a>
## [OpenAI Claims AI Model Solved Navier-Stokes Millennium Prize Problem](https://simonwillison.net/2026/Sep/8/on-navier-stokes/) ⭐️ 9.0/10

OpenAI announced that an unreleased internal model, running a swarm of approximately 10,000 AI agents, produced a counterexample proving the breakdown of Navier-Stokes solutions in three-dimensional space. The result was formalized in the Lean proof assistant using GPT-6 Astra, but the announcement is accompanied by a priority dispute with mathematicians Tristan Buckmaster and Levent Alpöge. If verified, this would mark the first time an AI system has resolved one of the seven Millennium Prize Problems, fundamentally transforming mathematical research and fluid dynamics. The controversy highlights emerging tensions over AI-assisted discovery, data privacy, and credit attribution between competing AI labs and academia. The OpenAI agents sent 2.7 million messages and consumed roughly 130 billion output tokens to resolve the problem, with formal verification taking an additional 17 hours. OpenAI stated it would decline the $1 million Clay Millennium Prize, and the counterexample has not yet been independently verified by the mathematical community.

rss · Simon Willison · Sep 8, 23:55

**Background**: The Navier-Stokes existence and smoothness problem is one of seven Millennium Prize Problems established by the Clay Mathematics Institute in 2000, each carrying a $1 million reward. It asks whether the equations governing fluid motion always produce smooth, globally defined solutions in three dimensions, or if they can break down into singularities. While computational fluid dynamics is widely used in engineering, a complete mathematical proof of the equations' behavior has remained elusive for over a century.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_existence_and_smoothness_problem">Navier-Stokes existence and smoothness problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Millennium_Prize_Problems">Millennium Prize Problems</a></li>

</ul>
</details>

**Tags**: `#AI Research`, `#Mathematics`, `#OpenAI`, `#Millennium Prize Problems`, `#Scientific Controversy`

---

<a id="item-5"></a>
## [Researchers Question OpenAI's Use of Unpublished Math in Model Training](https://mathstodon.xyz/@andreasthom/117240535270608201) ⭐️ 8.0/10

Researchers and the broader AI community are debating whether OpenAI is ethically and technically justified in using unpublished mathematical research from user interactions to train models and publish results without attribution. The discussion highlights concerns about data provenance, model training mechanics, and the potential for AI to inadvertently or intentionally leverage confidential academic work. This debate is significant because it touches on core issues of research integrity, intellectual property, and the ethical boundaries of AI training data usage. If AI companies routinely incorporate unpublished academic work into their models without proper attribution, it could undermine trust in AI collaboration and disrupt traditional academic publishing norms. Community members note that while OpenAI's models may improve their latent representations through user interactions, the massive scale of RLHF and verifiable math training could also lead to independent discoveries that diverge from specific user inputs. Critics point out the suspicious timing of generating 300 billion output tokens from a model still in training shortly after learning about potential training data containing major math proofs.

hackernews · pred_ · Sep 10, 06:49 · [Discussion](https://news.ycombinator.com/item?id=49639408)

**Background**: OpenAI and other AI developers often use user interactions and publicly available data to train large language models. Reinforcement Learning from Human Feedback (RLHF) and other training techniques help refine model outputs, but the exact mechanisms of how models retain or generalize from specific inputs remain partially opaque. Academic researchers frequently use AI tools to explore open problems, raising questions about whether their unpublished ideas might be absorbed into future model versions.

**Discussion**: The community discussion reveals a mix of ethical concerns and technical skepticism, with some comparing OpenAI's actions to unethical human collaboration while others argue that model training at scale may lead to independent discoveries. Users also question whether AI's rapid progress on open problems is genuine or influenced by fresh training data from researchers, and some suggest testing for data leakage using canary phrases.

**Tags**: `#AI Ethics`, `#Machine Learning`, `#Research Integrity`, `#OpenAI`, `#Mathematics`

---

<a id="item-6"></a>
## [Shopify transitions from React Native back to native iOS and Android development](https://shopify.engineering/back-to-native) ⭐️ 8.0/10

Shopify has publicly shared its engineering decision to transition its mobile applications from the cross-platform React Native framework back to platform-specific native development for iOS and Android. The company detailed the trade-offs involved, emphasizing that native development ultimately provided better optimization and performance for their specific needs. This decision serves as a significant industry case study that challenges the prevailing trend of adopting cross-platform frameworks for cost and resource efficiency. It highlights the ongoing debate in software engineering about when to prioritize platform-specific optimization over unified codebases, especially as AI-assisted code generation begins to lower the barrier for native development. Shopify's move underscores that while cross-platform tools like React Native can initially reduce headcount costs by leveraging web developers, they often result in lowest-common-denominator apps that require significant platform-specific workarounds. The transition back to native development reflects a strategic shift toward dedicated platform expertise, a trend further accelerated by modern AI tools that can rapidly generate native iOS and Android code.

hackernews · fnthawar2 · Sep 10, 14:09 · [Discussion](https://news.ycombinator.com/item?id=49643982)

**Background**: React Native is an open-source UI framework developed by Meta that allows developers to build mobile applications for iOS and Android using JavaScript and React. Native development, on the other hand, involves writing platform-specific code using languages like Swift or Objective-C for iOS and Kotlin or Java for Android. Historically, companies have adopted cross-platform frameworks to share code and reduce development costs, but this often comes at the expense of performance, access to the latest platform features, and a polished user experience.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/React_Native">React Native</a></li>
<li><a href="https://reactnative.dev/">React Native</a></li>
<li><a href="https://www.linkedin.com/pulse/native-ios-development-still-demand-comprehensive-overview-يسر-بلال-b6tic">Is Native iOS Development Still in Demand? A Comprehensive...</a></li>

</ul>
</details>

**Discussion**: Community comments largely agree that the choice between cross-platform and native development is a resource-driven engineering decision rather than an absolute rule. Several developers noted that while React Native was historically useful for leveraging web teams, the rise of AI code generation significantly reduces the overhead of building and maintaining separate native apps. Others pointed out that cross-platform frameworks rarely deliver the promised headcount savings and often lead to higher long-term maintenance costs due to platform-specific workarounds.

**Tags**: `#mobile-development`, `#react-native`, `#engineering-trade-offs`, `#software-architecture`, `#cross-platform`

---

<a id="item-7"></a>
## [Terence Tao Warns AI May Deplete Open Research Problems](https://simonwillison.net/2026/Sep/9/terence-tao/) ⭐️ 8.0/10

Fields Medal-winning mathematician Terence Tao recently posted on Mathstodon that AI's rapid problem-solving capabilities are depleting the pool of open research problems in a non-renewable way. He warns that the mere rumor of a researcher tackling a problem now triggers massive AI-driven efforts to solve it first, potentially incentivizing researchers to keep promising directions secret. This shift threatens to reverse centuries of open scientific tradition by replacing collaborative knowledge sharing with competitive secrecy. If researchers stop publishing early-stage ideas to avoid being scooped by AI, the long-term progress and collaborative culture of mathematics and broader scientific fields could suffer serious damage. Tao specifically notes that the scarcity of good, fruitful open problems is being accelerated by AI's ability to rapidly "flatten" problems once they become known. The core concern is a structural change in research incentives, where the risk of AI-driven scooping discourages the open sharing of research directions.

rss · Simon Willison · Sep 9, 00:20

**Background**: Terence Tao is a renowned mathematician and Fields Medal laureate known for his prolific contributions across multiple areas of mathematics. Open science relies on researchers sharing problems, methods, and partial results to build collective knowledge. In mathematics and theoretical fields, open problems serve as crucial milestones that drive progress and collaboration.

**Tags**: `#AI Ethics`, `#Open Science`, `#Mathematics`, `#Research Incentives`, `#AI Impact`

---

<a id="item-8"></a>
## [348M Parameter Model Achieves 99.4% Accuracy on GPT-3 Arithmetic Benchmarks](https://www.reddit.com/r/MachineLearning/comments/1wc7hmu/i_trained_a_348m_model_trained_from_scratch_on/) ⭐️ 8.0/10

A researcher trained a 348M parameter model from scratch on 22.7B tokens and fine-tuned it to explicitly show mathematical reasoning steps like column addition and partial-product multiplication. The model achieves 99.4% average accuracy across nine GPT-3 arithmetic sub-tasks, outperforming GPT-3 175B on most tasks, and can handle clean arithmetic up to 14 digits after a simple vocabulary expansion. This achievement demonstrates that small language models can rival or exceed much larger models on specific reasoning tasks when trained with explicit chain-of-thought methodologies. It highlights the critical role of data efficiency, structured reasoning traces, and vocabulary design in unlocking mathematical capabilities without relying on massive parameter counts. The model's initial 8-digit ceiling was caused by a limited vocabulary of place names, which was resolved by expanding the list from 6 to 19 entries. While it excels at arithmetic, it struggles with word problems (4% on GSM8K) due to operation selection errors, requires greedy decoding to maintain valid reasoning traces, and currently lacks division capabilities.

reddit · r/MachineLearning · /u/nkthebass · Sep 10, 03:28

**Background**: Chain-of-thought prompting is a technique that improves AI reasoning by instructing models to generate intermediate steps rather than jumping directly to an answer. Traditional large language models often struggle with complex arithmetic because they rely on pattern matching rather than algorithmic execution. This experiment shows that embedding explicit, step-by-step mathematical procedures into a model's training data can significantly enhance its computational accuracy.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Chain-of-thought_prompting">Chain-of-thought prompting</a></li>

</ul>
</details>

**Tags**: `#Small Language Models`, `#Mathematical Reasoning`, `#Chain-of-Thought`, `#Model Training`, `#AI Benchmarks`

---

<a id="item-9"></a>
## [Fly Connectome Fails to Learn Pong, Revealing Critical Simulation Flaws](https://www.reddit.com/r/MachineLearning/comments/1wc67ci/i_tried_to_make_a_real_fly_connectome_learn_to/) ⭐️ 8.0/10

An engineer attempted to train a real fruit fly connectome subgraph to play Pong using dopamine-style plasticity, but the model failed to learn. The debugging process uncovered critical issues in neuPrint data extraction, missing neural pathways, and validation failures in recent viral connectome demos. This audit exposes the gap between impressive viral demos and actual functional neuromorphic learning, highlighting the need for rigorous validation in connectome-based AI. It provides a crucial reality check for the neuromorphic computing field and guides future research toward biologically accurate circuit simulation. The author fixed a neuPrint regex bug that zeroed out neuron populations, discovered missing intermediate layers between photoreceptors and motion detectors, and found that half of the motor neurons had zero sensory input. Even after rebuilding the circuit, the learning rule merely suppressed motor responses rather than improving performance.

reddit · r/MachineLearning · /u/oPeraza2007 · Sep 10, 02:28

**Background**: A connectome is a comprehensive map of neural connections in a brain, with the Drosophila (fruit fly) connectome being a major milestone in neuroscience. Neuromorphic computing attempts to mimic biological neural systems for AI tasks, often using real connectome data. Tools like neuPrint are used to query and analyze these complex neural graphs, but accurate data extraction and biological pathway mapping remain challenging.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Drosophila_connectome">Drosophila connectome - Wikipedia</a></li>
<li><a href="https://connectome-neuprint.github.io/neuprint-python/docs/">neuprint -python — neuprint -python 0.6.2 documentation</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neuromorphic_computing">Neuromorphic computing</a></li>

</ul>
</details>

**Tags**: `#connectomics`, `#neuromorphic-computing`, `#machine-learning`, `#debugging`, `#simulation-validation`

---

<a id="item-10"></a>
## [Essay Theorizes Software Development Drives People Insane](https://graybeard.ing/software-drives-people-insane/) ⭐️ 7.0/10

A reflective essay theorizes that the abstract, siloed, and rapidly shifting nature of software development contributes to psychological strain and burnout among developers. It argues that working in disconnected, abstract environments without direct customer feedback amplifies mental fatigue. This perspective highlights a growing mental health crisis in the tech industry, urging teams to reconsider development workflows and customer engagement strategies. Addressing these psychological stressors could improve developer retention, product quality, and overall industry sustainability. The author emphasizes that isolation from end-users and constant shifts in technology stacks create a disorienting work environment. Commenters note that direct customer interaction and smaller, focused teams historically mitigated these issues, contrasting with modern siloed development practices.

hackernews · rglover · Sep 10, 16:13 · [Discussion](https://news.ycombinator.com/item?id=49646181)

**Background**: Software development often involves working with abstract logic, complex systems, and rapidly evolving frameworks that can feel disconnected from tangible outcomes. Modern development practices frequently separate engineers from end-users through layers of management and project coordination, which can obscure the real-world impact of the code being written.

**Discussion**: Commenters largely agree that isolation from users and overcomplicated tech shifts drive developer burnout, with some attributing the issue to internet culture rather than software itself. Others highlight historical examples of small, focused teams building critical systems efficiently, suggesting that modern siloed structures and market misinterpretations by tech leaders exacerbate the problem.

**Tags**: `#software engineering`, `#developer psychology`, `#industry culture`, `#team dynamics`, `#hackernews`

---

<a id="item-11"></a>
## [Cognition Launches SWE-2 Model Rivaling GPT-Astra and Fable 5.1](https://cognition.com/blog/swe-2) ⭐️ 7.0/10

Cognition has released SWE-2, its most advanced software engineering model to date, claiming performance comparable to frontier models like GPT-Astra and Fable 5.1 while reducing costs by up to 64%. The model is post-trained from Kimi K3 using a single reinforcement learning run with linear cost penalties and introduces configurable effort levels. This release intensifies competition in the AI coding assistant market by offering a potentially more cost-effective alternative to closed-weight frontier models. It highlights the growing industry trend of leveraging post-training and reinforcement learning to enhance existing base models rather than training entirely new architectures from scratch. SWE-2 lacks a published SWE-bench Verified score due to recent benchmark saturation, and Cognition has not disclosed token pricing or context window specifications. Community analysis reveals a significant performance drop on newer benchmarks, raising questions about overfitting and generalization capabilities.

hackernews · seelos · Sep 10, 15:29 · [Discussion](https://news.ycombinator.com/item?id=49645443)

**Background**: SWE-bench is a widely used benchmark that evaluates AI models on their ability to resolve real-world GitHub issues, serving as a key metric for coding assistant capabilities. Open-weight models provide access to trained parameters for customization and transparency, differing from fully open-source AI which includes training data and code. Reinforcement learning (RL) post-training is increasingly used to align models with specific tasks like software engineering, often improving efficiency without requiring massive new compute resources.

<details><summary>References</summary>
<ul>
<li><a href="https://cognition.com/blog/swe-2">Introducing SWE - 2 : Pushing the Pareto Frontier | Cognition</a></li>
<li><a href="https://genztech.blog/models/cognition-swe-2/">Cognition SWE - 2 for Coding — Benchmarks, Pricing & Specs (2026)</a></li>
<li><a href="https://alphasignal.ai/news/cognition-s-swe-2-beats-gpt-5-6-sol-at-64-lower-cost">Cognition 's SWE - 2 Beats GPT-5.6 Sol at 64% Lower Cost | AlphaSignal</a></li>

</ul>
</details>

**Discussion**: Community sentiment is highly skeptical, with users pointing out a massive performance delta between older and newer benchmarks that suggests severe overfitting. Commenters also criticize the lack of transparency regarding model weights and pricing, while noting that the model is merely a post-trained version of Kimi K3 rather than a novel architecture.

**Tags**: `#AI Coding Assistants`, `#Model Benchmarking`, `#Open-Weight Models`, `#Software Engineering AI`, `#AI Transparency`

---

<a id="item-12"></a>
## [PlanetScale Launches Neki, a Closed-Source Sharded Postgres Tool](https://planetscale.com/blog/introducing-neki) ⭐️ 7.0/10

PlanetScale has introduced Neki, a new closed-source database sharding and management tool designed to scale Postgres across multiple servers to handle hundreds of millions of queries per second. The tool adds a router, sidecars, and a control plane to enable horizontal scaling beyond a single machine. This launch is significant because it brings advanced database sharding capabilities to Postgres, potentially enabling developers to manage massive data workloads more efficiently. However, its closed-source nature and the CEO's controversial marketing approach have sparked intense debate within the developer community. Neki is currently closed-source, though PlanetScale has stated it will be released as an open-source project once tested in real production workloads. The architecture relies on real Postgres instances for each shard, augmented by PlanetScale's proprietary routing and control plane components.

hackernews · simon_weber · Sep 10, 15:43 · [Discussion](https://news.ycombinator.com/item?id=49645686)

**Background**: Database sharding is a horizontal scaling technique that partitions data across multiple database servers to improve performance and manage large datasets. While Postgres is a highly popular relational database, scaling it horizontally has traditionally been complex, often requiring third-party tools or custom implementations. PlanetScale, known for its work on Vitess (a database clustering system for MySQL), is now applying similar sharding expertise to Postgres.

<details><summary>References</summary>
<ul>
<li><a href="https://planetscale.com/neki">Neki — PlanetScale | Sharded Postgres by the Team Behind Vitess.</a></li>
<li><a href="https://neki.dev/?ref=upstract.com">Sharded Postgres by PlanetScale | Neki</a></li>
<li><a href="https://en.wikipedia.org/wiki/Database_sharding">Database sharding</a></li>

</ul>
</details>

**Discussion**: Community sentiment is largely critical, with users expressing frustration over the tool's closed-source status, the CEO's aggressive marketing tactics, and the blog post's failure to clearly explain what Neki actually is. Some users also noted the heavy advertising push, while others sarcastically questioned its necessity for small-scale projects.

**Tags**: `#Database`, `#Sharding`, `#PlanetScale`, `#Systems Engineering`, `#Infrastructure`

---

<a id="item-13"></a>
## [Raymond Chen Reveals Windows XP Default User Picture Selection Algorithm](https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683) ⭐️ 7.0/10

Microsoft veteran Raymond Chen published a detailed explanation of the specific algorithm Windows XP used to select a default user profile picture from a directory of images during initial account creation. He broke down the exact implementation logic and filesystem interaction patterns used by the operating system. This deep dive into legacy Windows internals highlights the engineering discipline and optimization trade-offs required in early operating system development. It provides valuable historical context and practical filesystem efficiency insights for modern systems programmers and software historians. The algorithm was specifically designed to minimize filesystem calls and reduce physical I/O overhead by avoiding redundant directory reads. Community members have located and shared the corresponding source code from the leaked Windows NT 5 codebase to verify the implementation.

hackernews · soheilpro · Sep 10, 09:04 · [Discussion](https://news.ycombinator.com/item?id=49640646)

**Background**: Windows XP, released in 2001, was a landmark operating system that introduced many user interface features still familiar today, including customizable user profile pictures. When a new account was created, the system automatically assigned one of several default images rather than leaving it blank. Understanding how the OS efficiently scanned directories and managed file system resources in that era provides context for modern software optimization challenges.

<details><summary>References</summary>
<ul>
<li><a href="https://devblogs.microsoft.com/oldnewthing/20260909-00/?p=112683">What algorithm did Windows XP use to choose your initial user ...</a></li>
<li><a href="https://energylast.com/technical-information/what-algorithm-did-windows-xp-use-to-choose-your-initial-user-picture/">What Algorithm Did Windows XP Use To Choose Your Initial User ...</a></li>

</ul>
</details>

**Discussion**: The community expressed strong appreciation for Chen's technical insights, with some users sharing the actual source code from the NT5 repository. Discussions focused on filesystem caching efficiency, the trade-offs between physical I/O and kernel cache hits, and reflections on how modern development pressures often erode the careful engineering discipline seen in legacy systems.

**Tags**: `#Windows Internals`, `#Systems Programming`, `#Software History`, `#Algorithm Design`

---

<a id="item-14"></a>
## [Sony Faces Lawsuit Over Digital Game Ownership Claims](https://consumerrights.wiki/w/Sony_PlayStation_digital_game_ownership_lawsuit) ⭐️ 7.0/10

A curated list has surfaced documenting Sony's past marketing language claiming players "own" their digital games, contrasting with its recent legal defense that consumers only purchase a revocable, non-transferable license. This discrepancy is central to a proposed class action lawsuit challenging PlayStation Store's terms of service. The case challenges the standard digital licensing model used across the gaming and software industries, potentially forcing companies to clarify ownership rights and consumer protections. A ruling against Sony could impact how digital storefronts handle refunds, account bans, and the long-term preservation of purchased media. Sony's Terms of Service include a binding arbitration agreement and class action waiver in Section 14, requiring users to opt out in writing within 30 days. The company argues that digital purchases are merely licenses, citing that multiple users can buy the same game simultaneously as proof that true ownership isn't transferred.

hackernews · haunter · Sep 10, 12:18 · [Discussion](https://news.ycombinator.com/item?id=49642531)

**Background**: Digital storefronts like the PlayStation Store typically sell games under End User License Agreements (EULAs) rather than transferring actual ownership. This means publishers retain control over the software and can revoke access under certain conditions, unlike physical media which can be resold or lent. Recent industry shifts have sparked consumer backlash over the lack of permanence and resale rights for digital purchases.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techpowerup.com/352232/sony-legally-argues-that-digital-game-ownership-is-not-plausible?cp=3">Sony Legally Argues That Digital Game Ownership ... | TechPowerUp</a></li>
<li><a href="https://kotaku.com/fans-put-together-a-list-of-every-time-sony-said-players-owned-their-digital-games-after-the-company-argued-in-a-lawsuit-that-it-was-obvious-players-dont-2000733271">A List Of Times Sony Told People They Own Their Digital Games</a></li>
<li><a href="https://www.fakta.co/gamers-boycott-sony-digital-licensing">Gamers Launch Boycott Over Sony Digital Licensing and Disc Sunset</a></li>

</ul>
</details>

**Discussion**: Commenters strongly criticize Sony's use of binding arbitration and class action waivers as tactics to strip consumer rights. Many highlight the contradiction between Sony's past marketing language and its current legal stance, with some noting the logical flaws in Sony's defense regarding simultaneous purchases. Overall sentiment reflects deep skepticism toward corporate digital licensing practices.

**Tags**: `#consumer-rights`, `#digital-ownership`, `#legal-tech`, `#gaming`, `#terms-of-service`

---

<a id="item-15"></a>
## [OpenAI Releases ChatGPT Images 2.5 with Improved Precision and Speed](https://simonwillison.net/2026/Sep/8/introducing-chatgpt-images-25/) ⭐️ 7.0/10

OpenAI has released ChatGPT Images 2.5, introducing two new API models—gpt-image-2.5-sunburst and gpt-image-2.5-flare—that offer better instruction-following, faster response times, and improved subject preservation in reference photos. Sunburst is optimized for precision editing workflows, while Flare is designed for fast, high-quality everyday image generation. This update significantly enhances OpenAI's image generation ecosystem, which already powers over 3 billion images, by giving developers and creators more control over editing precision and generation speed. The dual-model approach allows users to choose the right balance of quality and latency for their specific workflows, accelerating adoption in both creative and enterprise applications. The Sunburst model supports up to 16 reference images in a single request with optional masking, and generation is handled asynchronously via the API. Community tools like Simon Willison's openai_image.py CLI have already been updated to support multi-image reference inputs for the new models.

rss · Simon Willison · Sep 8, 22:46

**Background**: OpenAI's GPT-Image series provides text-to-image and image-to-image generation capabilities through its API, allowing developers to integrate AI-generated visuals into applications. The models support natural language prompts, reference image inputs, and flexible output sizes, with asynchronous processing to handle computationally intensive generation tasks. Version 2.5 builds on the previous GPT-Image 2 release by refining instruction-following across multi-turn interactions and improving consistency when editing existing images.

<details><summary>References</summary>
<ul>
<li><a href="https://www.orcarouter.ai/blog/gpt-image-2-5-flare-sunburst">GPT - Image - 2 . 5 Flare vs Sunburst : New OpenAI Image APIs</a></li>
<li><a href="https://zenn.dev/neotechpark/articles/514d034e19f370">GPT - Image - 2 . 5 Flare vs Sunburst : Which Model Should You Use?</a></li>
<li><a href="https://www.atlascloud.ai/models/openai/gpt-image-2.5-sunburst/edit">GPT Image 2.5 Sunburst Edit (I2I) API Image by OPENAI ... | Atlas Cloud</a></li>

</ul>
</details>

**Tags**: `#AI`, `#Image Generation`, `#OpenAI`, `#API`, `#Machine Learning`

---

<a id="item-16"></a>
## [Stanford Professor Launches Free 'Probability for AI' Course with 1:10 Teaching Ratio](https://www.reddit.com/r/MachineLearning/comments/1wbf3ox/teach_ml_community_service_project_from_stanford_n/) ⭐️ 7.0/10

Stanford professor Chris Piech has launched a free community service project called 'Probability for AI,' starting October 9th, which features a 1:10 teacher-to-student ratio and interactive AI-assisted learning tools. Over 1,000 volunteers have already applied to teach the course, which aims to make probability education accessible to those with light math backgrounds. This initiative significantly lowers the barrier to entry for understanding the mathematical foundations of AI, potentially democratizing access to high-quality ML education. By leveraging a volunteer-driven model and AI tools, it offers a scalable approach to personalized learning that could influence broader educational practices in tech. The course utilizes interactive tools like a free coding agent to help students build an AI text detection app within an hour, and teachers will train using 'teachable agents' based on Stanford's decades of pedagogical research. The project is fully funded by an alumnus, ensuring all tools and servers remain free for participants.

reddit · r/MachineLearning · /u/chrispiech · Sep 9, 07:54

**Background**: Probability and statistics form the mathematical backbone of machine learning, governing how models learn from data and make predictions. 'Teachable agents' are AI systems designed around the 'learning by teaching' paradigm, where students improve their own understanding by instructing an AI character. Coding agents are autonomous AI tools that assist with writing, reviewing, and debugging software, making complex programming tasks more accessible to beginners.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Teachable_agent">Teachable agent</a></li>
<li><a href="https://grokipedia.com/page/Coding_agent">Coding agent</a></li>

</ul>
</details>

**Tags**: `#Machine Learning Education`, `#Stanford University`, `#AI Literacy`, `#Community Service`, `#Probability for AI`

---

<a id="item-17"></a>
## [Clarifying What Sante's 83.83 Score on DiagnosisArena-MCQ Actually Measures](https://www.reddit.com/r/MachineLearning/comments/1wbkxsa/what_santes_8383_on_diagnosisarenamcq_actually/) ⭐️ 7.0/10

Ant Ling's new medical reasoning model, Ling-3.0-flash-Sante, achieved a score of 83.83 on the DiagnosisArena-MCQ benchmark, which evaluates multiple-choice diagnosis selection when case evidence and candidate options are provided. The analysis clarifies that this high score reflects performance in selecting from supplied alternatives, not the ability to generate unrestricted differentials or determine necessary clinical investigations. This clarification is crucial for preventing the misinterpretation of benchmark scores in medical AI, ensuring that developers and clinicians understand the specific clinical reasoning capabilities being measured. It highlights the need for comprehensive evaluation profiles, combining multiple benchmarks like MedXpertQA-Text and HealthBench Professional, to accurately assess a model's readiness for real-world clinical applications. The release also reports scores of 53.88 on MedXpertQA-Text and 45.73 on HealthBench Professional, though the latter uses physician-written rubrics rather than percentage accuracy. The analysis notes that the HealthBench Professional score lacks detail on whether it is length-adjusted, making direct comparisons with other published results difficult without further verification.

reddit · r/MachineLearning · /u/Expert_Coffee_203 · Sep 9, 13:01

**Background**: DiagnosisArena is a recently introduced benchmark designed to rigorously assess professional-level diagnostic competence in large language models. While many medical benchmarks focus on text-based multiple-choice questions, clinical reasoning in practice often involves generating differential diagnoses from scratch, identifying missing patient history, and deciding which tests to order next. Evaluating AI models across diverse tasks, such as open-ended clinical chats and challenging medical QA, provides a more holistic view of their capabilities beyond standardized exam formats.

<details><summary>References</summary>
<ul>
<li><a href="https://arxiv.org/html/2505.14107v1">DiagnosisArena: Benchmarking Diagnostic Reasoning for Large ...</a></li>
<li><a href="https://medxpertqa.github.io/">MedXpertQA</a></li>
<li><a href="https://arxiv.org/html/2604.27470">HealthBench Professional : Evaluating Large Language Models on...</a></li>

</ul>
</details>

**Tags**: `#Medical AI`, `#Benchmarking`, `#LLM Evaluation`, `#Clinical Reasoning`, `#Machine Learning`

---