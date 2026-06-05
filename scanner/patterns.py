import re

PATTERNS = {
    "Password": [
        re.compile(r"password\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
        re.compile(r"passwd\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
        re.compile(r"pwd\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
    ],

    "API Key": [
        re.compile(r"api[_-]?key\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
        re.compile(r"token\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
        re.compile(r"secret\s*=\s*['\"]?([^'\"]+)['\"]?", re.IGNORECASE),
    ],

    "AWS Key": [
        re.compile(r"AKIA[0-9A-Z]{16}")
    ],

    "GitHub Token": [
        re.compile(r"ghp_[A-Za-z0-9]{36}")
    ],

    "JWT": [
        re.compile(r"eyJ[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+")
    ]
}
