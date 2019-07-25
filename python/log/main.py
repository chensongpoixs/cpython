#!/bin/python
#-*- coding: UTF-8 -*-
#文件名：main.py
# author : chensong 
# date   :2019-07-26

import cloging

# main
if __name__ =='__main__':
    logyyx = cloging.Logger('debug.log')
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warning('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.cri('一个致命critical信息')

