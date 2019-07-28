#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装 mysql数据库依赖库命令
#pip3 install PyMySQL
 
import pymysql

#import cloging

import time





# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root',  passwd='', db='chensong', charset='utf8')
 
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
cursor = db.cursor()



sql = "insert into t_test_case_python values('%s', '%s', 1, 1);"

data = ('chen', 'chen')
str = "chen%d";
_start_time = time.time()
try:
	# 执行sql语句
	for i in range(0, 1000000, 1):
	#print(i)
		start_time = time.time()
		temp_str = str % (i)
	#print(temp_str)
		temp_sql = sql % (temp_str, temp_str)
		print (temp_sql)
		cursor.execute(temp_sql)
		db.commit()
		# 提交到数据库执行
		end_time = time.time()
		print('suucess install ok time:', (end_time - start_time )  , 'install:',cursor.rowcount, '条数据')
except:
   # 如果发生错误则回滚
   db.rollback()
   print('失败插入', cursor.rowcount, '条数据')
_end_time = time.time()
print('total_time:', _end_time - _start_time)

# 关闭数据库连接
db.close()

pass

 
 







