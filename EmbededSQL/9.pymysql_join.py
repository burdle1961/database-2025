from pymysql_connection import get_connection

cursor1 = get_connection().cursor()

sql = "SELECT 고객번호, 고객명, 직원번호, 이름 FROM 고객 c, 직원 e WHERE e.직원번호 = c.담당영업"
cursor1.execute(sql)
result1 = cursor1.fetchall()

for result in result1 :
    print (result)