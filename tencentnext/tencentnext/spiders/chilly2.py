# -*- coding: utf-8 -*-
import scrapy

from tencentnext.items import TencentnextItem
class Chilly2Spider(scrapy.Spider):
    name = 'chilly2'
    #allowed_domains = ['zz']
    start_urls = ['https://hr.tencent.com/position.php?&start=0']
    baseUrl = 'https://hr.tencent.com/'

    def parse(self, response):

        tr_list = response.xpath('//tr[@class="even" or @class="odd"]')

        for tr in tr_list:

            item = TencentnextItem()

            positionName = tr.xpath("./td[1]/a/text()").extract()[0]

            if len(tr.xpath('./td[2]/text()')) != 0:
                positionType = tr.xpath('./td[2]/text()').extract()[0]
            else:
                positionType = ""

            peopleCount = tr.xpath("./td[3]/text()").extract()[0]

            workPlace = tr.xpath("./td[4]/text()").extract()[0]

            publicTime = tr.xpath("./td[5]/text()").extract()[0]

            item['positionName'] = positionName
            item['positionType'] = positionType
            item['peopleCount'] = peopleCount
            item['workPlace'] = workPlace
            item['publicTime'] = publicTime
            yield item

        if len( response.xpath('//div[@class="pagenav"]/a[@id="next" and @class="noactive"]')
                 ) == 0:
            nextUrl = self.baseUrl + \
            response.xpath('//div[@class="pagenav"]/a[@id="next"]/@href').extract()[0]
            yield scrapy.Request(nextUrl,callback = self.parse)