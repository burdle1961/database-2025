
from pymysql_connection import get_connection

cursor1 = get_connection().cursor()

sql = "SELECT 고객번호, 고객명, 담당영업 FROM 고객"
cursor1.execute(sql)
result1 = cursor1.fetchall()

cursor2 = get_connection().cursor()

for record1 in result1 :
    
    sql = "SELECT 직원번호, 이름 FROM 직원 WHERE 직원번호 = %s"
    cursor2.execute(sql, (record1['담당영업']))
    result2 = cursor2.fetchall()

    for record2 in result2 :
        print (record1, record2)