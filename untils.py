import pymysql
from flask import jsonify

def get_conn():
    """
        :return: 连接，游标
    """
    #创建链接
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password="alkaid",
                           db="shipmap",
                           charset="utf8"
                           )
    # 创建游标
    cursor = conn.cursor()  # 执行完毕后返回的结果集默认以元组显示
    return conn, cursor

def close_conn(conn, cursor):
    cursor.close()
    conn.close()

def query(sql, *args):
    """
    封装通用查询
    :param sql:
    :param args:
    :return: 返回查询到的结果，((),(),)的形式
    """
    conn, cursor = get_conn()
    cursor.execute(sql, args)
    res = cursor.fetchall()
    close_conn(conn, cursor)
    return res

def get_shipdata():
    sql = """
            select * from shipdata
            """
    res = query(sql)
    return res

if __name__ == "__main__":
    data = get_shipdata()
    print(data)