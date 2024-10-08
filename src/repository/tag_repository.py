from psycopg2.extensions import connection

def get_by_id(conn:connection, tag_id:int):
    cursor = conn.cursor()
    cursor.execute(f"""
        SELECT 
            tag_name 
        FROM 
            tag
        WHERE 
            tag_id = {tag_id}            
    """)
    result = cursor.fetchone()
    cursor.close()
    return result[0]