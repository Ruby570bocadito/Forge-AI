"""Report generation for AIHACK.

This module was referenced across the CLI (``src/cli_app.py``,
``src/cli_commands/scan_commands.py`` and ``src/cli_commands/commands/scan.py``)
but was missing from the repository. It provides the two entry points the CLI
expects:

* ``create_quick_report(target, result, assessment_type) -> str``
* ``generate_report(target, findings, assessment_type, format) -> str``

Reports are written to the repository-local ``reports/`` directory (gitignored)
and the returned value is the absolute path to the generated file.
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

from src.tools.utils import sanitize_filename

# Repository root = parents[2] relative to src/reports/generator.py
REPORTS_DIR = Path(__file__).resolve().parents[2] / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)


def _timestamp() -> str:
    return datetime.now().strftime("%Y%m%d_%H%M%S")


def _stringify_output(result: Any) -> str:
    if isinstance(result, dict):
        output = result.get("output", "")
    else:
        output = result
    if isinstance(output, list):
        return "\n".join(str(line) for line in output)
    return str(output)


def create_quick_report(
    target: str,
    result: Optional[Dict[str, Any]] = None,
    assessment_type: str = "scan",
) -> str:
    """Create a lightweight markdown report and return its path."""
    result = result if isinstance(result, dict) else {}
    output = _stringify_output(result)
    error = result.get("error") if isinstance(result, dict) else ""

    safe_target = sanitize_filename(target or "unknown")
    filename = f"{safe_target}_{assessment_type}_{_timestamp()}.md"
    path = REPORTS_DIR / filename

    lines = [
        f"# AIHACK Report — {target}",
        "",
        f"- **Assessment type:** {assessment_type}",
        f"- **Generated:** {datetime.now().isoformat(timespec='seconds')}",
        "",
        "## Output",
        "",
        "```",
        output[:20000],
        "```",
    ]
    if error:
        lines += ["", "## Errors", "", "```", str(error)[:5000], "```"]

    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)


def generate_report(
    target: str,
    findings: Optional[List[Dict[str, Any]]] = None,
    assessment_type: str = "Assessment",
    format: str = "html",
) -> str:
    """Generate a report in the requested format and return its path.

    Supported formats: html, md/markdown, json (pdf falls back to markdown).
    """
    findings = findings or []
    fmt = (format or "md").lower()
    safe_target = sanitize_filename(target or "unknown")
    safe_type = sanitize_filename(assessment_type or "assessment")

    ext = {
        "html": "html",
        "htm": "html",
        "md": "md",
        "markdown": "md",
        "json": "json",
        "pdf": "md",
    }.get(fmt, "md")

    path = REPORTS_DIR / f"{safe_target}_{safe_type}_{_timestamp()}.{ext}"

    if ext == "json":
        payload = {
            "target": target,
            "assessment_type": assessment_type,
            "generated": datetime.now().isoformat(timespec="seconds"),
            "findings": findings,
        }
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
        return str(path)

    if ext == "html":
        rows = "".join(
            f"<li><strong>{f.get('title', f.get('name', 'Finding'))}</strong>"
            f" &mdash; {f.get('severity', 'N/A')}<br>{f.get('description', '')}</li>"
            for f in findings
        )
        html = (
            "<!DOCTYPE html>\n"
            '<html><head><meta charset="utf-8"><title>AIHACK Report</title>\n'
            "<style>body{font-family:sans-serif;margin:2rem}h1{color:#333}"
            "li{margin:.5rem 0}</style></head>\n"
            f"<body><h1>AIHACK Report &mdash; {target}</h1>\n"
            f"<p><b>Assessment type:</b> {assessment_type}<br>"
            f"<b>Generated:</b> {datetime.now().isoformat(timespec='seconds')}</p>\n"
            f"<h2>Findings ({len(findings)})</h2>\n"
            f"<ul>{rows or '<li>No findings</li>'}</ul>\n"
            "</body></html>\n"
        )
        path.write_text(html, encoding="utf-8")
        return str(path)

    # Markdown fallback
    lines = [
        f"# AIHACK Report — {target}",
        "",
        f"- **Assessment type:** {assessment_type}",
        f"- **Generated:** {datetime.now().isoformat(timespec='seconds')}",
        "",
        f"## Findings ({len(findings)})",
        "",
    ]
    for f in findings:
        title = f.get("title", f.get("name", "Finding"))
        severity = f.get("severity", "N/A")
        lines.append(f"- **{title}** [{severity}]")
        if f.get("description"):
            lines.append(f"  {f.get('description')}")
    lines.append("")
    path.write_text("\n".join(lines), encoding="utf-8")
    return str(path)
