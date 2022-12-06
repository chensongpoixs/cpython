#!/usr/bin/python
# -*- coding: UTF-8 -*-
#						created: 		2019-12-18
#
#						author:			chensong
#
#						purpose:		execl_tab
# python真是个奇葩的东西   居然不可以使用Tab键 只能使用回车键   ^_^

import xlrd
import xlrd as xls
import sys
import getopt

def help():
    print("-h --help ")
    print("-i --in_file_name  ")
    print("-o --out_file_name  ")

def read_execl_write_file(in_file_name, out_file_name):
    try:
        data = xls.open_workbook(in_file_name)
    except Exception:
        return -1
	
    table = data.sheet_by_index(0)
    fp = open(out_file_name, 'w', encoding='utf-8-sig') # 若是'wb'就表示写二进制文件
	
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
            if table.cell_type(row, col) == 2:
                fp.write(str(int(table.cell(row, col).value)))
            elif table.cell_type(row, col) == 3:
               fp.write(str(xlrd.xldate.xldate_as_datetime(table.cell(row,col).value, 0)))
            else:
                fp.write(str(table.cell(row, col).value))

    fp.flush()
    fp.close()
    return 0



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

    if in_file_name == "":
        help()
        sys.exit(-1)
    elif out_file_name == "":
        help()
        sys.exit(-1)

    if read_execl_write_file(in_file_name, out_file_name) == 0:
       print("write file ok")
    else:
       print("read file failed ")
    pass
    
    