from pymysql_connection import get_connection

connection1 = get_connection()
cursor1 = connection1.cursor()

sql = "SELECT 고객번호, 고객명, 담당영업 FROM 고객"
cursor1.execute(sql)
result1 = cursor1.fetchall()

connection2 = get_connection()
cursor2 = connection2.cursor()

sql = "SELECT 직원번호, 이름 FROM 직원"
cursor2.execute(sql)
result2 = cursor2.fetchall()


print (result1)
print (result2)