# 🔍 CredSleuth

> **Advanced Credential Leak Detection & Security Scanning Tool**

[![Python](https://img.shields.io/badge/Python-3.8+-3776ab?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-Officiallynith-333?logo=github)](https://github.com/Officiallynith)

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Scanning Modes](#scanning-modes)
- [Output Formats](#output-formats)
- [Configuration](#configuration)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**CredSleuth** is a powerful, lightweight credential leak detection tool designed to help security professionals and developers identify exposed secrets, API keys, passwords, and sensitive data in their codebase and Git history.

With dual scanning capabilities—filesystem scanning and Git history analysis—CredSleuth provides comprehensive coverage to catch credential leaks before they reach production.

### Why CredSleuth?

✅ **Multi-pattern Detection** - Identifies API keys, AWS credentials, database passwords, private keys, and more  
✅ **Dual Scanning Modes** - Scan directories or Git repositories  
✅ **Risk Scoring** - Severity-based classification (Critical, High, Medium)  
✅ **Beautiful Reports** - HTML and JSON outputs for documentation and automation  
✅ **Git History Analysis** - Catch secrets even in commit history  
✅ **Fast & Efficient** - Optimized scanning with minimal overhead  

---

## ✨ Features

### 🔐 Credential Detection
- **API Keys** - GitHub, AWS, Stripe, Twilio, SendGrid
- **Database Credentials** - MongoDB, PostgreSQL, MySQL connections
- **Private Keys** - SSH, RSA, DSA keys
- **Cloud Credentials** - AWS Access Keys, GCP, Azure
- **Tokens & Secrets** - Bearer tokens, OAuth tokens, JWT
- **Custom Patterns** - Extensible regex-based detection

### 📊 Reporting
- **JSON Reports** - Machine-readable format for CI/CD integration
- **HTML Reports** - Beautiful visual dashboards with metrics
- **Console Output** - Real-time scan progress with color-coded severity
- **Risk Scoring** - Quantified security risk assessment

### 🔍 Scanning Modes
- **Directory Scan** - Analyze entire directories recursively
- **Git History Scan** - Search through all commits and branches
- **Selective Testing** - Configurable patterns and exclusions

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Clone the Repository
```bash
git clone https://github.com/Officiallynith/CredSleuth.git
cd CredSleuth
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Verify Installation
```bash
python main.py
```

You should see the CredSleuth banner with usage instructions.

---

## ⚡ Quick Start

### Scan a Directory
```bash
python main.py scan /path/to/directory
```

### Scan Git History
```bash
python main.py git /path/to/git/repo
```

### Expected Output
```
==================================================
      CredSleuth - Credential Leak Scanner
==================================================

[Critical] [AWS_KEY] config.json (Line 42)
    AKIA3Q7XAMPLE9ABCDEF

[High] [DATABASE_URL] .env (Line 5)
    mongodb+srv://user:password@cluster.mongodb.net/db

[Medium] [PRIVATE_KEY] keys/id_rsa (Line 1)
    -----BEGIN RSA PRIVATE KEY-----

Scan Summary
-------------------------------
Scan Mode      : SCAN
Scan Target    : /path/to/directory
Scan Time      : 2026-06-05 21:45:30
Files Scanned  : 156
Total Findings : 3
Risk Score     : 24
-------------------------------
Critical       : 1
High           : 1
Medium         : 1
-------------------------------
```

---

## 📖 Usage

### Scan Mode

Recursively scans all files in a directory for credential patterns:

```bash
python main.py scan <directory_path>
```

**Parameters:**
- `directory_path` - Path to the directory to scan (relative or absolute)

**Output Files Generated:**
- `scan_report.json` - Detailed findings in JSON format
- `scan_report.html` - Interactive HTML report

### Git Mode

Analyzes Git repository history for credential leaks across all commits:

```bash
python main.py git <repo_path>
```

**Parameters:**
- `repo_path` - Path to the Git repository

**Output Files Generated:**
- `git_scan_report.json` - Git history findings
- `git_scan_report.html` - Git scan visual report

---

## 🎯 Scanning Modes

### 1. Directory Scanner
**Purpose:** Scan files in a directory structure  
**Best For:** 
- Pre-commit security checks
- Codebase audits
- Configuration file reviews

### 2. Git History Scanner
**Purpose:** Analyze repository commit history  
**Best For:**
- Security audits of existing repositories
- Finding accidental secrets committed in past
- Compliance reviews

---

## 📤 Output Formats

### JSON Report
```json
{
  "findings": [
    {
      "file": "config.json",
      "line": 42,
      "type": "AWS_KEY",
      "severity": "Critical",
      "value": "AKIA3Q7XAMPLE9ABCDEF",
      "timestamp": "2026-06-05T21:45:30"
    }
  ],
  "summary": {
    "total_findings": 3,
    "critical": 1,
    "high": 1,
    "medium": 1,
    "risk_score": 24
  }
}
```

### HTML Report
Beautiful interactive dashboard with:
- 📊 Risk score visualization
- 📈 Severity distribution charts
- 🔍 Detailed findings table
- ⏱️ Scan metadata and timing
- 🎨 Color-coded severity indicators

---

## ⚙️ Configuration

### .gitignore Integration
CredSleuth respects `.gitignore` patterns to avoid scanning unnecessary files:

```
# Example .gitignore entries (automatically respected)
node_modules/
*.log
.env.local
dist/
```

### Environment Variables
```bash
# Enable verbose logging
export CREDSLEUTH_VERBOSE=true

# Custom report directory
export CREDSLEUTH_REPORT_DIR=./security_reports
```

---

## 💡 Examples

### Example 1: Pre-commit Security Check
```bash
#!/bin/bash
python main.py scan . 
if [ -f scan_report.json ]; then
  FINDINGS=$(grep -c "Critical\|High" scan_report.json)
  if [ "$FINDINGS" -gt 0 ]; then
    echo "Security issues detected! Commit blocked."
    exit 1
  fi
fi
```

### Example 2: Audit Existing Repository
```bash
# Audit repository history
python main.py git /path/to/repo

# Open the generated HTML report
open git_scan_report.html  # macOS
xdg-open git_scan_report.html  # Linux
start git_scan_report.html  # Windows
```

### Example 3: CI/CD Integration
```yaml
# GitHub Actions Example
- name: Scan for Credential Leaks
  run: |
    pip install -r requirements.txt
    python main.py scan .
    
- name: Check Security Report
  run: |
    python -c "import json; report=json.load(open('scan_report.json')); exit(1 if report['summary']['risk_score'] > 20 else 0)"
```

---

## 📁 Project Structure

```
CredSleuth/
├── main.py                 # Entry point
├── requirements.txt        # Dependencies
├── README.md              # This file
├── LICENSE                # MIT License
├── scanner/
│   ├── detector.py        # Core credential detection logic
│   ├── git_scanner.py     # Git history scanning
│   └── reporter.py        # Report generation (JSON, HTML)
├── templates/
│   └── report.html        # HTML report template
├── test_files/            # Sample test cases
└── .gitignore             # Git ignore rules
```

---

## 🛠️ Technical Details

### Detection Patterns
CredSleuth uses regex-based pattern matching for multiple credential types:

| Pattern Type | Severity | Example |
|---|---|---|
| AWS Keys | Critical | `AKIA[0-9A-Z]{16}` |
| Private Keys | Critical | `-----BEGIN RSA PRIVATE KEY-----` |
| API Keys | High | Stripe, GitHub, SendGrid tokens |
| Database URLs | High | MongoDB, PostgreSQL connection strings |
| Bearer Tokens | High | OAuth and JWT tokens |
| Email Credentials | Medium | Email server credentials |

### Risk Scoring
```
Risk Score = (Critical × 10) + (High × 5) + (Medium × 2)

Score Interpretation:
0-10    → Low risk
11-25   → Medium risk
26-50   → High risk
50+     → Critical risk
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Areas for Contribution
- 🔐 Additional credential patterns
- 🌍 Multi-language support
- 📊 Enhanced reporting features
- ⚡ Performance optimizations
- 🧪 Test coverage improvements

---

## 🐛 Bug Reports & Feature Requests

Found a bug? Have an idea? Please [open an issue](https://github.com/Officiallynith/CredSleuth/issues) with:
- Clear description of the problem/request
- Steps to reproduce (for bugs)
- Expected vs. actual behavior
- Your environment details

---

## 📋 Security & Privacy

⚠️ **Important:** CredSleuth is designed for authorized security testing only. Ensure you have permission before scanning any codebase or repository.

**What CredSleuth Does NOT Do:**
- ❌ Does not store or transmit found credentials
- ❌ Does not modify files or repositories
- ❌ Does not track usage or data
- ❌ Does not require internet connection

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Inspired by leading security tools like TruffleHog, GitLeaks, and Detect Secrets
- Built with ❤️ for the security community
- Thanks to all contributors and users

---

## 📞 Support

- 📧 **Email:** security@officiallynith.com
- 💬 **Issues:** [GitHub Issues](https://github.com/Officiallynith/CredSleuth/issues)
- 🌐 **Website:** [GitHub Profile](https://github.com/Officiallynith)

---

## 🎖️ Status

![Build Status](https://img.shields.io/badge/Build-Passing-brightgreen)
![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776ab)
![Active Development](https://img.shields.io/badge/Status-Active-blueviolet)

---

<div align="center">

**⭐ If you find CredSleuth helpful, please consider starring the repository! ⭐**

Made with 🔒 Security in Mind

</div>
