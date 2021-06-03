# 导出SQL文件 
# mysqldump -uroot -p [ no-data ]  逻辑库 > 路径
# mysqldump 数据库用户名 -p手动输入密码 no-data值导出表结构 逻辑库名 导出路径

# 导入SQL文件
-- USE demo
-- SOURCE backup.sql