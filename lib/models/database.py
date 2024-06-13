# database.py

import sqlite3

# SQLite database path
DATABASE_PATH = 'todo.db'

# Function to initialize database and create tasks table
def init_db():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    # Create tasks table if not exists
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    ''')

    conn.commit()
    conn.close()

# Initialize the database
if __name__ == '__main__':
    init_db()
