-- SHOW DATABASES;
-- CREATE DATABASE demo;
use main;

CREATE TABLE student(
	id Int UNSIGNED PRIMARY KEY,
	name VARCHAR(20) NOT NULL,
	sex CHAR(1) NOT NULL,
	birthday DATE NOT NULL,
	tel CHAR(11) NOT NULL,
	remark VARCHAR(200)
);

INSERT INTO student VALUES(1,'何梓阳','男','1998-02-26','17601511257','你好');
SHOW TABLES;
DESC information_schema;
SHOW CREATE TABLE student;
DROP TABLE student;

-- 修改数据表结构
ALTER TABLE student
ADD address VARCHAR(200) NOT NULL,
ADD home_tel CHAR(11) Not NULL;

ALTER TABLE student
MODIFY home_tel VARCHAR(20) NOT NULL;
DESC student;

ALTER TABLE student
CHANGE address home_address VARCHAR(200) NOT NULL;
DESC student;

ALTER TABLE student
DROP home_address;
DESC student;

DROP TABLE t_teacher

CREATE TABLE t_dept(
	deptno INT UNSIGNED PRIMARY KEY,
	dname VARCHAR(20) NOT NULL UNIQUE,
	tel CHAR(4) UNIQUE
);

# 添加主外键
CREATE TABLE t_emp(
	empo INT UNSIGNED PRIMARY KEY,
	ename VARCHAR(20) NOT NULL,
	deptno INT UNSIGNED NOT NULL,
	FOREIGN KEY (deptno) REFERENCES t_dept(deptno)

# 添加索引方便查找
CREATE TABLE t_message(
	id INT UNSIGNED PRIMARY KEY,
	content VARCHAR(200) NOT NULL,
	type ENUM("公告","通报","个人通知") NOT NULL,
	create_time TIMESTAMP NOT NULL,
	INDEX idx_type (type)
);

# 如何添加与删除索引
DROP INDEX idx_type ON t_message;

# 索引添加方式一
CREATE INDEX idx_type ON t_message(type);
SHOW INDEX FROM t_message;

# 索引添加方式二
ALTER TABLE t_message ADD INDEX idx_type(type);