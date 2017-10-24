import  requests
import pymysql
import json

import sys
from bs4 import  BeautifulSoup


class TranserfMoney():
    def __init__(self,conn):
        pass
    def tm(self):
        pass


def test(param):
    pass


if __name__ == '__main__':
    # 原账户
    source_accid=10
    # 目标账户
    target_accid=11
    # 转账金额
    money = 12
    conn = pymysql.connect(host='59.110.215.202', user='root', passwd='wanghao', db='app_cms', port=3306,
                           charset='utf8')
    tr_money=TranserfMoney(conn)

    try:
        tr_money.tm()
        test(1)
    except Exception as e:
        print(e)


