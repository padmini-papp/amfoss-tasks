import sqlite3

conn = sqlite3.connect("bot.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id TEXT PRIMARY KEY,
        username TEXT,
        balance INTEGER DEFAULT 100,
        last_daily TEXT,
        last_rob TEXT
    )
""")
conn.commit()


def get_user(user_id, username):
    cursor.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
    user = cursor.fetchone()
    if user is None:
        cursor.execute(
            "INSERT INTO users (user_id, username, balance) VALUES (?, ?, 100)",
            (user_id, username)
        )
        conn.commit()
        return (user_id, username, 100, None, None)
    return user


def update_balance(user_id, amount):
    cursor.execute(
        "UPDATE users SET balance = balance + ? WHERE user_id = ?",
        (amount, user_id)
    )
    conn.commit()


def set_last_daily(user_id, timestamp):
    cursor.execute(
        "UPDATE users SET last_daily = ? WHERE user_id = ?",
        (timestamp, user_id)
    )
    conn.commit()


def set_last_rob(user_id, timestamp):
    cursor.execute(
        "UPDATE users SET last_rob = ? WHERE user_id = ?",
        (timestamp, user_id)
    )
    conn.commit()


def get_top_users(limit=5):
    cursor.execute(
        "SELECT username, balance FROM users ORDER BY balance DESC LIMIT ?",
        (limit,)
    )
    return cursor.fetchall()