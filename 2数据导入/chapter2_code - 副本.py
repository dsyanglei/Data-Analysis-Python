# -*- coding: utf-8 -*-
####################################################################

file = 'traffic_log_for_dataivy'
fn = open(file, 'r')  # 打开要读取的日志文件对象
content = fn.readlines()  # 以列表形式读取日志数据
print (content[:2])
fn.close()  # 关闭文件对象