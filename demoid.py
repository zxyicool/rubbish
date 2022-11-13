# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/7 23:10
@Auth ： zxy
@File ：demoid.py

"""


# 1、导入mysql
import pymysql
from pymysql import *
# 2、创建数据库连接
conn = connect(host='172.16.20.247',
               port=33060,
               user='root',
               password='ptdAChu+byhzq2dCc0',
               db='camel',
               charset='utf8')
# 3、打开游标
cur = conn.cursor()
# 4、执行sql语句
sql = input('请输入查询sql:')
# sql = "select id from tms_batch order by id  asc"
# 执行sql语句
cur.execute(sql)
result1 = cur.fetchall()
# print(result1)
# print(len(result1))
new_list = [seq[0] for seq in result1]
# print(new_list)
# print(len(new_list))
j = new_list[0]
# 5、关闭游标
cur.close()
# 6、关闭连接
conn.close()


def check_id(x, y):
    for i in x:
        if i == y:
            y += 1
        else:
            return False
    return True


if __name__ == '__main__':
    print(check_id(new_list, j))







