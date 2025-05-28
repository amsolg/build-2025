# Model Context Protocol (MCP)

## Date
2025-05-26

## Overview
During the Microsoft Build 2025 Opening Keynote, Microsoft introduced the Model Context Protocol (MCP), a standardized protocol that allows developers to configure and control how AI agents interact with code, data, and infrastructure. This protocol represents a significant advancement in secure AI integration for development workflows.

## Details
- **Secure Resource Access**: MCP ensures that coding agents only use developer-approved resources, maintaining security and compliance boundaries.
- **Configuration Control**: Developers can explicitly define what resources, tools, and data AI agents can access and use.
- **Standardized Interface**: Provides a consistent way for AI systems to interact with development environments and tools.
- **Multi-Agent Support**: Enables orchestration between different specialized agents that can collaborate on complex tasks.
- **Enterprise Governance**: Supports organizational policies for AI usage, including audit trails and permission management.

## Technical Implementation
MCP operates through:
- MCP servers that expose specific capabilities to AI agents
- Client integrations in tools like GitHub Copilot and VS Code
- Semantic Kernel package integration for developers building custom agents
- Lightweight programs that facilitate the connection between models and tools/resources

## Use Cases
The keynote highlighted several key use cases for MCP:
- **Security Boundaries**: Ensuring AI agents operate only within approved perimeters
- **Workflow Integration**: Connecting AI capabilities with existing development workflows
- **Team Collaboration**: Enabling multiple agents with different specializations to work together
- **Custom Tool Access**: Providing AI agents with controlled access to organization-specific tools
- **Resource Management**: Controlling what data sources and computational resources agents can use

## Workflow Example
As demonstrated in the keynote:
1. A developer configures MCP servers with specific tool and resource access
2. AI agents (like GitHub Copilot) connect to these servers to access capabilities
3. When performing tasks, agents can only use the pre-approved resources
4. All interactions are logged and can be audited for security compliance

## Integration with Coding Agents
MCP is particularly important for GitHub Copilot agent functionality:
- Ensures agents only work with approved code repositories
- Controls deployment capabilities for automated workflows
- Manages access to sensitive systems and data
- Provides boundaries for code generation and modification

## Links & Resources
- [MCP Documentation](https://learn.microsoft.com/en-us/ai/mcp)
- [Semantic Kernel GitHub Repository](https://github.com/microsoft/semantic-kernel)
- [GitHub Copilot Security Documentation](https://docs.github.com/en/copilot)
- [Build Session: Securing AI Agent Access](https://build.microsoft.com/sessions)

> Referenced in: [keynotes/KEY010/KEY010-transcript-based-report.md](../KEY010-transcript-based-report.md)