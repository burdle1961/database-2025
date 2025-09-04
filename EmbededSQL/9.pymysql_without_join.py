
from pymysql_connection import get_connection

cursor1 = get_connection().cursor()

sql = "SELECT 고객번호, 고객명, 이메일, 담당영업 FROM 고객"
cursor1.execute(sql)
result1 = cursor1.fetchall()

cursor2 = get_connection().cursor()

sql = "SELECT 직원번호, 이름, 직책 FROM 직원"
cursor2.execute(sql)
result2 = cursor2.fetchall()

for record1 in result1 :
    for record2 in result2 :
        if (record1['담당영업']==record2['직원번호']) :
            print (record1, record2)