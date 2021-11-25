from . import db_connection as db

def drop_tables(conn):
    cursor = conn.cursor()
    sql = "DROP TABLE IF EXISTS users"
    cursor.execute(sql)
    conn.commit()


def create_tables(conn):
    cursor = conn.cursor()
    sql = """CREATE TABLE users (
        id integer primary key autoincrement, 
        username text UNIQUE, 
        password text);"""
    cursor.execute(sql)
    conn.commit()


def initialize_db():
    conn = db.get_connection()
    drop_tables(conn)
    create_tables(conn)


if __name__ == "__main__":
    initialize_db()
