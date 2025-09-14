from flask import Flask, request, render_template
import pymysql.cursors
from datetime import date

app = Flask(__name__)

# DB 연결
connection = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='burdle',
    database='sample',
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

def convert_dates(rows):
    """datetime.date 객체를 문자열로 변환"""
    for row in rows:
        for k, v in row.items():
            if isinstance(v, date):
                row[k] = v.strftime("%Y-%m-%d")
    return rows

@app.route("/", methods=["GET", "POST"])
def index():
    orders = []
    order_number = ""
    if request.method == "POST":
        order_number = request.form.get("order")
        if order_number:
            cursor = connection.cursor()
            query = "SELECT 주문번호, 고객번호, 주문날짜, 배송날짜, 상태 FROM 주문 WHERE 주문번호 = %s"
            cursor.execute(query, (order_number,))
            results = cursor.fetchall()
            cursor.close()
            orders = convert_dates(results)

    return render_template("index.html", orders=orders, order_number=order_number)

if __name__ == "__main__":
    app.run(debug=True)
