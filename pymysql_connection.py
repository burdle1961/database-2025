# db_connection.py
import pymysql.cursors

def get_connection():
    connection = pymysql.connect(
        host='localhost',
        port=3306,           # 필요한 포트로 변경
        user='root',
        password='burdle',   # 비밀번호 설정
        database='sample',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection