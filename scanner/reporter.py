import json
from jinja2 import Environment, FileSystemLoader

SEVERITY_MAP = {
    "AWS Key": "Critical",
    "GitHub Token": "Critical",
    "JWT": "High",
    "API Key": "High",
    "Password": "Medium",
    "High Entropy Secret": "High"
}


def get_severity(secret_type):
    return SEVERITY_MAP.get(secret_type, "Low")


def mask_secret(secret):
    if len(secret) <= 8:
        return "*" * len(secret)

    return (
        secret[:4]
        + "*" * (len(secret) - 8)
        + secret[-4:]
    )


def save_json_report(findings, filename="reports/report.json"):
    # Mask the findings before exporting to JSON
    safe_findings = []
    for finding in findings:
        copy = finding.copy()
        copy["value"] = mask_secret(finding["value"])
        safe_findings.append(copy)

    with open(filename, "w") as f:
        json.dump(safe_findings, f, indent=4)

    print(f"\n[+] Report saved: {filename}")


def save_html_report(
    findings,
    critical,
    high,
    medium,
    scan_time,
    target,
    risk_score,
    scanned_files,
    filename="reports/report.html"
):

    env = Environment(
        loader=FileSystemLoader("templates")
    )

    template = env.get_template(
        "report_template.html"
    )

    # Mask findings safely
    safe_findings = []
    for finding in findings:
        copy = finding.copy()
        copy["value"] = mask_secret(finding["value"])
        safe_findings.append(copy)

    html = template.render(
        findings=safe_findings,
        critical=critical,
        high=high,
        medium=medium,
        scan_time=scan_time,
        target=target,
        risk_score=risk_score,
        scanned_files=scanned_files
    )

    with open(filename, "w") as f:
        f.write(html)

    print(f"[+] HTML report saved: {filename}")
