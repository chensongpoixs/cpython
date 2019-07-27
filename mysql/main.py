#!/bin/python
#-*- coding: UTF-8 -*-
#文件名：main.py
# author : chensong 
# date   :2019-07-26

#import cloging
#import ccreate_table
import time


# main
if __name__ =='__main__':
   # cglobal_logger = cloging.Logger('debug.log')
	start_time = time.time()
	for i in range(1, 50, 1):
		end_time = time.time();
		temp_time = start_time - end_time
		print("i:%d:time:%d" % (i, temp_time))