import os

# configuration values should be pulled from environment variables to avoid hardcoding secrets
DB_NAME = os.environ.get("DB_NAME", "app.db")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

# any other secret values can be fetched by callers directly from the environment

def get_database_url():
    return f"sqlite:///{DB_NAME}"
