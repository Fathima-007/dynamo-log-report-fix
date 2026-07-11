import json
from pathlib import Path

def test_report_exists():
    """Success criterion 1 (instruction.md): the agent must write a report to /app/report.json."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_valid_json():
    """Success criterion 1 (instruction.md): the report must be valid JSON."""
    data = json.loads(Path("/app/report.json").read_text())
    assert isinstance(data, dict), "report.json is not a JSON object"

def test_total_requests():
    """Success criterion 2 (instruction.md): total_requests must equal the number of log lines."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("total_requests") == 6, f"expected 6, got {data.get('total_requests')}"

def test_unique_ips():
    """Success criterion 3 (instruction.md): unique_ips must equal the number of distinct client IPs."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("unique_ips") == 3, f"expected 3, got {data.get('unique_ips')}"

def test_top_path():
    """Success criterion 4 (instruction.md): top_path must be the most frequently requested path."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("top_path") == "/index.html", f"expected /index.html, got {data.get('top_path')}"