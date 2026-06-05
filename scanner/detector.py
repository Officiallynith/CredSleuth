from pathlib import Path
from scanner.entropy import is_high_entropy
from scanner.patterns import PATTERNS
from scanner.reporter import get_severity

# Set of allowed extensions to optimize scanning and skip binary/unrelated files
ALLOWED_EXTENSIONS = {
    ".env",
    ".txt",
    ".py",
    ".js",
    ".json",
    ".yaml",
    ".yml",
    ".ini",
    ".conf",
    ".config",
    ".xml"
}


def scan_file(file_path):
    findings = []
    seen = set()  # Added to track and prevent duplicate findings

    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:

            for line_num, line in enumerate(f, start=1):
                matched_secret = False

                # 1. Regex-based pattern matching
                for secret_type, regex_list in PATTERNS.items():
                    for regex in regex_list:
                        matches = regex.finditer(line)
                        for match in matches:
                            value_raw = match.group(0)
                            
                            # Create a unique key for tracking
                            key = (str(file_path), line_num, secret_type, value_raw)
                            
                            if key not in seen:
                                seen.add(key)
                                findings.append({
                                    "file": str(file_path),
                                    "line": line_num,
                                    "type": secret_type,
                                    "severity": get_severity(secret_type),
                                    "value": value_raw.strip()
                                })
                            
                            matched_secret = True

                # 2. Heuristic-based Shannon Entropy checking (only if no regex matched)
                if not matched_secret:
                    words = line.split()
                    for word in words:
                        cleaned = word.strip("\"'()[]{}:,;")
                        if is_high_entropy(cleaned):
                            
                            # Clean, deduplicated key check with dynamic severity evaluation
                            key = (
                                str(file_path),
                                line_num,
                                "High Entropy Secret",
                                cleaned
                            )
                            
                            if key not in seen:
                                seen.add(key)
                                findings.append({
                                    "file": str(file_path),
                                    "line": line_num,
                                    "type": "High Entropy Secret",
                                    "severity": get_severity("High Entropy Secret"),
                                    "value": cleaned
                                })

    except Exception:
        pass

    return findings


def scan_directory(directory):
    all_findings = []
    scanned_files = 0  # Counter tracking tracked asset metrics

    for file in Path(directory).rglob("*"):

        if (
            file.is_file()
            and file.suffix.lower() in ALLOWED_EXTENSIONS
        ):
            scanned_files += 1
            all_findings.extend(scan_file(file))

    return all_findings, scanned_files
