from flask import Flask, request, jsonify
import pymysql.cursors
from flask_cors import CORS

#Connect to the database
connection = pymysql.connect(host='localhost',
                             port= 3306,        # maria DB 설치 시의 port 번호로 변경 (예. 3309)
                             user='root',
                             password='burdle', # 비밀번호 변경
                             database='sample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__)
CORS(app)  # React에서 요청 가능하게


@app.route("/search", methods=["GET"])
def search():
    order = request.args.get("order", type=int)

    cursor = connection.cursor()

    query = "SELECT * FROM 주문 WHERE 주문번호 = %s"
    cursor.execute(query, (order,))
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)
    connection.close()

