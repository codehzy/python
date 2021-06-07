import pymysql;

# connect = pymysql.Connect(
#     host='106.13.37.227',
#     port=3306,
#     user='news',
#     passwd='hzy',
#     db='news',
#     charset='utf8'
# )

# SQL注入
# username = "1 OR 1=1"
# password = "1 OR 1=1"
# sql = "SELECT COUNT(*) FROM t_user WHERE username=" + username + \
#       " AND AES_DECRYPT(UNHEX(password),'HelloWorld') =" + password
# cursor = connect.cursor()
# cursor.execute(sql)
# print(cursor.fetchone()[0])
# connect.close()

# # 使用SQL预编译机制抵御注入攻击
# username = "1 OR 1=1"
# password = "1 OR 1=1"
# sql = "SELECT COUNT(*) FROM t_user WHERE username=%s " \
#       "AND AES_DECRYPT(UNHEX(password),'HelloWorld')=%s"
# cursor = connect.cursor()
# cursor.execute(sql, (username, password))
# print(cursor.fetchone()[0])
# connect.close()

# 事务
import mysql.connector

try:
    connect = mysql.connector.connect(
        host='106.13.37.227',
        port=3306,
        user='news',
        passwd='hzy',
        db='news',
        charset='utf8'
    )
    connect.start_transaction()
    cursor = connect.cursor()
    sql = "INSERT INTO t_role(id,role)" \
          "VALUES(%s,%s)"
    cursor.execute(sql, (3,"编辑者"))
    connect.commit()
except Exception as e:
    if "connect" in dir():
        connect.rollback()
    print(e)
finally:
    if "connect" in dir():
        connect.close()
