SELECT * FROM t_emp
SELECT empno,ename,job FROM t_emp

# 别名
SELECT
	empno,
	sal * 12 AS "income"
FROM t_emp

# 数据分页，LIMIT 起始位置，偏移量
SELECT empno,ename FROM t_emp LIMIT 0,5;

# 结果集排序 ASC = 升序，DESC = 降序
SELECT ename,sal FROM t_emp ORDER BY sal DESC;

SELECT empno,ename,sal,hiredate
FROM t_emp
ORDER BY sal DESC,hiredate ASC;

SELECT
	empno,ename,deptno,sal
FROM t_emp
ORDER BY deptno,sal DESC

# 这个公司工资前五
SELECT
	empno,ename,sal
FROM t_emp ORDER BY sal DESC LIMIT 0,5;

# 结果集中的重复记录
SELECT job From t_emp;
# 去重，只对单个字段有效
SELECT DISTINCT job FROM t_emp;

# 条件查询
SELECT empno,ename,sal FROM t_emp
WHERE (deptno = 10 OR deptno = 20) AND sal >= 2000;

# 算术运算符,筛选年 薪资超过15000并且工龄打印20年的人
SELECT empno,ename,sal,hiredate
FROM t_emp
WHERE deptno = 10 AND (sal + IFNULL(comm,0)) * 12 >= 15000
AND DATEDIFF(NOW(),hiredate) / 365 >= 20;

# 类比python语言中运算符
SELECT
	empno,ename,sal,hiredate
From t_emp
WHERE deptno IN(10,20,30) AND job != 'SALESMAN'
AND hiredate < "1985-01-01";

SELECT
	ename,comm
FROM t_emp WHERE comm IS NULL;

SELECT
	ename,comm
FROM t_emp WHERE comm IS NOT NULL

SELECT
	ename,comm
FROM t_emp WHERE comm IS NULL
AND sal BETWEEN 2000 AND 3000
AND ename LIKE "%A%";

SELECT
	ename,comm
FROM t_emp WHERE comm IS NULL
AND sal BETWEEN 2000 AND 3000
AND ename LIKE "_LAKE";

SELECT
	ename,comm,sal
FROM t_emp WHERE comm IS NOT NULL
-- AND sal BETWEEN 1000 AND 3000
AND ename REGEXP "^[\\u4e00-\\u9fa5]{2,4}$";


# 逻辑运算符
SELECT
	ename,deptno
From t_emp
WHERE NOT deptno IN(10,20) XOR sal >= 2000;

# 二进制按位运算
# WHERE语句中，条件执行的顺序是从左向右的。所以我们应该把索引条件，或者筛选掉记录最多的条件写在最左侧。
# FROM ——> WHERE -> SELECT -> ORDER BY -> LIMIT


# 聚合函数 不可以出现在WHERE语句中
# 求平均值
SELECT AVG(sal + IFNULL(comm,0)) AS avg FROM t_emp;

# 求和
SELECT SUM(sal) FROM t_emp WHERE deptno IN(10,20)

# MAX函数
SELECT MAX(comm) FROM t_emp;

SELECT MAX(sal + IFNULL(comm,0)) FROm t_emp WHERE deptno IN(10,20);

SELECT MAX(LENGTH(ename)) FROM t_emp;

SELECT MIN(comm) FROM t_emp;

# avg函数主要统计数值

# COUNT函数
SELECT COUNT(*),comm FROM t_emp

# 查询10和20部门中，底薪超过2000元并且工龄超过15年的员工
SELECT COUNT(*) FROM t_emp
WHERE deptno IN(10,20) AND sal >= 2000
AND DATEDIFF(NOW(),hiredate) / 365 >= 15

# 查询1985年以后入职的员工，底薪超过公司平均底薪的员工的数量?
SELECT COUNT(*) FROM t_emp
WHERE hiredate >= "1985-01-01"
AND sal > AVG(sal);

# 分组语言
SELECT 
	deptno,ROUND(AVG(sal))
FROM t_emp
GROUP BY deptno;

# 逐级分组
SELECT deptno,job,COUNT(*),AVG(sal)
FROM t_emp GROUP BY deptno,job
ORDER BY deptno;

# 报错。因为group by中不包含对sal的分组
SELECT deptno,COUNT(*),AVG(sal),sal
FROM t_emp
# 解决方法： GROUP_CONCAT函数
# GROUP_CONCAT函数可以把分组查询中的某个字段拼接成一个字符串
# 查询每个部门内底薪超过2000元的人数和员工姓名
SELECT deptno,GROUP_CONCAT(ename),COUNT(*)
FROM t_emp WHERE sal >= 2000
GROUP BY deptno;

# 对分组结果集再次进行汇总计算
SELECT
	deptno,COUNT(*),AVG(sal),MAX(sal),MIN(sal)
FROM t_emp GROUP BY deptno WITH ROLLUP;

# FROM ——> WHERE -> GROUP BY -> SELECT -> ORDER BY -> LIMIT


# HAVING
# 报错: WHERE先于GROUP BY执行，所以AVG不知道聚合的范围,解决方法HAVING
SELECT deptno
FROM t_emp
WHERE AVG(sal) >= 2000
GROUP BY deptno

# 解决
SELECT deptno
FROM t_emp
GROUP BY deptno HAVING AVG(sal) >= 2000;


# HAVGING子句的用途
# 查询每个部门中，1982年以后入职的员工超过2个人的部门编号
SELECT deptno FROM t_emp
WHERE hiredate >= "1982-01-01"
GROUP BY deptno HAVING COUNT(*) >= 2;
ORDER BY deptno ASC;

# HAVING子句的特殊用法
SELECT deptno,COUNT(*) FROM t_emp
GROUP BY 1;

SELECT deptno,COUNT(*) FROM t_emp
GROUP BY 1 HAVING deptno IN (10,20);

# 多表查询
SELECT e.empno,e.ename,d.dname
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno

# 内连接（交集）和外连接
SELECT e.empno,e.ename,d.dname,e.sal,e.job,s.grade
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno
JOIN t_salgrade s ON e.sal BETWEEN s.losal AND s.hisal;

# 查询与SCOTT相同部门的员工都有谁
# 内连接需要优化
SELECT ename 
FROM t_emp
WHERE deptno = (SELECT deptno FROM t_emp WHERE ename = "SCOTT")
AND ename != "SCOTT";

# 优化:将内连接使用表连接，相同数据表也可以表连接
SELECT e2.ename
FROM t_emp e1 JOIN t_emp e2 ON e1.deptno = e2.deptno
WHERE e1.ename = "SCOTT" AND e2.ename != "SCOTT";

# 查询底薪超过公司平均底薪的员工信息？
# 将某次查询的结果作为一张表来进行表连接查询
SELECT e.empno,e.ename,e.sal
FROM t_emp e JOIN
(SELECT AVG(sal) avg FROM t_emp) t
ON e.sal >= t.avg

# 内连接查询,查询RESEARCH部门的人数、最高底薪、最低底薪、平均底薪、平均工龄?
SELECT COUNT(*),MAX(e.sal),MIN(e.sal),AVG(e.sal),FLOOR(AVG(DATEDIFF(NOW(),e.hiredate) / 365))
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno
WHERE d.dname = "RESEARCH";

# 内连接查询
# 查询每种职业的最高工资、最低工资、平均工资、最高工资等级、最低工资等级？
SELECT 
e.job,
MAX(e.sal + IFNULL(e.comm, 0)),
MIN(e.sal + IFNULL(e.comm, 0)),
AVG(e.sal + IFNULL(e.comm, 0)),
MAX(s.grade),
MIN(s.grade)
FROM t_emp e JOIN t_salgrade s
ON (e.sal + IFNULL(e.comm,0)) BETWEEN s.losal AND s.hisal
GROUP BY e.job;

# 查询每个底薪超过部门平均底薪的员工信息
SELECT e.empno,e.ename,e.sal
FROM t_emp e JOIN
(SELECT deptno,AVG(sal) AS avg FROM t_emp GROUP BY deptno) t
ON e.deptno = t.deptno AND e.sal >= t.avg;

# 外连接
# 左外接连就是保留左表所有的记录，与右表做连接。如果右表有符合条件的记录就与左表连接。
# 如果右表没有符合条件的记录，就用NULL与左表连接。右外连接也是如此。
SELECT e.empno,e.ename,d.dname
FROM t_emp e
LEFT JOIN t_dept d ON e.deptno = d.deptno;

SELECT e.empno,e.ename,d.dname
FROM t_dept d 
RIGHT JOIN t_emp e ON e.deptno = d.deptno;

# 查询每个部门的名称和部门的人数？
SELECT d.dname,COUNT(e.deptno)
FROM t_dept d
LEFT JOIN t_emp e
ON d.deptno = e.deptno
GROUP BY d.deptno;

# 查询每个部门的名称和部门的人数？如果没有部门的员工，部门名称用NULL显示
# UNION连接左外和右外连接查询
(SELECT d.dname,COUNT(e.deptno)
FROM t_dept d
LEFT JOIN t_emp e
ON d.deptno = e.deptno
GROUP BY d.deptno) 
UNION
(SELECT d.dname,COUNT(*)
FROM t_dept d
RIGHT JOIN t_emp e
ON d.deptno = e.deptno
GROUP BY d.deptno)

# 查询每名员工的编号、姓名、部门、月薪、工资等级、工龄、上司编号、上司姓名、上司部门？
SELECT
	e.empno,
	e.ename,
	d.dname,
	e.sal + IFNULL(e.comm,0),
	s.grade,
	FLOOR(DATEDIFF(NOW(),e.hiredate) / 365),
	t.empno AS mgrno,t.ename AS mname,t.dname AS mdname
FROM t_emp e LEFT JOIN t_dept d ON e.deptno=d.deptno
LEFT JOIN t_salgrade s ON e.sal BETWEEN s.losal AND s.hisal
LEFT JOIN
(SELECT e1.empno,e1.ename,d1.dname
FROM t_emp e1 JOIN t_dept d1 ON e1.deptno = d1.deptno) t ON e.mgr = t.empno


# 子查询

# 最好不要写，因为没执行一次查询都要查询一个子查询
# WHERE子查询
SELECT empno,ename,sal
FROM t_emp
WHERE sal >= (SELECT AVG(sal) FROM t_emp);

# FROM子查询，不是相关子查询
SELECT
	e.empno,e.ename,e.sal,t.avg
FROM t_emp e JOIN
(SELECT deptno,AVG(sal) as avg FROM t_emp GROUP BY deptno) t
ON e.deptno = t.deptno AND e.sal >= t.avg

# select子查询


# 数据库插入 了解IGNORE关键字
INSERT IGNORE INTO t_dept(deptno,dname,loc)
VALUES(60,"后勤部","北京"),(70,"前台部","北京")

# 向后勤部添加一条员工记录
INSERT INTO t_emp
(empno,ename,job,mgr,hiredate,sal,comm,deptno)
VALUES(8001,"刘娜","SALESMAN",8000,"1998-12-20",2000,NULL,(SELECT deptno FROM t_dept WHERE dname="后勤部"))

# 把每个员工的编号和上司的编号+1，用ORDER BY子句完成
UPDATE t_emp SET empno = empno + 1,mgr = mgr + 1
ORDER BY empno DESC;
# 把月收入前三名的员工底薪减100元，用LIMIT子句完成
UPDATE t_emp
SET sal = sal - 100
ORDER BY sal + IFNULL(comm,0) DESC
LIMIT 3;

# 把10部门中，工龄超过20年的员工，底薪增加200元
UPDATE t_emp
SET sal = sal + 200
WHERE DATEDIFF(NOW(),hiredate) / 365 >= 20

# 把ALLEN调往RESEARCH部门，职务调整为ANALYST
# 看似被需要条件，实则不要
UPDATE t_emp e JOIN t_dept d
SET e.deptno = d.deptno,e.job = "ANALYST",d.loc = "北京"
WHERE e.ename = "ALLEN" AND d.dname = "RESEARCH"

# 把底薪低于公司平均底薪的员工，底薪增加150元
UPDATE t_emp e JOIN
(SELECT AVG(sal) AS avg FROM t_emp) t
ON e.sal < t.avg
SET e.sal = e.sal + 150;

# 把没有部门的员工，或者SALES部门低于2000元底薪的员工，都调往20部门
UPDATE t_emp e LEFT JOIN t_dept d ON e.deptno = d.deptno
SET e.deptno = 20
WHERE e.deptno IS NULL OR (d.dname="SALES" AND e.sal < 2000);

# DELETE语句
DELETE FROM t_emp
WHERE deptno = 10 AND DATEDIFF(NOW(),hiredate) / 365 >= 20;

# 删除20部门中工资最高的员工记录
DELETE FROM t_emp
WHERE deptno = 20
ORDER BY sal + IFNULL(comm,0) DESC
LIMIT 1;

# 删除SALES部门和该部门的全部员工记录
DELETE e,d
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno
WHERE d.dname = "SALES";

# 删除每个低于部门平均底薪的员工记录
DELETE e
FROM t_emp e JOIN
(SELECT deptno,AVG(sal) AS sal FROM t_emp GROUP BY deptno) t
ON e.deptno = t.deptno AND e.sal < t.sal

# 删除员工KING和他的直接下属的员工记录，用表连接实现
DELETE e
FROM t_emp e JOIN
(SELECT empno FROM t_emp WHERE ename = "KING" ) t
ON e.mgr = t.empno OR e.empno=t.empno

# 删除SALES部门的员工，以及没有部门的员工
DELETE e
FROM t_emp e LEFT JOIN t_dept d ON e.deptno = d.deptno
WHERE d.dname = "SALES" OR e.deptno IS NULL

# 快速情况数据表
TRUNCATE TABLE t_emp


# 函数
SELECT ABS(-100);
SELECT ROUND(4.6288*100)/100;
SELECT FLOOR(9.9);
SELECT CEIL(3.2);
SELECT POWER(2,3);
SELECT LOG(7,3);
SELECT LN(10);

SELECT SQRT(9);
SELECT PI();
SELECT SIN(RADIANS(30));
SELECT COS(RADIANS(45));
SELECT TAN(RADIANS(90));
SELECT COT(RADIANS(45));
SELECT DEGREES(1);

SELECT NOW(),CURDATE(),CURTIME();

# 格式化日期
SELECT ename,DATE_FORMAT(hiredate,"%Y") AS "year" FROM t_emp;

# 查询明年你的生日是星期几
SELECT DATE_FORMAT('2021-07-25','%W');

# 利用日期函数，查询1981年上半年入职的员工有多少人？
SELECT COUNT(*)
FROM t_emp
WHERE DATE_FORMAT(hiredate,"%Y") = 1981
AND DATE_FORMAT(hiredate,"%m") <= 6; 

# 日期偏移计算
SELECT DATE_ADD(NOW(),INTERVAL 100 DAY);
# DATEDIFF(expr1,expr2)
SELECT DATEDIFF(NOW(),'1998-07-25') / 365;

# 字符替换
SELECT
	LOWER(ename),UPPER(ename),LENGTH(ename),
	CONCAT(sal,"$"),INSTR(ename,"A")
FROM t_emp;

SELECT INSERT("你好",1,1,"先生");

SELECT REPLACE("你好先生","先生","女士")；

# 字符截取和补充
-- SELECT SUBSTR(str,pos,len)
-- SELECT SUBSTRING(str FROM pos FOR len)
SELECT SUBSTR("你好世界",3,4),SUBSTRING("你好世界",3,2)

SELECT LPAD(str,len,padstr)
SELECT LPAD(SUBSTRING("17601511257",8,4),11,"*");

SELECT RPAD(SUBSTRING("李晓娜",1,1),LENGTH("李晓娜") / 3,"*");

SELECT TRIM("        Hello World    ");

# 条件函数
# IFNULL(expr1,expr2)
# IF(expr1,expr2,expr3) 类似于三元运算符

# SALES部门发放礼品A，其余部门发放礼品B，打印每名员工获得的礼品
SELECT
	e.empno,e.ename,d.dname,
	IF(d.dname = "SALES","礼品A","礼品B")
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno;

/*
SALES部门去P1地点
ACCOUNTING部门去P2地点
RESERACH部门去P3地点
*/
# CASE语句
SELECT
	e.empno,e.ename,
	CASE
		WHEN d.dname = "SALES" THEN
			"p1"	
		WHEN d.dname = "ACCOUNTING" THEN
			"p2"	
		WHEN d.dname = "RESEARCH" THEN
			"p3"
	END AS place
FROM t_emp e JOIN t_dept d ON e.deptno = d.deptno;