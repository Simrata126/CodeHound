# 🌐 VulScanner - Vulnerability Scanner Tool

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-v3.9-blue)
![Flask](https://img.shields.io/badge/flask-v2.0-lightgrey)

VulScanner is an open-source vulnerability scanner designed to help security enthusiasts and professionals conduct various assessments such as OSINT, port scanning, and vulnerability detection. It integrates the best open-source tools to provide seamless scanning, remediation, and reporting.

## 🔥 Features

- **OSINT**: Leverage tools like Sherlock and TheHarvester to gather information.
- **Port Scanning**: Use Nmap to identify open ports and services.
- **Vulnerability Scanning**: Execute Nuclei and SQLMap for detecting web vulnerabilities.
- **Remediation Suggestions**: Automatically get potential fixes based on the vulnerabilities found.
- **Documentation**: Generate detailed reports and logs from your scans.

## 🖼️ Screenshots

| Dashboard                       | Scanning Tools                      | Remediation Suggestions              |
| -------------------------------- | ----------------------------------- | ------------------------------------ |
| ![Dashboard](screenshots/dashboard.png) | ![Scanning](screenshots/scanning.png) | ![Remediation](screenshots/remediation.png) |

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.9+
- Flask (`pip install flask`)
- Nmap (`apt install nmap` or download from [here](https://nmap.org/download.html))
- Nuclei (`go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest`)
- SQLMap (`pip install sqlmap`)

### 2. Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/VulScanner.git
    cd VulScanner
    ```

2. Create a virtual environment and activate it:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # For Windows: venv\Scripts\activate
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Install and configure required tools:

    - **Nmap**: Follow [Nmap’s documentation](https://nmap.org/book/install.html).
    - **Nuclei**: Install using Go: `go install github.com/projectdiscovery/nuclei/v2/cmd/nuclei@latest`.
    - **SQLMap**: Install via pip: `pip install sqlmap`.

### 3. Run the Application

Start the Flask server:

```bash
python3 app.py

Access the dashboard in your browser at http://127.0.0.1:5000.

## 🔧 Usage

- **OSINT Section**: Input a username to gather intelligence using Sherlock.
- **Scanning Section**: Enter a domain or IP for scanning with Nmap and Nuclei.
- **Remediation Section**: View potential fixes for detected vulnerabilities.
- **Documentation**: Download and view reports from your previous scans.

## 🎨 UI Overview

The dashboard offers easy navigation between key features:

- **Home**: Displays a summary of your scanning tools.
- **OSINT**: Gather information using open-source intelligence tools.
- **Scanning**: Run detailed scans using Nmap, Nuclei, and SQLMap.
- **Remediation**: Get suggestions for fixing detected vulnerabilities.
- **Documentation**: Access reports and logs.

## ⚡ Tools Integrated

| Tool           | Description                                                     | Link                      |
| -------------- | --------------------------------------------------------------- | ------------------------- |
| **Nmap**       | Port scanning and network discovery.                             | [Nmap](https://nmap.org)   |
| **Nuclei**     | Fast vulnerability scanning with customizable templates.         | [Nuclei](https://nuclei.projectdiscovery.io) |
| **SQLMap**     | Automated SQL injection and database takeover tool.              | [SQLMap](https://sqlmap.org) |
| **Sherlock**   | OSINT username search across social media platforms.             | [Sherlock](https://github.com/sherlock-project/sherlock) |
| **TheHarvester**| Email, subdomain, and information gathering tool.               | [TheHarvester](https://github.com/laramies/theHarvester) |

## 📝 Contributing

We welcome contributions to improve VulScanner. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature-name`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push the branch (`git push origin feature/your-feature-name`).
5. Open a pull request.

## 🛡️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 💬 Contact

If you have any questions or need support, feel free to reach out:

- **Email**: simrata.126@gmail.com
- **LinkedIn**: [SimrataSingh](https://www.linkedin.com/in/simrata-singh-868b90200/)
