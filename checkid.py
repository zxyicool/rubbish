# -*- coding: utf-8 -*-
"""
@Time ： 2022/11/7 22:48
@Auth ： zxy
@File ：checkid.py

"""


import pymysql
import xlwt
import xlrd
# xlwt,xlrd是python将数据导入excel表格使用的库




db_info = {
        "host": "172.16.20.247",
        "user": "root",
        "password": "ptdAChu+byhzq2dCc0",
        "database": "camel",
        "port": 33060
}


class ConnectDb(object):
    def __init__(self, db_info):
        # 初始化，连接数据库
        self.db = pymysql.connect(**db_info, cursorclass=pymysql.cursors.DictCursor)
        # 创建游标
        self.cur = self.db.cursor()

    def select_sql(self, sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        return result

    def execute_sql(self, sql):
        self.cur.execute(sql)
        self.db.commit()

    def close(self):
        self.cur.close()
        self.db.close()


if __name__ == '__main__':
    db = ConnectDb(db_info)
    sql = "select * from tms_line"
    r = db.select_sql(sql)
    print(r)
    a = r[0]['id']
    wb = xlwt.Workbook()
    # 添加一个表
    ws = wb.add_sheet('test')

    # 添加数据使用.write函数（横坐标，纵坐标，内容）注意横纵坐标从0开始，横纵坐标即对于excel而言
    # ws.write(x坐标, y坐标, 导出内容)
    # 例：ws.write(0, 0, '股票编号')
    ws.write(0, 0, a)

    # 将数据导出，保存格式为xxx.xls。其中xxx与上文表名同步
    # 注意此处一定要保存为.xls形式，如果是xlsx会打不开
    wb.save('C:/Users/zxy/Desktop/test.xls')


