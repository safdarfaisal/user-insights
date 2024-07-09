import sqlite3

def initialize_database():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()

    with open('user-insights/create_tables.sql', 'r') as f:
        c.executescript(f.read())

    with open('user_insights/insert_data.sql', 'r') as f:
        c.executescript(f.read())

    conn.commit()
    conn.close()

if __name__ == '__main__':
    initialize_database()
