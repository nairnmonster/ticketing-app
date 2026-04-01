import sqlite3
from sqlite3 import Error

DB_NAME = "tickets.db"

def create_connection():
    """Create a database connection to SQLite database"""
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print(f"Database connection error: {e}")
    return None

def create_table():
    """Create the tickets table if it doesn't exist"""
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT DEFAULT 'open'
        )
    """)

    conn.commit()
    conn.close()

def add_ticket(title, description):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO tickets (title, description) VALUES (?, ?)",
                   (title, description))

    conn.commit()
    conn.close()

def get_all_tickets():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets")
    results = cursor.fetchall()

    conn.close()
    return results

def search_ticket(ticket_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM tickets WHERE id = ?", (ticket_id,))
    result = cursor.fetchone()

    conn.close()
    return result

def update_ticket(ticket_id, title, description, status):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE tickets 
        SET title = ?, description = ?, status = ?
        WHERE id = ?
    """, (title, description, status, ticket_id))

    conn.commit()
    conn.close()

def delete_ticket(ticket_id):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM tickets WHERE id = ?", (ticket_id,))

    conn.commit()
    conn.close()
