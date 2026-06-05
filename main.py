import sys
from datetime import datetime
from scanner.detector import scan_directory
from scanner.git_scanner import scan_git_history
from scanner.reporter import save_json_report, save_html_report


def banner():
    print("=" * 50)
    print("      CredSleuth - Credential Leak Scanner")
    print("=" * 50)


def main():
    # Validate the new multi-argument routing schema
    if len(sys.argv) != 3 or sys.argv[1] not in ["scan", "git"]:
        print("Usage:")
        print("  python main.py scan <directory>")
        print("  python main.py git <repo_path>")
        return

    mode = sys.argv[1]
    target = sys.argv[2]

    banner()

    # Track the exact time the scan starts
    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Route execution based on execution flag choice
    if mode == "scan":
        findings, scanned_files = scan_directory(target)
    else:  # mode == "git"
        findings = scan_git_history(target)
        scanned_files = 0  # History parsing evaluates streams rather than file items

    # Initialize severity counters early
    critical = 0
    high = 0
    medium = 0

    for finding in findings:
        if finding["severity"] == "Critical":
            critical += 1
        elif finding["severity"] == "High":
            high += 1
        elif finding["severity"] == "Medium":
            medium += 1

        # Print current runtime progress to terminal
        print(
            f"[{finding['severity']}] "
            f"[{finding['type']}] "
            f"{finding['file']} "
            f"(Line {finding['line']})"
        )
        print(f"    {finding['value']}")
        print()

    # Calculate dynamic environment risk score threat metrics
    risk_score = (critical * 10) + (high * 5) + (medium * 2)

    if not findings:
        print("[+] No secrets found.")

    # Save artifact metrics outputs
    save_json_report(findings)
    
    save_html_report(
        findings=findings,
        critical=critical,
        high=high,
        medium=medium,
        scan_time=scan_time,
        target=f"[{mode.upper()}] {target}",
        risk_score=risk_score,
        scanned_files=scanned_files
    )

    # Print terminal screen execution breakdown
    print("\nScan Summary")
    print("-" * 30)
    print(f"Scan Mode      : {mode.upper()}")
    print(f"Scan Target    : {target}")
    print(f"Scan Time      : {scan_time}")
    if mode == "scan":
        print(f"Files Scanned  : {scanned_files}")
    print(f"Total Findings : {len(findings)}")
    print(f"Risk Score     : {risk_score}")
    print("-" * 30)
    print(f"Critical       : {critical}")
    print(f"High           : {high}")
    print(f"Medium         : {medium}")
    print("-" * 30)
    print()


if __name__ == "__main__":
    main()
