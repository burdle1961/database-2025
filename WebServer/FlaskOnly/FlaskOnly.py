from flask import Flask, request, jsonify, send_from_directory
import pymysql.cursors
from flask_cors import CORS

# Connect to the database
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='burdle',
                             database='sample',
                             charset='utf8',
                             cursorclass=pymysql.cursors.DictCursor)

app = Flask(__name__, static_folder='./flaskonly/build')

# React Development Mode에서는 CORS가 필요하지만, 
# Production Mode에서는 Flask가 프론트엔드를 서빙하므로 CORS가 필요하지 않습니다.
# 따라서 주석 처리하거나, 조건부로 적용할 수 있습니다.
# CORS(app)

# Flask API Endpoint
@app.route("/search", methods=["GET"])
def search():
    order = request.args.get("order", type=int)
    cursor = connection.cursor()
    query = "SELECT * FROM 주문 WHERE 주문번호 = %s"
    cursor.execute(query, (order,))
    results = cursor.fetchall()
    cursor.close()
    return jsonify(results)

# React 프론트엔드 정적 파일 서빙
@app.route("/", defaults={'path': ''})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    import os
    app.run(debug=True)
    connection.close()