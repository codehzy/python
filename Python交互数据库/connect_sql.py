# import mysql.connector
# import sshtunnel
#
# with sshtunnel.SSHTunnelForwarder(
#         ('106.13.37.227', 3306),
#         ssh_username='root',
#         ssh_password='hzy@1314',
#         remote_bind_address=('106.13.37.227', 3306),
#         local_bind_address=('127.0.0.1', 3306)
# ) as tunnel:
#     conn = mysql.connector.connect(
#         user="news",
#         password="hzy",
#         host="127.0.0.1",
#         port=3306,
#         database='news'
#     )
#
# # 游标
# cursor = conn.cursor()
# query = "select id,role FROM t_role;"
# cursor.execute(query)
# data = cursor.fetchall()
# print(data)
#
# import mysql.connector
#
# conn = mysql.connector.connect(
#     user="数据库",
#     password="hzy",
#     host="106.13.37.227",
#     port=3306,
#     database='news'
# )
# conn.close()

# 导入pymysql模块
import pymysql

# 连接database
connect = pymysql.Connect(
    host='106.13.37.227',
    port=3306,
    user='news',
    passwd='hzy',
    db='news',
    charset='utf8'
)

# 得到一个可以执行SQL语句的光标对象
cursor = connect.cursor()  # 执行完毕返回的结果集默认以元组显示
# connect
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 定义要执行的SQL语句
sql = "select * from t_type;"

# 执行SQL语句
cursor.execute(sql)

for one in cursor:
    print(one[0], one[1])

# 关闭光标对象
cursor.close()

# 关闭数据库连接
connect.close()
