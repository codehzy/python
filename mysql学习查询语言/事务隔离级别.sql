# 只使用买票系统,读取未提交数据
SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
START TRANSACTION;
SELECT empno,ename,sal FROM t_emp;
COMMIT;

# 使用在银行转账系统，读取已提交数据
SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED;
START TRANSACTION;
SELECT empno,ename,sal FROM t_emp;
COMMIT;

# REPEATABLE READ 代表事务在执行中反复读取数据，得到的结果是一致的，不会受其他事务影响。
# 重复读取
SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
START TRANSACTION;
SELECT empno,ename,sal FROM t_emp;
COMMIT;

# 由于事务并发执行所带来的各种问题，前三种隔离级别只使用在某些业务场景中，但是序列化的隔离室，让事务逐一执行，就不会产生上述问题了。
# 序列化，主要就是等待之前的事务完成，如回滚或者提交。可以理解为的单线程，不过这样会影响数据库的并发性。
# 序列化
SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
SELECT empno,ename,sal FROM t_emp;
COMMIT;
