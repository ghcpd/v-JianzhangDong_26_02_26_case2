import sqlite3
from .config import DB_NAME


def get_connection():
    return sqlite3.connect(DB_NAME)


def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    # only insert the admin user if it does not already exist
    cur.execute("SELECT 1 FROM users WHERE username = ?", ("admin",))
    if not cur.fetchone():
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", ("admin", "admin123"))
    conn.commit()
    conn.close()


def find_user(username):
    conn = get_connection()
    cur = conn.cursor()
    # use parameterized query to mitigate SQL injection
    cur.execute("SELECT * FROM users WHERE username = ?", (username,))
    result = cur.fetchone()
    conn.close()
    return result
