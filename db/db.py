import os
from psycopg2.pool import SimpleConnectionPool

DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_DSN = f"host={DB_HOST} user={DB_USER} password={DB_PASSWORD} dbname={DB_NAME}"

pool = SimpleConnectionPool(minconn=1, maxconn=10, dsn=DB_DSN)

def get_conn():
    return pool.getconn()

def put_conn(conn):
    pool.putconn(conn)

def close_pool():
    pool.closeall()
