#!/usr/bin/python
# -*- coding: UTF-8 -*-
#/***********************************************************************************************
#						created: 		2019-12-18
#
#						author:			chensong
#
#						purpose:		execl_tab
#************************************************************************************************/

import xlrd
#from readConfig import Signup_data,Login_data

#df = xlrd.open_workbook('M3.7工作任务.xlsx')

#print(df.shape)

#-*- coding:utf-8 -*-
import xlrd as xls
import sys
import getopt

def help():
    print("-h --help ")
    print("-i --in_file_name  ")
    print("-o --out_file_name  ")

def read_execl_write_file(in_file_name, out_file_name):
    data = xls.open_workbook(in_file_name)
    table = data.sheet_by_index(0)
    #table = data.sheet_by_name("版本3.7")
    fp = open(out_file_name, 'w') # 若是'wb'就表示写二进制文件

     #返回book中所有工作表的名字
    names = data.sheet_names()
    print("work name = ", names);
    # 获取行数和列数
    nrows = table.nrows
    ncols = table.ncols
    for row in range(nrows):
        if row != 0:
            fp.write("\n")
        for col in range(ncols):
            if col != 0:
                fp.write("\t")
            # 2是数据类型int类型 3是日期类型
            print("type = ", table.cell_type(row, col), ",data =", table.cell(row, col).value)
            if table.cell_type(row, col) == 2:
                fp.write(str(int(table.cell(row, col).value)))
            elif table.cell_type(row, col) == 3:
               #print( xlrd.xldate.xldate_as_datetime(table.cell(1,1).value, 0))
               fp.write(str(xlrd.xldate.xldate_as_datetime(table.cell(1,1).value, 0)))
            else:
                fp.write(str(table.cell(row, col).value))
            #fp.write(table.cell_value(row, col).str)
            #print("i = ", i, ", j = ", j, ", data =", table.cell(i,j).value)
          #  if ctype == 2 and cell % 1 == 0.0:  # ctype为2且为浮点
          #      cell = int(cell)  # 浮点转成整型
          #      cell = int(cell)  # 浮点转成整型
    # col_values数据表某一列的值
    print("col[0]", table.col_values(0))
    print("row[0] =", table.row_values(0))

    #f.write('Hello, world!')
    fp.flush()
    fp.close()

# 示例：
## 导入扩展包
#import xlrd
## 打开Excel文件读取数据
#data = xlrd.open_workbook('excelFile.xls') [1] 
## 获取一个工作表
#table = data.sheets()[0]                 #通过索引顺序获取
#table = data.sheet_by_index(0)           #通过索引顺序获取
#table = data.sheet_by_name(u'Sheet1')    #通过名称获取
## 获取整行和整列的值（数组）
#table.row_values(i)
#table.col_values(i)
## 获取行数和列数
#nrows = table.nrows
#ncols = table.ncols
## 循环行列表数据
#for i in range(nrows ):
#print table.row_values(i)
## 单元格
#table.cell(rowx,colx)
#cell_A1 = table.cell(0,0).value
#cell_C4 = table.cell(3,2).value
## 使用行列索引
#cell_A1 = table.row(0)[0].value
#cell_A2 = table.col(1)[0].value
## 简单的写入
#row = 0
#col = 0
## 常用单元格中的类型 
#0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error, 6 blank
#ctype = 1 value = '单元格的值'
## 扩展的格式化
#xf = 0  
#table.put_cell(row, col, ctype, value, xf)
#table.cell(0,0)        #单元格的值'
#table.cell(0,0).value  #单元格的值'

if __name__ == '__main__':
    in_file_name=""
    out_file_name=""

    try:
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["in_file_name=","out_file_name="])
    except getopt.GetoptError:
        help()
        sys.exit(-1)
    for opt,arg in opts:
        if opt == '-h':
            help()
            sys.exit(-1)
        elif opt in ("-i", "--in_file_name"):
            in_file_name = arg + ".xlsx"
        elif opt in ("-o","--out_file_name"):
            out_file_name = arg + ".tab"
    #print ('输入:'+in_file_name)
    #print ('输出:'+out_file_name)
    #print ('其他程序参数:'+",".join(args))
    #print("read execl !!!!! ")
    if in_file_name == "":
        help()
        sys.exit(-1)
    elif out_file_name == "":
        help()
        sys.exit(-1)
  #  print(in_file_name + ".xlsx")
	#read_execl_write_file(in_file_name, out_file_name)
    read_execl_write_file(in_file_name, out_file_name)
    
    pass

#def SignUp():
#    filepath = Signup_data
#    file = xlrd.open_workbook(filepath)
#    table = file.sheets()[0]
#    nrows = table.nrows
#    Susername = []
#    Smobile = []
#    Stxtcode = []
#    Smobilecode = []
#    Spassword = []
#    # 定义对应的用例条件list
#    for i in range(1,nrows):
#        # 循环行列表数据
#        Susername.append(table.cell(i,0).value)
#        Smobile.append(table.cell(i,1).value)
#        Stxtcode.append(table.cell(i,2).value)
#        Smobilecode.append(table.cell(i,3).value)
#        Spassword.append(table.cell(i,4).value)
#    # 返回list结果
#    return Susername,Smobile,Stxtcode,Sobilecode,Spassword
#
#def Login():
#    filepath = Login_data
#    file = xlrd.open_workbook(filepath)
#    table = file.sheet()[0]
#    nrows = table.nrows
#    Lusername = []
#    Lpassword = []
#
#    for i in range(1,nrows):
#        Lusername.append(table.cell(i,0).value)
#        Lpassword.append(table.cell(i,1).value)
#    # 返回list结果
#    return Lusername,Lpassword
    
    