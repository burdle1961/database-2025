from pymysql_connection import get_connection

cursor1 = get_connection().cursor()

sql = "SELECT 고객번호, 고객명, 이메일 FROM 고객 LIMIT 5"
cursor1.execute(sql)
result1 = cursor1.fetchall()
print("첫번째 fetch() 결과 : \n", result1)

cursor2 = get_connection().cursor()

# sql = "SELECT 직원번호, 이름, 직책 FROM 직원 LIMIT 5"
# cursor2.execute(sql)
# result2 = cursor2.fetchall()
sql = "SELECT 직원번호, 이름, 직책 FROM 직원"
cursor2.execute(sql)
result2 = cursor2.fetchmany(5)
print("두번째 fetch() 결과 : \n", result2)


print ("SELECT * from 고객, 직원 >> 카티션 곱 형태의 출력")
for record1 in result1 :
    for record2 in result2 :
        print (record1, record2)
    print("--------------")
