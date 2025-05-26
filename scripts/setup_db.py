import sqlite3
from lib.db.connection import get_connection

def setup_database():
    with open('lib/db/schema.sql', 'r') as f:
        schema = f.read()


    conn = get_connection()
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()
    print("Database setup complete!")

if __name__ == "__main__":
    setup_database()