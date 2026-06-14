import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect("cleanup.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT,
        files_scanned INTEGER,
        files_deleted INTEGER,
        files_kept INTEGER,
        space_recovered REAL
    )
    """)

    conn.commit()
    conn.close()


def insert_log(scanned, deleted, kept, space):
    conn = sqlite3.connect("cleanup.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO logs (timestamp, files_scanned, files_deleted, files_kept, space_recovered)
    VALUES (?, ?, ?, ?, ?)
    """, (
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        scanned,
        deleted,
        kept,
        space
    ))

    conn.commit()
    conn.close()