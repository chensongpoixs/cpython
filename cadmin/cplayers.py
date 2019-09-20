#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 安装 mysql数据库依赖库命令
#pip3 install PyMySQL
 
import pymysql
import sys

# 检查玩家加入和退出次数是否相等
def check_player_num():
	# 打开数据库连接
	#try:
	db = pymysql.connect(host='localhost',
	port=3306,
	user='root',
	passwd='',
	db='global_log',
	charset='utf8'
	)

	cursor = db.cursor()
	#except pymysql.error, e
	#	print("connect mysql error")
	#	sys.exit(1)
	
	# 所有玩家加入和退出数量 sql 
	players_sign_up_sql = "SELECT count(*) FROM `t_player_sign_up_table`;"
	players_sign_out_sql = "SELECT count(*) FROM `t_player_sign_out_table`;"


	# 查询加入数量
	cursor.execute(players_sign_up_sql)
	players_sign_up =  cursor.fetchone()

	cursor.execute(players_sign_out_sql)
	players_sign_out =  cursor.fetchone()
	print("players sign up = %s " % players_sign_up)
	print("players sign out = %s " % players_sign_out)
	if players_sign_up == players_sign_out :
		print("==")
		cursor.close()
		db.close()
		return 0
	else:
		print("!=")
		cursor.close()
		db.close()
		return 1
	

# 查询出所有玩家
def get_all_players():
# 打开数据库连接
	#try:
	db = pymysql.connect(host='localhost',
	port=3306,
	user='root',
	passwd='',
	db='global_log',
	charset='utf8'
	)

	cursor = db.cursor()
	#except pymysql.error, e
	#	print("connect mysql error")
	#	sys.exit(1)
	
	all_players_id_sql = "SELECT DISTINCT `player_id` FROM `t_player_sign_up_table`;";


	# 查询出所有玩家id 
	all_players_ids = []
	cursor.execute(all_players_id_sql)
	results = cursor.fetchall()
	#
	for row in results:
	##	row_list = []
	##	for column in row:
	##		row_list.append(column.replace('\t', '').replace('\n', '').replace('\r', ''))
		all_players_ids.append(row[0])
	#	#players = row[0]
	#	#all_players_ids.append(players)
	##for row in cursor.fetchall():
	#	# 找出那些玩家没有退出比赛的
	# #   print("player_id:%s" % row)
	#		
	print('find all players = ', cursor.rowcount)
	cursor.close()
	db.close()
	return all_players_ids



# 检查玩家加入和退出是否正常
def check_player_join_out(all_players_ids):
# 打开数据库连接
	#try:
	db = pymysql.connect(host='localhost',
	port=3306,
	user='root',
	passwd='',
	db='global_log',
	charset='utf8'
	)

	cursor = db.cursor()
	#except pymysql.error, e
	#	print("connect mysql error")
	#	sys.exit(1)
	
	all_player_id_join_tables = "SELECT count(*) from `t_player_sign_up_table` where `player_id` = '%s'";
	all_player_id_out_tables = "SELECT count(*) from `t_player_sign_out_table` where `player_id` = '%s'";


	## 查询玩家的加入和退出是相等
	for player_id_ in all_players_ids:
	#	print("player_id_ = %s" % player_id_)
		cursor.execute(all_player_id_join_tables % player_id_)
		player_join_num = cursor.fetchone()
		cursor.execute(all_player_id_out_tables % player_id_)
		player_out_num = cursor.fetchone()
		if player_join_num == player_out_num :
			print("player_id = %s ok " % player_id_)
			print("player join num = ", player_join_num)
			print("player out num = ", player_out_num)
		else:
			print("player_id = %s error " % player_id_)
			print("player join num = ", player_join_num)
			print("player out num = ", player_out_num)
	
	cursor.close()
	db.close()



# python main 
if __name__ == '__main__':
	print("check players data begin !!!!! ")
	players = check_player_num()
	print("=== %s " % players)
	all_players_ids = get_all_players()
	print(all_players_ids)
	check_player_join_out(all_players_ids)
	pass


#old_players = players_sign_up - players_sign_out
#print(" sign up sign out = %s " % old_players)
#print ("...")
# 创建表

# 使用 execute() 方法执行 SQL，如果表存在则删除
#cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# 
## 使用预处理语句创建表
#sql = """CREATE TABLE `EMPLOYEE` (
#         `FIRST_NAME`  CHAR(20) NOT NULL,
#         `LAST_NAME`  CHAR(20),
#         `AGE` INT,  
#         `SEX` CHAR(1),
#         `INCOME` FLOAT )"""
# 
#cursor.execute(sql)
# 
## 关闭数据库连接
##db.close()
#
#
## insert
#
## SQL 插入语句
#sql = """INSERT INTO `EMPLOYEE`(`FIRST_NAME`,
#         `LAST_NAME`, `AGE`, `SEX`, `INCOME`)
#         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
#try:
#   # 执行sql语句
#   cursor.execute(sql)
#   # 提交到数据库执行
#   db.commit()
#except:
#   # 如果发生错误则回滚
#   db.rollback()
# 
## 关闭数据库连接
#db.close()

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