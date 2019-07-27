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


sql = "UPDATE `t_test_case_python` SET `last_name` = '%s' WHERE `first_name` = '%s'; "
data = ('wangrong', 'chen')
try:
   # 执行sql语句
   cursor.execute(sql % data)
   # 提交到数据库执行
   db.commit()
   print('成功修改', cursor.rowcount, '条数据')
except:
   # 如果发生错误则回滚
   db.rollback()
   print('失败修改', cursor.rowcount, '条数据')


# 关闭数据库连接
db.close()

 
 







