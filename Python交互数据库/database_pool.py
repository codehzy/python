import pymysql
import mysql.connector.pooling

config = {
    "host": "106.13.37.227",
    "port": 3306,
    "user": "news",
    "password": "hzy",
    "database": "news"
}

try:
    pool = mysql.connector.pooling.MySQLConnectionPool(
        **config,
        pool_size=10
    )
    con = pool.get_connection()
    # con.start_transaction()
    cursor = con.cursor()
    # sql = "UPDATE t_role SET role='new编辑' WHERE id = 2"
    sql = "TRUNCATE TABLE t_role"
    cursor.execute(sql)
    # con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
