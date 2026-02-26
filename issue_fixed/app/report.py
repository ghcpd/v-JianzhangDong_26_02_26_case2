import os


def generate_report(filename):
    # avoid executing shell commands; read file directly
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        # if file cannot be read, return empty string rather than executing arbitrary commands
        return ""