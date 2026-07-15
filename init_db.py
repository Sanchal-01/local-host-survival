import sqlite3
from datetime import datetime

DATABASE_NAME = "database.db"


def init_db():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        sender_name TEXT NOT NULL,
        message_text TEXT NOT NULL,
        timestamp TEXT NOT NULL,
        is_broadcast INTEGER NOT NULL
    )
    """)

    connection.commit()
    connection.close()


def save_message(sender_name, message_text, is_broadcast):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
    INSERT INTO messages (
        sender_name,
        message_text,
        timestamp,
        is_broadcast
    )
    VALUES (?, ?, ?, ?)
    """, (
        sender_name,
        message_text,
        timestamp,
        int(is_broadcast)
    ))

    connection.commit()
    connection.close()


def get_all_messages():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT sender_name,
           message_text,
           timestamp,
           is_broadcast
    FROM messages
    ORDER BY id ASC
    """)

    messages = cursor.fetchall()

    connection.close()

    return messages


def get_broadcast_messages():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
    SELECT sender_name,
           message_text,
           timestamp
    FROM messages
    WHERE is_broadcast = 1
    ORDER BY id ASC
    """)

    alerts = cursor.fetchall()

    connection.close()

    return alerts


if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")