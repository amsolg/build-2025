# KEY010 - Microsoft Build 2025 Opening Keynote: Detailed Summary

## Date
2025-05-26

## Overview
The Microsoft Build 2025 opening keynote, led by Satya Nadella and joined by industry leaders such as Sam Altman, set the direction for the event by focusing on the evolution of AI, cloud, developer tools, and the agentic web. The keynote highlighted Microsoft's vision to empower developers and organizations through advancements in AI, open platforms, and productivity tools.

## Domains of Information

### 1. Developer Inspiration & Community
- Personal stories from developers about their journey into programming, the excitement of AI, and the sense of empowerment and limitless possibilities.
- Developers described programming and AI as "magical," and compared making AI available to everyone as giving everyone a superpower.
- Emphasis on the impact of software development in making the world better, enabling creativity, and empowering others.
- Developers highlighted the limitless and endless nature of ideas, and the importance of solving real-world problems and making a positive impact.

### 2. Platform Shifts & Historical Context
- Satya Nadella contextualized the current era as a major platform shift, comparing it to previous milestones: Win32 (1991), the Web Stack (1996), and Cloud/Mobile (2008).
- The 2025 shift is toward an open, scalable, agentic web, moving from vertically integrated apps to platforms enabling agent-based solutions.

### 3. Developer Tools & Ecosystem
- Visual Studio and VS Code: Over 50 million users for Visual Studio family, 150 million for GitHub, and 15 million for GitHub Copilot.
- Announcements:
  - Visual Studio: .NET 10 support, live preview, improved tooling, new debugger, monthly stable releases.
  - VS Code: 100th open release, improved multi-window support, easier staging.
  - GitHub: Enterprise momentum, focus on trust, security, compliance, auditability, and data residency.

#### Microsoft Fabric
- Microsoft Fabric is an end-to-end analytics platform that unifies data movement, data engineering, data integration, data science, real-time analytics, and business intelligence. It enables organizations to build and manage data-driven solutions at scale, supporting seamless integration with Azure and other Microsoft services.
- Fabric provides a single SaaS experience for all analytics workloads, with deep integration into Microsoft 365 and Power BI, making it easier for developers and analysts to collaborate and deliver insights.

#### NLWeb (Natural Language Web)
- NLWeb refers to the integration of natural language capabilities directly into web applications and platforms, enabling users to interact with software using conversational language.
- At Build 2025, NLWeb is highlighted as a key enabler for agentic applications, allowing developers to build web experiences where users can ask questions, assign tasks, and receive intelligent responses from AI agents.
- NLWeb leverages advancements in large language models and multimodal AI to support text, voice, and even image-based interactions within web environments.

#### Coding Agent (GitHub Copilot Agent)
- The keynote introduced a full coding agent built into GitHub, evolving Copilot from a pair programmer to a peer programmer.
- The coding agent can autonomously complete tasks such as bug fixes, new features, and code maintenance. Developers can assign issues directly to Copilot, which will create branches, generate pull requests, and follow secure workflows.
- The agent respects security boundaries, works in isolated branches, and integrates with GitHub Actions for CI/CD. It also supports code reviews and can collaborate with other agents.

#### Model Context Protocol (MCP)
- MCP is a protocol that allows developers to configure and control how AI agents interact with code, data, and infrastructure.
- In the keynote, MCP servers are mentioned as a way to ensure that coding agents only use developer-approved resources, maintaining security and compliance.
- MCP supports multi-agent orchestration, enabling complex workflows where different agents can collaborate on tasks such as SRE, code review, and deployment.

#### Digital Twin
- Digital twin technology enables the creation of virtual replicas of physical assets, systems, or processes. These digital models can be used for simulation, monitoring, and optimization.
- At Build 2025, digital twins are discussed as part of the broader agentic and AI ecosystem, where AI agents can interact with digital twins to automate management, predict maintenance needs, and optimize operations in real time.
- Integration with Azure Digital Twins and IoT services allows developers to build scalable, intelligent solutions for industries such as manufacturing, energy, and smart cities.

#### Azure AI Studio
- Azure AI Studio reached General Availability (GA), providing a unified platform for building, training, and deploying AI models and solutions. It offers integrated tools for prompt engineering, model evaluation, and deployment, supporting both open-source and proprietary models.
- The platform is designed for both code-first and low-code/no-code users, enabling rapid prototyping and production-scale AI deployments.

#### Surface Devices with AI Acceleration
- New Surface devices were announced featuring dedicated AI acceleration hardware, enabling on-device inferencing and improved performance for AI-powered applications.
- These devices are optimized for running Copilot and other AI workloads locally, supporting privacy, responsiveness, and offline scenarios.

#### GitHub Copilot Everywhere
- Copilot is being integrated across the Microsoft ecosystem, including Visual Studio, VS Code, Windows, and web experiences.
- The keynote highlighted Copilot's evolution from code completion to chat, multi-file edits, agents, and now full task automation and peer programming.

#### Visual Studio & VS Code Enhancements
- Visual Studio: Announced support for .NET 10, live preview at design time, improved Git tooling, a new cross-platform debugger, and a move to monthly stable releases.
- VS Code: Celebrated its 100th open release, with new features like improved multi-window support and enhanced staging directly in the editor.

#### GitHub Enterprise & Security
- GitHub Enterprise continues to gain momentum, with a focus on trust, security, compliance, auditability, and data residency.
- New features and controls were introduced to help organizations manage code, agents, and workflows securely at scale.

#### Open Source Copilot in VS Code
- Microsoft announced the open sourcing of Copilot in VS Code, integrating AI-powered capabilities directly into the core open-source repository.
- This move aims to foster community contributions and transparency in the development of AI coding assistants.

#### Expanded: App Modernization via Copilot
- Copilot’s new Agent mode can upgrade frameworks (e.g., Java 8 to Java 21, .NET 6 to .NET 9) and migrate on-premise apps to the cloud.
- It creates a plan for code and dependencies, suggests fixes, learns from developer changes, and makes the modernization process seamless.

#### Expanded: SRE Agent
- Introduction of an autonomous Site Reliability Engineering (SRE) agent that can triage, root-cause, and mitigate live site issues.
- The SRE agent logs incident management reports as GitHub issues, including all repair items, which can then be assigned to Copilot for resolution.

#### Expanded: GitHub Copilot as a Peer Programmer
- Copilot can now be assigned issues (bug fixes, new features, code maintenance) and will autonomously complete these tasks, create branches, generate PRs, and follow secure workflows.
- Copilot’s workflow includes setting up branches, using GitHub Actions to generate compute or create virtual machines, and committing draft PRs to session logs for review.

#### Expanded: Security & Workflow Controls
- Copilot agents work in isolated branches, use only developer-configured MCP servers, and require code reviews before CI/CD or merge.
- Emphasis on an open and secure agent ecosystem, with controls for both individual developers and IT.
- Partners can build their own agents (SRE, SWE, code review, etc.), ensuring a broad and secure ecosystem.

#### Expanded: OpenAI Codex Agent
- Mention of OpenAI’s Codex agent, recently launched, and its integration with GitHub and developer workflows.
- Codex enables a real agentic coding experience, acting as a virtual teammate that can be assigned work and operate autonomously.
- Deep integration with GitHub allows for advanced task delegation and parallel workstreams.

#### Expanded: Model Roadmap & Capabilities
- Discussion of the evolution of AI models: becoming smarter, simpler to use, more reliable, and more multimodal.
- The vision for “it just works” AI, with automatic tool use and integration, and fewer models to choose from as they become more general and capable.
- Models will be more trustworthy, feature-rich, and support multimodal interactions (text, voice, images, etc.).

#### Expanded: Multi-Agent Orchestration
- The future of building agentic apps includes multi-agent orchestration, model scaffolding, and high-scale, stateful applications.
- Developers are encouraged to leverage new tools and workflows to build production-grade, stateful, agentic applications.

#### Expanded: Developer Workflow Transformation
- Early adopters of Codex changed their workflow significantly, achieving much more than before.
- The keynote highlighted the transformative impact of adopting agentic tools and workflows on developer productivity.

#### Expanded: The Challenge of Rapid Change
- The difficulty of keeping up with the rapid pace of technological change and the need for app servers and infrastructure that can adapt quickly.
- Developers are encouraged to plan for continual increases in model power and to lean into new tools and workflows.

#### Expanded: Specific Product Mentions
- Redis and staging cache are mentioned in the context of a bug/feature Copilot is assigned to fix, illustrating real-world integration with modern infrastructure components.

#### Expanded: Collaboration & Partnership
- The ongoing partnership between Microsoft and OpenAI, and the collaborative vision for the future of software engineering, is emphasized.
- The keynote underscores the importance of collaboration between organizations to drive innovation in AI and developer tools.

### 4. Open Source & AI Integration
- Open sourcing Copilot in VS Code, integrating AI-powered capabilities directly into the core open-source repo.
- AI is now central to coding, with Copilot evolving from code completions to chat, multi-file edits, and agents.

### 5. Agentic Web & AI Agents
- The rise of agentic applications: users can ask questions, assign tasks, and collaborate with AI agents.
- Copilot's new capabilities:
  - App modernization (e.g., upgrading frameworks, migrating apps to the cloud).
  - Autonomous SRE agent for site reliability engineering (triages, mitigates, and logs incidents).
  - Full coding agent in GitHub: Copilot can autonomously complete tasks, bug fixes, and new features.
- Security: Agents work in isolated branches, use developer-configured MCP servers, and support code reviews and CI/CD controls.
- Open ecosystem: Partners can build their own agents (SRE, SWE, code review, etc.).

### 6. Collaboration with OpenAI
- Sam Altman (OpenAI) joined virtually to discuss the evolution of agentic coding and the vision for software engineering.
- Highlights:
  - The emergence of virtual teammates (coding agents) that can be assigned work and operate autonomously.
  - Deep integration with GitHub, enabling advanced task delegation and parallel workstreams.
  - The rapid progress in model capabilities, reliability, and ease of use (multimodality, tool integration, "it just works").
  - Advice for developers: Embrace the rapid rate of change, plan for increasing model power, and leverage new tools for building high-scale, stateful, agentic applications.

### 7. Vision for the Future
- Microsoft and OpenAI are committed to making AI and agentic tools accessible, reliable, and secure for all developers.
- The keynote encourages developers to build the next generation of agentic apps, orchestrate multi-agent systems, and drive innovation at scale.

## Links & Resources
- [Official Microsoft Build 2025 Event Page](https://learn.microsoft.com/en-us/events/build/)
- [Microsoft Copilot Overview](https://www.microsoft.com/en-us/microsoft-copilot)
- [Azure AI Documentation](https://learn.microsoft.com/en-us/azure/)
- [Surface Devices](https://www.microsoft.com/surface/devices/surface-pro)
- [Microsoft Build Blog](https://techcommunity.microsoft.com/t5/microsoft-build-blog/bg-p/MicrosoftBuildBlog)
- [Official Microsoft News Center](https://news.microsoft.com/build2025/)
- [Watch the full keynote on demand](https://build.microsoft.com/en-US/ondemand/keynote)

> Referenced in: [keynotes/KEY010.md](../keynotes/KEY010.md)
