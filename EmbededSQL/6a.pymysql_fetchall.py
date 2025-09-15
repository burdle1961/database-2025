from pymysql_connection import get_connection

with get_connection() as connection:
    with connection.cursor() as cursor:
        # reuslt <--- select 의 결과 여러개의 레코드 읽기
        #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        # `` backtick 문자를 사용하는 이유, 사용하지 않아도 되는 이유
        # sql = "select id, password from users where email = %s"  
        # sql = "SELECT * FROM users WHERE email LIKE %s" 
        tbl = input("테이블 명 : ")
        sql = "SELECT * FROM "+tbl

        # cursor.execute(sql, ('%@python.org%',))
        cursor.execute(sql)

        result = cursor.fetchall()
        print (result)

        for record in result :   
	        print(record)

        for i in range (0, len(result)) :
             print (i, result[i])