import os

DB_NAME = os.getenv("DB_NAME", "app.db")
# Credentials should be provided via environment variables in production.
DB_CREDENTIALS = {
    "user": os.getenv("DB_USER", ""),
    "pwd": os.getenv("DB_PASS", ""),
}
SERVICE_TOKEN = os.getenv("SERVICE_TOKEN", "")

def get_database_url():
    return f"sqlite:///{DB_NAME}"