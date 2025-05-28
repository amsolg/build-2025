# AI-Guided Robotics Demo

## Date
2025-05-28

## Overview
A centerpiece of the KEY040 session at Microsoft Build 2025 was the live demonstration of an AI-guided robot performing a practical task. This demo showcased the integration of advanced AI systems with physical robotics, demonstrating how language models, computer vision, and planning algorithms can work together to enable a robot to understand and execute real-world tasks.

## Details
- **Task Demonstration**: The robot was tasked with locating and retrieving a Coca-Cola can, a complex operation requiring multiple AI capabilities working in concert.
- **Voice Command Interaction**: The demo began with natural language instructions given to the robot, which were processed and understood by the AI system.
- **Real-time Performance**: Attendees witnessed the entire process from instruction to completion, with all processing and decision-making happening in real-time.
- **Problem-Solving Capabilities**: The robot demonstrated adaptive behaviors when encountering obstacles or challenges during task execution.

## Technical Implementation
The demo utilized several sophisticated technologies:

### Hardware Platform
- **Stretch 3 Robot**: An open-source research platform from Hello Robot was used as the physical agent
- **Sensor Array**: Multiple sensors provided environmental data, including:
  - Cameras for visual perception
  - Distance sensors for navigation
  - Tactile sensors for object manipulation
- **Articulated Arm**: Precision gripper for grasping and manipulating objects

### AI Components
- **Voice Recognition**: System for converting speech instructions to text
- **Natural Language Understanding**: Processing of text instructions into semantic meaning
- **Computer Vision**: Real-time object recognition and scene understanding
- **Path Planning**: Navigation algorithms for moving through physical space
- **Manipulation Planning**: Calculating precise movements for grasping objects
- **Task Orchestration**: Coordinating all components through Semantic Kernel

## Demo Workflow
The demonstration followed a structured sequence:

1. **Instruction Phase**: The robot received a voice command to fetch a Coca-Cola can
2. **Analysis & Planning**: The AI system:
   - Processed the request
   - Identified the target object
   - Generated a plan including navigation and retrieval steps
3. **Execution Phase**:
   - Navigation to the area where the can was located
   - Visual scanning to identify the specific object
   - Approach and positioning for optimal grasping
   - Precise manipulation to pick up the can
4. **Completion Phase**:
   - Return to the starting position
   - Delivery of the retrieved object
   - Confirmation of task completion

## Challenges & Adaptations
During the demonstration, several real-world challenges were encountered and addressed:

- **Lighting Variations**: Adjustments were made to handle changing light conditions affecting object recognition
- **Surface Transitions**: The robot adapted to different floor surfaces during navigation
- **Precision Grasping**: Fine motor adjustments were demonstrated when interacting with the can
- **Real-time Troubleshooting**: Presenters showed how to adjust system parameters when the robot encountered difficulties

## Impact & Significance
The demonstration illustrated several important advances:

- **Practical AI Application**: Moving beyond theoretical AI to real-world physical task execution
- **Multimodal Integration**: Showcasing how different AI systems can work together cohesively
- **Accessibility Implications**: Suggesting potential applications for assisting people with mobility limitations
- **Development Framework**: Providing a model for developers to build their own AI-robotics applications

## Audience Reaction
The demo generated significant engagement:
- Expressions of surprise at the robot's capabilities
- Questions about implementation details
- Discussion of potential applications
- Interest in development tools and frameworks

## Links & Resources
- [Hello Robot - Stretch 3 Platform](https://hello-robot.com)
- [Microsoft Semantic Kernel GitHub](https://github.com/microsoft/semantic-kernel)
- [AI & Robotics Integration Guide](https://learn.microsoft.com/ai-robotics)
- [Computer Vision Services](https://azure.microsoft.com/en-us/services/cognitive-services/computer-vision/)

> Referenced in: [keynotes/KEY040/KEY040-transcript-based-report.md](../KEY040-transcript-based-report.md)