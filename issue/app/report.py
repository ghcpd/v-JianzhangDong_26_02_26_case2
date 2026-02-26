import os

def generate_report(filename):
    command = f"type {filename}"
    return os.popen(command).read()