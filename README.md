# 🎯 InstaReporter  
  
<div align="center">  

**🚀 Advanced Instagram Content Reporting  Tool**  
  
*Streamline your content moderation workflow with intelligent proxy rotation and multiprocessing* 
<img align="right" alt="count" src="https://count.getloli.com/get/@:ziddi-shop?theme=rule34">
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)  
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/ziddi-shop/Instagram-Report-Tool)  
  
</div>  
  
---  
  
🌟 Features
🎯 Dual Attack Modes

Profile Reporting: Target specific Instagram user profiles with precision.
Video Content Reporting: Report individual Instagram video posts efficiently.

⚡ High-Performance Architecture

Multiprocessing Engine: Supports up to 5 concurrent processes for optimal performance.
Smart Load Distribution: Automatically distributes 10 proxies per process for balanced workloads.
Intelligent Fallback: Seamlessly switches to no-proxy mode with 10 requests per process if proxies are unavailable.

🛡️ Advanced Anonymity

Dynamic Proxy Support: Automatically harvests proxies from reliable online sources.
Custom Proxy Lists: Upload your own proxy list (up to 50 proxies).
User Agent Rotation: Rotates through 90+ realistic browser user agents to mimic organic traffic.
Protocol Intelligence: Auto-configures HTTP/HTTPS proxy protocols for compatibility.

🎨 Professional User Interface

Colorized Console: Clean, visually appealing terminal output with status indicators.
Real-Time Monitoring: Live tracking of reporting progress and transactions.
Robust Error Handling: Detailed diagnostics for quick troubleshooting.


🚀 Quick Start
Prerequisites

Python: Version 3.7 or higher. Verify with:
bashpython --version


Installation

Clone the Repository
bashgit clone https://github.com/ziddi-shop/Instagram-Report-Tool.git
cd InstaReporter

Install Dependencies
bashpip install requests colorama asyncio proxybroker

Run the Application
python main.py



📋 Usage Guide
🎯 Interactive Mode
InstaReporter offers a streamlined, interactive interface:

Proxy Configuration

Choose to use proxies or run in no-proxy mode.
Auto-harvest proxies from the internet or provide a custom proxy list file.


Attack Mode Selection

1: Report Instagram profiles.
2: Report Instagram videos.


Target Specification

For profiles: Enter the Instagram username.
For videos: Provide the full video URL.



📁 Proxy File Format
Create a text file with one proxy per line in the format:
textproxy1.example.com:8080
proxy2.example.com:3128
192.168.1.100:8080

🏗️ Architecture Overview
🔧 Core Components

Main Orchestrator (main.py): Manages processes and user interactions.
Attack Engine (libs/attack.py): Handles HTTP requests and form submissions.
Proxy Harvester (libs/proxy_harvester.py): Automatically discovers and validates proxies.
Utility Suite (libs/utils.py): Provides console UI and file-handling utilities.

🔄 Workflow
#mermaid-diagram-mermaid-a8pjr7q{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#ccc;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-diagram-mermaid-a8pjr7q .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-a8pjr7q .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-diagram-mermaid-a8pjr7q .error-icon{fill:#a44141;}#mermaid-diagram-mermaid-a8pjr7q .error-text{fill:#ddd;stroke:#ddd;}#mermaid-diagram-mermaid-a8pjr7q .edge-thickness-normal{stroke-width:1px;}#mermaid-diagram-mermaid-a8pjr7q .edge-thickness-thick{stroke-width:3.5px;}#mermaid-diagram-mermaid-a8pjr7q .edge-pattern-solid{stroke-dasharray:0;}#mermaid-diagram-mermaid-a8pjr7q .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-diagram-mermaid-a8pjr7q .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-diagram-mermaid-a8pjr7q .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-diagram-mermaid-a8pjr7q .marker{fill:lightgrey;stroke:lightgrey;}#mermaid-diagram-mermaid-a8pjr7q .marker.cross{stroke:lightgrey;}#mermaid-diagram-mermaid-a8pjr7q svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-diagram-mermaid-a8pjr7q p{margin:0;}#mermaid-diagram-mermaid-a8pjr7q .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#ccc;}#mermaid-diagram-mermaid-a8pjr7q .cluster-label text{fill:#F9FFFE;}#mermaid-diagram-mermaid-a8pjr7q .cluster-label span{color:#F9FFFE;}#mermaid-diagram-mermaid-a8pjr7q .cluster-label span p{background-color:transparent;}#mermaid-diagram-mermaid-a8pjr7q .label text,#mermaid-diagram-mermaid-a8pjr7q span{fill:#ccc;color:#ccc;}#mermaid-diagram-mermaid-a8pjr7q .node rect,#mermaid-diagram-mermaid-a8pjr7q .node circle,#mermaid-diagram-mermaid-a8pjr7q .node ellipse,#mermaid-diagram-mermaid-a8pjr7q .node polygon,#mermaid-diagram-mermaid-a8pjr7q .node path{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-diagram-mermaid-a8pjr7q .rough-node .label text,#mermaid-diagram-mermaid-a8pjr7q .node .label text,#mermaid-diagram-mermaid-a8pjr7q .image-shape .label,#mermaid-diagram-mermaid-a8pjr7q .icon-shape .label{text-anchor:middle;}#mermaid-diagram-mermaid-a8pjr7q .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-diagram-mermaid-a8pjr7q .rough-node .label,#mermaid-diagram-mermaid-a8pjr7q .node .label,#mermaid-diagram-mermaid-a8pjr7q .image-shape .label,#mermaid-diagram-mermaid-a8pjr7q .icon-shape .label{text-align:center;}#mermaid-diagram-mermaid-a8pjr7q .node.clickable{cursor:pointer;}#mermaid-diagram-mermaid-a8pjr7q .root .anchor path{fill:lightgrey!important;stroke-width:0;stroke:lightgrey;}#mermaid-diagram-mermaid-a8pjr7q .arrowheadPath{fill:lightgrey;}#mermaid-diagram-mermaid-a8pjr7q .edgePath .path{stroke:lightgrey;stroke-width:2.0px;}#mermaid-diagram-mermaid-a8pjr7q .flowchart-link{stroke:lightgrey;fill:none;}#mermaid-diagram-mermaid-a8pjr7q .edgeLabel{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-diagram-mermaid-a8pjr7q .edgeLabel p{background-color:hsl(0, 0%, 34.4117647059%);}#mermaid-diagram-mermaid-a8pjr7q .edgeLabel rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-diagram-mermaid-a8pjr7q .labelBkg{background-color:rgba(87.75, 87.75, 87.75, 0.5);}#mermaid-diagram-mermaid-a8pjr7q .cluster rect{fill:hsl(180, 1.5873015873%, 28.3529411765%);stroke:rgba(255, 255, 255, 0.25);stroke-width:1px;}#mermaid-diagram-mermaid-a8pjr7q .cluster text{fill:#F9FFFE;}#mermaid-diagram-mermaid-a8pjr7q .cluster span{color:#F9FFFE;}#mermaid-diagram-mermaid-a8pjr7q div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:hsl(20, 1.5873015873%, 12.3529411765%);border:1px solid rgba(255, 255, 255, 0.25);border-radius:2px;pointer-events:none;z-index:100;}#mermaid-diagram-mermaid-a8pjr7q .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-diagram-mermaid-a8pjr7q rect.text{fill:none;stroke-width:0;}#mermaid-diagram-mermaid-a8pjr7q .icon-shape,#mermaid-diagram-mermaid-a8pjr7q .image-shape{background-color:hsl(0, 0%, 34.4117647059%);text-align:center;}#mermaid-diagram-mermaid-a8pjr7q .icon-shape p,#mermaid-diagram-mermaid-a8pjr7q .image-shape p{background-color:hsl(0, 0%, 34.4117647059%);padding:2px;}#mermaid-diagram-mermaid-a8pjr7q .icon-shape rect,#mermaid-diagram-mermaid-a8pjr7q .image-shape rect{opacity:0.5;background-color:hsl(0, 0%, 34.4117647059%);fill:hsl(0, 0%, 34.4117647059%);}#mermaid-diagram-mermaid-a8pjr7q :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}YesNoProfileVideoUser InputProxy ChoiceProxy HarvestingNo-Proxy ModeAttack Mode SelectionProfile or VideoProfile AttackVideo AttackMultiprocess ExecutionSuccess/Error Reporting
🎯 Attack Process Flow

Initialize an HTTP session with proxy configuration.
Extract cookies via Facebook → Instagram authentication chain.
Parse dynamic tokens and session data for form submissions.
Submit reports via POST requests to Instagram’s help infrastructure.
Validate responses and report success or errors.


⚙️ Configuration
🔧 Performance Tuning






























ParameterDefaultDescriptionMax Processes5Number of concurrent attack processesProxies per Process10Proxies assigned per processNo-Proxy Requests10Requests per process in no-proxy modeHTTP Timeout10sTimeout duration for HTTP requests
🛡️ Security Features

Dynamic User Agents: Rotates browser user agents to avoid detection.
Cookie Management: Handles session cookies automatically.
Error Resilience: Robust exception handling for reliable operation.
Protocol Flexibility: Supports both HTTP and HTTPS proxies.


📊 System Requirements
🖥️ Minimum Requirements

Operating System: Windows 7+, macOS 10.12+, or any modern Linux distribution.
Python: Version 3.7 or higher.
Memory: 512MB of available RAM.
Network: Stable internet connection.

📦 Dependencies

requests[socks]: HTTP client with SOCKS proxy support.
colorama: Cross-platform colored terminal output.
asyncio: Asynchronous I/O for efficient operations.
proxybroker: Proxy discovery and validation.


🛠️ Development
📁 Project Structure

├── main.py          # Main application entry point
├── libs/
│   ├── attack.py            # Core attack logic
│   ├── proxy_harvester.py   # Proxy discovery and validation
│   ├── user_agents.py       # User agent rotation
│   ├── utils.py             # Utility functions for UI and file ops
│   ├── logo.py              # Branding and UI elements
│   └── check_modules.py     # Dependency validation
└── README.md                # Project documentation
🔍 Key Functions

chunks(): Segments proxy lists for multiprocessing.
profile_attack_process(): Executes profile reporting tasks.
video_attack_process(): Executes video reporting tasks.
report_profile_attack(): Core logic for profile reporting.
report_video_attack(): Core logic for video reporting.


⚠️ Legal Disclaimer
InstaReporter is intended solely for educational and research purposes. Users must:

✅ Adhere to Instagram’s Terms of Service.
✅ Comply with all applicable local and international laws.
✅ Use the tool ethically and responsibly.
❌ Avoid any form of harassment or malicious activity.

The developers are not liable for any misuse of this software.

🤝 Contributing
We welcome contributions to improve InstaReporter! To contribute:

Fork the repository.
Create a feature branch: git checkout -b feature/amazing-feature.
Commit your changes: git commit -m 'Add amazing feature'.
Push to the branch: git push origin feature/amazing-feature.
Open a Pull Request.

🐛 Bug Reports
To report a bug, open an issue with:

A detailed description of the issue.
Steps to reproduce the bug.
Expected vs. actual behavior.
System information (OS, Python version, etc.).

  
## 📞 Support & Contact  
  
<div align="center">  
  

  
[![Instagram](https://img.shields.io/badge/Instagram-@ziddi-shop-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/yknowxziddi)  
[![GitHub](https://img.shields.io/badge/GitHub-ziddi-shop-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ziddi-shop)  
[![Email](https://img.shields.io/badge/Email-shehzadakingziddi@.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shehzadakingziddi@.com)  
  
</div>  
  
---  
  
## 📄 License  
  
This project is licensed under the **Educational License** - see the [LICENSE](LICENSE) file for details.  
  
---  
  
<div align="center">  
  
**⭐ If this project helped you, please give it a star! ⭐**  
  
*Made with ❤️ by [@ziddi-shop](https://github.com/ziddi-shop)*  
  
</div>
