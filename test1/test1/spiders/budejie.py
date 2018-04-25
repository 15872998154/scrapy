
import scrapy

import json
from test1.items import Test1Item




class BudejieSpider(scrapy.Spider):
    name = 'budejie'
    #allowed_domains = ['budejie']
    start_urls = ['http://www.budejie.com/text/']

    def parse(self, response):
    	 #创建item对象
    	comment = response.xpath("//div[@class='j-r-list-c-desc']/a/text()").extract()
    	
    	for com initem = Test1Item()
    		item['comment'] = com
    		#pinglun = json.dumps(dict(item),ensure_ascii = False)
    		#print(pinglun)
    		yield item
    		

