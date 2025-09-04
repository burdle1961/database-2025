import pymysql.cursors

#Connect to the database
connection = pymysql.connect(host='localhost',
                             port= 3306,        # maria DB 설치 시의 port 번호로 변경 (예. 3309)
                             user='root',
                             password='burdle', # 비밀번호 변경
                             database='sample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
