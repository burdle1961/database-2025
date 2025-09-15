from pymysql_connection import get_connection

with get_connection() as connection:
    with connection.cursor() as cursor:
        
        # reuslt <--- select 의 결과 여러개의 레코드 읽기
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))

        result = cursor.fetchall()
        print(result)
