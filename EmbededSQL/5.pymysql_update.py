from pymysql_connection import get_connection

# with get_connection() as connection:
connection = get_connection()
# with get_connection() as connection:

cursor = connection.cursor()

sql = "UPDATE users SET password = %s  WHERE id = %s"

cursor.execute(sql, ('xxx', 1))

connection.commit()

with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchall()
        print(result)
