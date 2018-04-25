# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from ..settings import MYSQL_HOST,MYSQL_DBNAME,MYSQL_USER,MYSQL_PASSWD

class TencentnextPipeline(object):
    def process_item(self, item, spider):
        for each_ele in list(dict(item).values()):
            with open('tencentnext2.txt','a') as f:
                f.write(each_ele + '\t')
        with open('tencentnext2.txt','a') as f:
            f.write('\n')
        return item


class DBPipeline():
	def __init__(self):
		self.db = pymysql.connect(
			host = MYSQL_HOST,
			db = MYSQL_DBNAME,
			user = MYSQL_USER,
			passwd = MYSQL_PASSWD,
			charset='utf8',
            use_unicode=True
			)