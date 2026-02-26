from pathlib import Path

def generate_report(filename):
    try:
        # Avoid using shell commands to prevent command injection.
        return Path(filename).read_text(encoding="utf-8")
    except Exception:
        return ""