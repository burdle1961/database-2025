import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port= 3306,        # maria DB 설치 시의 port 번호로 변경 (예. 3309)
                             user='root',
                             password='burdle', # 비밀번호 변경
                             database='sample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()

sql = """DROP TABLE `users`"""

cursor.execute(sql)

connection.close()
