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
    con.start_transaction()
    cursor = con.cursor()
    sql = "INSERT into t_role(id,role) VALUE (%s,%s)"
    data = [
        ['3', '社会部'],
        ['4', '教师']
    ]
    cursor.executemany(sql, data)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)
