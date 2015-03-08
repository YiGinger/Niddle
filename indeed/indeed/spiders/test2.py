# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from indeed.items import IndeedItem

class Test2Spider(scrapy.Spider):
    name = "test2"
    allowed_domains = ["indeed.com"]
    start_urls = (
        'http://www.indeed.com/jobs?q=data+scientist&l=',
    )

    def parse(self, response):
    	response=Selector(response)
        infos=response.xpath('//td[@id="resultsCol"]//div[@class="row  result"]')
        items=[]
        for info in infos:
            item = IndeedItem()
                        #print 'this is a name ',info.xpath('.//a[@class="jobtitle"]//@title').extract()
            if info.xpath('.//h2[@class="jobtitle"]//a/@title'):
                name=info.xpath('.//h2[@class="jobtitle"]//a/@title').extract()
            else:
                name=info.xpath('.//a[@class="jobtitle"]//@title').extract()
            item['jobtitle'] = name
            item['company'] = info.xpath('.//span[@class="company"]//text()').extract()
            item['location'] =  info.xpath('.//span[@class="location"]//text()').extract()
            items.append(item)
        
        return items

       