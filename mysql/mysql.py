#!/usr/bin/python
# -*- coding: UTF-8 -*-


#pip3 install PyMySQL
 
import pymysql
 
#import pymysql.cursors
# 打开数据库连接
db = pymysql.connect(host='localhost',
    port=3306,
    user='root',
    passwd='',
    db='chensong',
    charset='utf8'
)
 
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
#cursor = connect.cursor()
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询 
cursor.execute("SELECT VERSION()")
 
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()
 
print ("Database version : %s " % data)
 
# 关闭数据库连接
#db.close()

# 创建表

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
 
# 使用预处理语句创建表
sql = """CREATE TABLE `EMPLOYEE` (
         `FIRST_NAME`  CHAR(20) NOT NULL,
         `LAST_NAME`  CHAR(20),
         `AGE` INT,  
         `SEX` CHAR(1),
         `INCOME` FLOAT )"""
 
cursor.execute(sql)
 
# 关闭数据库连接
#db.close()


# insert

# SQL 插入语句
sql = """INSERT INTO `EMPLOYEE`(`FIRST_NAME`,
         `LAST_NAME`, `AGE`, `SEX`, `INCOME`)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # 执行sql语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()
 
# 关闭数据库连接
db.close()

# 插入数据
#sql = "INSERT INTO trade (name, account, saving) VALUES ( '%s', '%s', %.2f )"
#data = ('雷军', '13512345678', 10000)
#cursor.execute(sql % data)
#connect.commit()
#print('成功插入', cursor.rowcount, '条数据')
#
## 修改数据
#sql = "UPDATE trade SET saving = %.2f WHERE account = '%s' "
#data = (8888, '13512345678')
#cursor.execute(sql % data)
#connect.commit()
#print('成功修改', cursor.rowcount, '条数据')
#
## 查询数据
#sql = "SELECT name,saving FROM trade WHERE account = '%s' "
#data = ('13512345678',)
#cursor.execute(sql % data)
#for row in cursor.fetchall():
#    print("Name:%s\tSaving:%.2f" % row)
#print('共查找出', cursor.rowcount, '条数据')
#
## 删除数据
#sql = "DELETE FROM trade WHERE account = '%s' LIMIT %d"
#data = ('13512345678', 1)
#cursor.execute(sql % data)
#connect.commit()
#print('成功删除', cursor.rowcount, '条数据')
#
## 事务处理
#sql_1 = "UPDATE trade SET saving = saving + 1000 WHERE account = '18012345678' "
#sql_2 = "UPDATE trade SET expend = expend + 1000 WHERE account = '18012345678' "
#sql_3 = "UPDATE trade SET income = income + 2000 WHERE account = '18012345678' "
#
#try:
#    cursor.execute(sql_1)  # 储蓄增加1000
#    cursor.execute(sql_2)  # 支出增加1000
#    cursor.execute(sql_3)  # 收入增加2000
#except Exception as e:
#    connect.rollback()  # 事务回滚
#    print('事务处理失败', e)
#else:
#    connect.commit()  # 事务提交
#    print('事务处理成功', cursor.rowcount)
#
## 关闭连接
#cursor.close()
#connect.close()