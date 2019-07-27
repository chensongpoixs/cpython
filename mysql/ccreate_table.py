#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装 mysql数据库依赖库命令
#pip3 install PyMySQL
 
import pymysql

#import cloging



#class cmysql_mgr:
   # def __init__(self):
		#db = pymysql.connect(host='localhost',
		#	port=3306,
		#	user='root',
		#	passwd='',
		#	db='chensong',
		#	charset='utf8'
		#)
  
    #def create_table(self):
		#cglobal_logger = cloging.Logger('debug.log')
		## 创建表
        #
		## 使用 execute() 方法执行 SQL，如果表存在则删除  测试案例表
		#cursor.execute("DROP TABLE IF EXISTS t_test_case_python")
        #
		## 使用预处理语句创建表
		#sql = """CREATE TABLE `t_test_case_python` (
		#		 `first_name`  CHAR(20) NOT NULL COMMENT '姓',
		#		 `last_name`  CHAR(20) COMMENT '名',
		#		 `age` INT COMMENT '年龄',   
		#		 `sex` CHAR(1) COMMENT '性别',
		#		 `income` FLOAT )"""
		# 
		#cursor.execute(sql)
		#cglobal_logger.info('create table ok')
		## 关闭数据库连接
		#db.close()
		
 
#import pymysql.cursors
# 打开数据库连接



# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root',  passwd='', db='chensong', charset='utf8')
 
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
cursor = db.cursor()

# 创建表

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS `t_test_case_python`;")
 
# 使用预处理语句创建表
sql = """CREATE TABLE `t_test_case_python` (
         `first_name`  CHAR(20) NOT NULL COMMENT '姓',
         `last_name`  CHAR(20) COMMENT '名',
         `sex` CHAR(1) COMMENT '年龄' ,
         `income` FLOAT COMMENT 'income');"""

cursor.execute(sql)

#cursor.execute("CREATE TABLE `t_test_case_python` (`first_name` CHAR(20) NOT NULL COMMENT '姓', `last_name` CHAR(20) COMMENT '名', `age` INT COMMENT 'age', `sex` CHAR(1) COMMENT '性别', `income` FLOAT COMMENT 'income')")
 
# 关闭数据库连接
db.close()

 
 







