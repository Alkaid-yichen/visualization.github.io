import pymysql
from flask import Flask
from flask import render_template
# 将字典转换为json格式
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def visualization():
    # return返回类型有两种：字符串、模板、Json格式字符串
    return render_template("main.html")

# 连接数据库的配置
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'alkaid',
    'db': 'shipmap',
    'charset': 'utf8'
}

def query_ship_data():
    # 连接数据库
    conn = pymysql.connect(**db_config)
    cursor = conn.cursor()

    # 执行查询
    cursor.execute("SELECT id, x, y, speed, direction, time, type FROM shipdata")
    data = cursor.fetchall()

    # 关闭连接
    cursor.close()
    conn.close()

    return data

@app.route('/mapid', methods=['GET'])
def get_ship_data():
    # 从数据库查询渔船数据
    fishing_boats_data = query_ship_data()
    return jsonify(fishing_boats_data)


if __name__ == '__main__':
    app.run()
