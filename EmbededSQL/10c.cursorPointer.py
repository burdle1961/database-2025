import pymysql.cursors

# cursor  동작 이해를 돕기 위한 코드로서,  client-side cursor에서만 동작함.
# cursor의 위치를 변경하는  fetchmany(-2)와 같이 음수 값은 공식적으로 지원되지 않으므로, 실제 사용시에는 주의하여야 함.

#Connect to the database(Cursor : Client-side cursor (cursor 영역을 client 내에 생성)
connection = pymysql.connect(host='localhost',
                             port= 3306,        # maria DB 설치 시의 port 번호로 변경 (예. 3309)
                             user='root',
                             password='burdle', # 비밀번호 변경
                             database='sample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.Cursor)

with connection:
    with connection.cursor() as cursor:

        print (f"0. Row count 값 : SQL 실행 전 ({cursor.rowcount})", end=" ==> ")
        sql = "SELECT `id`, `password` FROM `users`"
        cursor.execute(sql)
        print (f"후 ({cursor.rowcount})")
        input()

        print (f"1. Row number 값 : fetch 실행 전 ({cursor.rownumber})", end=" ==> ")
        result = cursor.fetchmany(3)
        print (f"후 ({cursor.rownumber}), 결과 : {result}")
        input()
        
        print (f"2. Row number 값 : fetch 실행 전 ({cursor.rownumber})", end=" ==> ")
        result = cursor.fetchmany(2)
        print (f"후 ({cursor.rownumber}), 결과 : {result}")
        input()

        print (f"3. Row number 값 : fetch 실행 전 ({cursor.rownumber})", end=" ==> ")
        result = cursor.fetchmany(-2)
        print (f"후 ({cursor.rownumber}), 결과 : {result}")
        input()

        print (f"4. Row number 값 : fetch 실행 전 ({cursor.rownumber})", end=" ==> ")
        result = cursor.fetchmany(1)
        print (f"후 ({cursor.rownumber}), 결과 : {result}")
        input()

        print (f"5. Row number 값 : fetch 실행 전 ({cursor.rownumber})", end=" ==> ")
        result = cursor.fetchmany(3)
        print (f"후 ({cursor.rownumber}), 결과 : {result}")
