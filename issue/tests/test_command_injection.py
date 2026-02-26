import os
from app.report import generate_report

def test_command_injection_prevention(tmp_path):
    test_file = tmp_path / "safe.txt"
    test_file.write_text("safe content")

    result = generate_report(str(test_file))
    assert "safe content" in result

    malicious = f"{test_file}; echo hacked"
    result = generate_report(malicious)
    assert "hacked" not in result