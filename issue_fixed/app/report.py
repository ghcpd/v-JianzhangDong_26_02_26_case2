def generate_report(filename):
    # Read file directly to prevent command injection
    # This is safer than using subprocess with shell commands
    try:
        with open(filename, 'r') as f:
            return f.read()
    except (FileNotFoundError, OSError, IOError):
        return ""
