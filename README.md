# 🎯 InstaReporter  
  
<div align="center">  
  

**🚀 Advanced Instagram Content Reporting Tool**  
  
*Streamline your content moderation workflow with intelligent proxy rotation and multiprocessing* 
<img align="right" alt="count" src="https://count.getloli.com/get/@:ziddi-shop?theme=rule34">
[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)  
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)  
[![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)](https://github.com/ziddi-shop/Instagram-Report-Tool)  
  
</div>  
  
---  
  
## 🌟 Features  
  
### 🎯 **Dual Attack Modes**  
- **Profile Reporting**: Target specific Instagram user profiles with precision.
- **Video Content Reporting**: eport individual Instagram video posts efficiently.
  
  
### 🛡️ **Advanced Anonymity System**  
- **Dynamic Proxy Support**: Automatically harvests proxies from reliable online sources. 
- **Custom Proxy Lists**: Upload your own proxy list (up to 50 proxies)
- **User Agent Rotation**: Rotates through 90+ realistic browser user agents to mimic organic traffic.
- **Protocol Intelligence**: Auto-configures HTTP/HTTPS proxy protocols for compatibility
  
### 🎨 **Professional User Interface**  
**Colorized Console**: Clean, visually appealing terminal output with status indicators.
**Real-Time Monitoring**: Live tracking of reporting progress and transactions.
**Robust Error Handling**: Detailed diagnostics for quick troubleshooting. 
  
---  
  
## 🚀 Quick Start  
  
### Prerequisites  
  #Python: Version 3.7 or higher. Verify with:
```bash  
python --version  
```  
  
### Installation  
  
1. **Clone the repository**  
```bash  
git clone https://github.com/ziddi-shop/Instagram-Report-Tool.git  
cd InstaReporter  
```  
  
2. **Install dependencies**  
```bash  
pip install requests colorama asyncio proxybroker  
```  
  
3. **Run the application**  
```bash  
python main.py  
```  
  
---  
  
## 📋 Usage Guide  
  
### 🎯 **Interactive Mode**  
  
The application provides an intuitive step-by-step interface:  
  
1. **Proxy Configuration**  
   - Choose to use proxies or run without them  
   - Auto-harvest proxies from the internet  
   - Or provide your own proxy list file  
  
2. **Attack Mode Selection**  
   - `1` - Report Instagram profiles  
   - `2` - Report Instagram videos  
  
3. **Target Specification**  
   - Enter the username (for profiles)  
   - Enter the video URL (for videos)  
  
### 📁 **Proxy File Format**  
  
Create a text file with one proxy per line:  
```  
proxy1.example.com:8080  
proxy2.example.com:3128  
192.168.1.100:8080  
```  
  
---  
  
## 🏗️ Architecture Overview  
  
### 🔧 **Core Components**  
  
- **Main Orchestrator** (`main.py`): Process management and user interaction  
- **Attack Engine** (`libs/attack.py`): HTTP request handling and form submission  
- **Proxy Harvester** (`libs/proxy_harvester.py`): Automatic proxy discovery  
- **Utility Suite** (`libs/utils.py`): Console interface and file operations  
  
 
  

  
### 🎯 **Attack Process Flow**  
  
1. **Session Initialization**: Create HTTP session with proxy configuration  
2. **Authentication Chain**: Facebook → Instagram cookie extraction  
3. **Form Parameter Extraction**: Dynamic token and session data parsing  
4. **Report Submission**: POST request to Instagram's help infrastructure  
5. **Response Validation**: Success/error status verification  
  
---  
  
## ⚙️ Configuration  
  
### 🔧 **Performance Tuning**  
  
| Parameter | Default | Description |  
|-----------|---------|-------------|  
| Max Processes | 5 | Concurrent attack processes |  
| Proxies per Process | 10 | Proxy distribution ratio |  
| No-Proxy Requests | 10 | Fallback request count |  
| HTTP Timeout | 10s | Request timeout duration |  
  
### 🛡️ **Security Features**  
  
- **Dynamic User Agents**: Automatic browser user agent rotation  
- **Cookie Management**: Automatic session handling  
- **Error Resilience**: Comprehensive exception handling  
- **Protocol Flexibility**: HTTP/HTTPS proxy support  
  
---  
  
## 📊 System Requirements  
  
### 🖥️ **Minimum Requirements**  
- **OS**: Windows 7+, macOS 10.12+, Linux (any modern distro)  
- **Python**: 3.7 or higher  
- **RAM**: 512MB available memory  
- **Network**: Stable internet connection  
  
### 📦 **Dependencies**  
- `requests[socks]` - HTTP client with SOCKS proxy support  
- `colorama` - Cross-platform colored terminal text  
- `asyncio` - Asynchronous I/O operations  
- `proxybroker` - Proxy discovery and validation  
  
---  
  

  
### 📁 **Project Structure**  
  
```  
Instagram-Report-Tool/  
├── main.py          # Main application entry point  
├── libs/  
│   ├── attack.py            # Core attack functionality  
│   ├── proxy_harvester.py   # Automatic proxy discovery  
│   ├── user_agents.py       # Browser user agent rotation  
│   ├── utils.py             # Utility functions  
│   ├── logo.py              # Branding and UI elements  
│   └── check_modules.py     # Dependency validation  
└── README.md                # This file  
```  
  
### 🔍 **Key Functions**  
  
- `chunks()`: Proxy list segmentation for multiprocessing  
- `profile_attack_process()`: Profile reporting worker  
- `video_attack_process()`: Video reporting worker  
- `report_profile_attack()`: Core profile attack logic  
- `report_video_attack()`: Core video attack logic  
  
---  
  
## ⚠️ Legal Disclaimer  
  
This tool is designed for **educational and research purposes only**. Users are responsible for:  
  
✅ Adhere to Instagram’s Terms of Service.
✅ Comply with all applicable local and international laws.
✅ Use the tool ethically and responsibly.
❌ Avoid any form of harassment or malicious activity.
  
**The developers are not liable for any misuse of this software.**  
  
---  
  
## 🤝 Contributing  
  
We welcome contributions! Here's how you can help:  
  
1. **🍴 Fork the repository**  
2. **🌿 Create a feature branch** (`git checkout -b feature/amazing-feature`)  
3. **💾 Commit your changes** (`git commit -m 'Add amazing feature'`)  
4. **📤 Push to the branch** (`git push origin feature/amazing-feature`)  
5. **🔄 Open a Pull Request**  
  
### 🐛 **Bug Reports**  
Found a bug? Please open an issue with:  
- Detailed description  
- Steps to reproduce  
- Expected vs actual behavior  
- System information  
  
---  
  
## 📞 Support & Contact  
  
<div align="center">  
  
 
  
[![Instagram](https://img.shields.io/badge/Instagram-@foileds-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/yknowziddi)  
[![GitHub](https://img.shields.io/badge/GitHub-ziddi-shop-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/ziddi-shop)  
[![Email](https://img.shields.io/badge/Email-shehzadakingziddi@gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:shehzadakingziddi@gmail.com)  
  
</div>  
  
---  
  
## 📄 License  
  
This project is licensed under the **Educational License** - see the [LICENSE](LICENSE) file for details.  
  
---  
  
<div align="center">  
  
**⭐ If this project helped you, please give it a star! ⭐**  
  
*Made with ❤️ by [@ziddi-shop](https://github.com/ziddi-shop)*  
  
</div>
