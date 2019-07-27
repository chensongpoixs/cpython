#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装 mysql数据库依赖库命令
#pip3 install PyMySQL
 
import pymysql


# 打开数据库连接
db = pymysql.connect(host='localhost', port=3306, user='root',  passwd='', db='chensong', charset='utf8')
 
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
# 使用 cursor() 方法创建一个游标对象 cursor
# 获取游标
cursor = db.cursor()
## 删除数据
sql = "DELETE FROM `t_test_case_python` WHERE `last_name` = '%s' LIMIT %d;"
data = ('wangrong', 1)
cursor.execute(sql % data)
db.commit()
print('成功删除', cursor.rowcount, '条数据')
# 关闭数据库连接
db.close()

 
 







