import os

DB_PASSWORD = "SuperSecret123"
API_KEY = "hardcoded-api-key"
DB_NAME = "app.db"

def get_database_url():
    return f"sqlite:///{DB_NAME}"