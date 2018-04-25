# -*- coding: utf-8 -*-
import scrapy

from tencent.items import TencentItem

class ChillySpider(scrapy.Spider):
    name = 'chilly'
    #allowed_domains = ['hr.tencent']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']
    baseUrl = 'https://hr.tencent.com/position.php?&start='
    offset = 0
    def parse(self, response):

        content = response.xpath('//tr[@class="even" or @class="odd"]')
        for tr in content:

            item = TencentItem()
            
            positionName = tr.xpath("./td[1]/a/text()").extract()[0]
            
            if len(tr.xpath('./td[2]/text()')) != 0:
            	positionType = tr.xpath('./td[2]/text()').extract()[0]
            else:
                positionType=""
            peopleCount  = tr.xpath("./td[3]/text()").extract()[0]

            workPlace    = tr.xpath("./td[4]/text()").extract()[0]
    		
            publicTime   = tr.xpath("./td[5]/text()").extract()[0]

            print(positionName,positionType,peopleCount,workPlace,publicTime)
            item['positionName'] = positionName
            item['positionType'] = positionType
            item['peopleCount']  = peopleCount
            item['workPlace']    = workPlace
            item['publicTime']   = publicTime

            yield item

        if self.offset < 3950:
            self.offset += 10
            url = self.baseUrl + str(self.offset)
            yield  scrapy.Request(url,callback = self.parse)



