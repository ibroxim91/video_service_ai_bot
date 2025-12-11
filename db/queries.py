from db.db import get_conn, put_conn

def execute_query(sql: str):
    conn = get_conn()
    try:
        with conn.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()

     
            if not rows:
                return None  

            #  [(Decimal('result'),)]
            if len(rows) == 1 and len(rows[0]) == 1:
                value = rows[0][0]

                # Decimal → int
                if isinstance(value, Decimal):
                    return int(value)

                
                if isinstance(value, (int, float)):
                    return int(value)

                return value  # fallback

            
            return rows

    finally:
        put_conn(conn)



