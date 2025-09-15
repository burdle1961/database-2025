
from pymysql_connection import get_connection

cursor1 = get_connection().cursor()
sql = "SELECT 직원번호, 이름, 직책 FROM 직원"
cursor1.execute(sql)
result1 = cursor1.fetchall()

cursor2 = get_connection().cursor()
sql = "SELECT 고객번호, 고객명, 도시, 담당영업 FROM 고객"
cursor2.execute(sql)
result2 = cursor2.fetchall()

for record1 in result1 :
    print (record1['직원번호'], record1['이름'], end = "  :  ")
    NotFirst = False
    for record2 in result2 :
        if (record1['직원번호'] == record2['담당영업']) :
            if NotFirst : 
                print (record1['직원번호'], record1['이름'], end = "  :  ")
            print (record2['고객명'], record2['도시'])
            NotFirst = True

    if not(NotFirst) : print()