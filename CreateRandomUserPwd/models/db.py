import sqlite3

create_user_table_sql="""
create table if not exists users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    email text,
    passwd text
)
"""


def connect_db(dbfile):
    conn = sqlite3.connect(dbfile)
    return conn

def create_user_table(conn):
    conn.execute(create_user_table_sql)

def execute_insert_sql(sql,conn):
    conn.execute(sql)
    conn.commit()

def execute_sql(sql,conn):
    cursor = conn.execute(sql)
    return cursor.fetchall()