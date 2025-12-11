from psycopg2.extensions import cursor
from db.db import get_conn


def execute_query(sql: str) -> int:
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
    except:
        return "Неверный запрос"   
    return cursor.fetchone()[0]

