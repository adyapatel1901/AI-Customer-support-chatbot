import sqlite3
from datetime import datetime

DATABASE = "database/chatbot.db"


def get_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            sender TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            issue TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_message(session_id, sender, message):

    connection = get_connection()

    connection.execute(
        """
        INSERT INTO messages
        (session_id, sender, message, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            session_id,
            sender,
            message,
            datetime.now().isoformat()
        )
    )

    connection.commit()
    connection.close()


def get_messages(session_id):

    connection = get_connection()

    messages = connection.execute(
        """
        SELECT sender, message
        FROM messages
        WHERE session_id = ?
        ORDER BY id ASC
        """,
        (session_id,)
    ).fetchall()

    connection.close()

    return messages


def create_ticket(session_id, issue):

    connection = get_connection()

    cursor = connection.execute(
        """
        INSERT INTO tickets
        (session_id, issue, status, created_at)
        VALUES (?, ?, ?, ?)
        """,
        (
            session_id,
            issue,
            "Open",
            datetime.now().isoformat()
        )
    )

    ticket_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return ticket_id