import subprocess
from scanner.patterns import PATTERNS
from scanner.reporter import get_severity

def get_git_history(repo_path):
    """
    Executes 'git log -p' on the target repository to extract the full 
    commit history including all diff patches.
    """
    try:
        result = subprocess.run(
            ["git", "-C", repo_path, "log", "-p"],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except Exception:
        # Returns empty string if the path is not a git repo or git is missing
        return ""


def scan_git_history(repo_path):
    """
    Scans the extracted git patch history stream line by line 
    reusing the central patterns engine.
    """
    findings = []
    seen = set()  # Tracks uniqueness to prevent identical findings within the history stream

    history = get_git_history(repo_path)
    if not history:
        return findings

    lines = history.splitlines()

    for line_num, line in enumerate(lines, start=1):
        # Focus scan surface: optionally limit to code lines added in commits ("+")
        # If you want to scan raw lines including metadata/removals, keep as-is.
        
        for secret_type, regex_list in PATTERNS.items():
            for regex in regex_list:
                matches = regex.finditer(line)
                for match in matches:
                    value_raw = match.group(0)
                    
                    # Create a unique deduction composite signature key
                    key = ("git-history", line_num, secret_type, value_raw)
                    
                    if key not in seen:
                        seen.add(key)
                        findings.append({
                            "file": "git-history",
                            "line": line_num,
                            "type": secret_type,
                            "severity": get_severity(secret_type),
                            "value": value_raw.strip()
                        })

    return findings
