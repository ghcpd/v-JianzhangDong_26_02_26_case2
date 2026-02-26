import sqlite3
from .config import DB_NAME

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin123')")
    conn.commit()
    conn.close()

def find_user(username):
    conn = get_connection()
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cur.execute(query)
    result = cur.fetchone()
    conn.close()
    return result