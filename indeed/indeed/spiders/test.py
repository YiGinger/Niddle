# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from indeed.items import IndeedItem


class JobsSpider(CrawlSpider):
    name = 'test'
    allowed_domains = ['indeed.com']
    start_urls = ['http://www.indeed.com/jobs?q=data+scientist&l=New+York%2C+NY']

    #rules = (
     #   Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    #)

    def parse_item(self, response):
        response=Selector(response)
        infos=response.xpath('//td[@id="resultsCol"]//div[@class="row  result"]')
        items=[]
        for info in infos:
            print 'haha I am in loop'
            item = IndeedItem()
            item['jobtitle'] = response.xpath('.//a/@title').extract()
            item['company'] =  "hahahhahahlaonianghuitouzaiyanjiu"
            item['link'] =  info.xpath('.//a/@href').extract()
            print 'haha start to append'
            items.append(item)
        
        print items
        return items
