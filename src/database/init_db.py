from . import db_connection as db


def drop_tables(conn):
    cursor = conn.cursor()
    sql = "DROP TABLE IF EXISTS users"
    cursor.execute(sql)
    sql2 = "DROP TABLE IF EXISTS stocks"
    cursor.execute(sql2)
    conn.commit()


def create_tables(conn):
    cursor = conn.cursor()
    sql = """CREATE TABLE users (
        id integer primary key autoincrement, 
        username text UNIQUE, 
        password text);"""
    cursor.execute(sql)
    sql2 = """CREATE TABLE IF NOT EXISTS stocks (
        id integer primary key autoincrement, 
        user_id integer,
        name text,
        ticker text,
        amount integer,
        price real,
        current real,
        currency text);"""
    cursor.execute(sql2)
    conn.commit()


def initialize_db():
    conn = db.get_connection()
    drop_tables(conn)
    create_tables(conn)


if __name__ == "__main__":
    initialize_db()
