from pymysql_connection import get_connection

# Connect to the database
connection = get_connection()

# cusor를 선언하고 2개를 읽고,
with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchmany(2)
        print("첫번째 읽기", result)

# cusor를 다시 선언하고 2개 읽기
with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchmany(2)
        print("두번째 읽기", result)
