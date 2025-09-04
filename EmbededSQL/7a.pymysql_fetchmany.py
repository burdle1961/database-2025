from pymysql_connection import get_connection

# Connect to the database
connection = get_connection()

with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchmany(2)
        print(result)

# fetchmany()와 유사한  SELECT 명령의 option은 ?
# SELECT * from users limit 2
