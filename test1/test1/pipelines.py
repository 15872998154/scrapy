# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
class Test1Pipeline(object):
	

	def process_item(self, item, spider):
		line = list(dict(item).values())[0]+'\n'*2
		with open("3.json","a") as f:
			f.write(line)
		return item

	
