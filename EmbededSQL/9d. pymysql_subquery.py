
from pymysql_connection import get_connection

cursor1 = get_connection().cursor()
sql = "SELECT 담당영업, count(*) AS 고객수 FROM 고객 GROUP BY 담당영업"
cursor1.execute(sql)
result1 = cursor1.fetchall()

cursor2 = get_connection().cursor()
sql = "SELECT 직원번호, 이름 FROM 직원"
cursor2.execute(sql)
result2 = cursor2.fetchall()

for record1 in result1 :
    for record2 in result2 :
        if (record1['담당영업']==record2['직원번호']) :
            print (record2['직원번호'], record2['이름'], record1['고객수'])
