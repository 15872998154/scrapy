# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import json
from tencent.settings import MYSQL_HOST,MYSQL_DBNAME,MYSQL_USER,MYSQL_PASSWD
import logging
import pymysql
class TencentPipeline(object):
    def process_item(self, item, spider):
        for i in list(dict(item).values()):
            print(i)
            print('\n')
            with open ("8.txt",'a') as f:
                f.write(i+'\t')
        with open("8.txt","a") as f:
            f.write("\n")
        return item

class DBPipeline(object):

    def __init__(self):
        self.connect = pymysql.connect(
			host = MYSQL_HOST,
            db = MYSQL_DBNAME,
            user = MYSQL_USER,
            passwd = MYSQL_PASSWD,
            charset = 'utf8',
            use_unicode = True
			)
        self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        try:
            sql = "insert tencent values('{}','{}',{},'{}','{}')".format(item['positionName'],item['positionType'],int(item['peopleCount']),item['workPlace'],item['publicTime']	)

            self.cursor.execute(sql)
            self.connect.commit()
        except Exception as error:
            logging(error)
        return item
