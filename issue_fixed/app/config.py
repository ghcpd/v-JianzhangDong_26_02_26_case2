import os

# Load secrets from environment variables instead of hardcoding them
DB_SECRET = os.getenv("DB_SECRET", "default_secret")
SERVICE_TOKEN = os.getenv("SERVICE_TOKEN", "default_token")
DB_NAME = "app.db"

def get_database_url():
    return f"sqlite:///{DB_NAME}"
