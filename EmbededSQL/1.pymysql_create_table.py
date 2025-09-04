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

sql = """CREATE TABLE `users` ( \
	`id` int(11) NOT NULL AUTO_INCREMENT, \
	`email` varchar(255) COLLATE utf8_bin NOT NULL, \
	`password` varchar(255) COLLATE utf8_bin NOT NULL, \
	PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin \
        AUTO_INCREMENT=1"""

cursor.execute(sql)

connection.close()
