from db.db import get_conn, put_conn

def execute_query(sql: str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            result = cursor.fetchall()
            return result
    finally:
        put_conn(conn)  


