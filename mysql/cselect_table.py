#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装 mysql数据库依赖库命令
#pip3 install PyMySQL
 
import pymysql

#import cloging

# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root',  passwd='', db='chensong', charset='utf8')
 
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
cursor = db.cursor()


# 查询数据
sql = "SELECT `first_name`, `last_name`, `sex` FROM `t_test_case_python` WHERE `first_name` = '%s' ;"
data = ('chen')
cursor.execute(sql % data)
for row in cursor.fetchall():
    print("first_name:%s\last_name:%s\sex:%c" % row)
print('共查找出', cursor.rowcount, '条数据')


# 关闭数据库连接
db.close()

 
 







