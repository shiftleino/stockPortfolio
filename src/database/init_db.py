import database.db_connection as db


def drop_tables(conn):
    """Removes the tables users and stocks from the database.

    Args:
        conn (SQLite3 Connection): The connection to the database.
    """
    cursor = conn.cursor()
    sql = "DROP TABLE IF EXISTS users"
    cursor.execute(sql)
    sql2 = "DROP TABLE IF EXISTS stocks"
    cursor.execute(sql2)
    conn.commit()


def create_tables(conn):
    """Creates new tables users and stocks in the database.

    Args:
        conn (SQLite3 Connection): The connection to the database.
    """
    cursor = conn.cursor()
    sql = """CREATE TABLE users (
        id integer primary key autoincrement, 
        username text UNIQUE, 
        password text);"""
    cursor.execute(sql)
    sql2 = """CREATE TABLE stocks (
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
    """Initializes the an empty database with tables users and stocks.
    """
    conn = db.get_connection()
    drop_tables(conn)
    create_tables(conn)


if __name__ == "__main__":
    initialize_db()
