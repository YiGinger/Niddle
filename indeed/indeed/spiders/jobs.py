# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from indeed.items import IndeedItem


class JobsSpider(CrawlSpider):
    name = 'jobs'
    allowed_domains = ['indeed.com']
    start_urls = ['http://www.indeed.com/jobs?q=data+science&l=']

    rules = (
       Rule(LinkExtractor(allow=r'http://www.indeed.com/jobs?q=data+scientist&l=New+York%2C+NY'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        response=Selector(response)
        infos=response.xpath('//td[@id="resultsCol"]//div[@class="row  result"]//a')
        items=[]
        for info in infos:
            item = IndeedItem()
            item['jobtitle'] = response.xpath('/@title').extract()
            item['company'] =  "hahahhahahlaonianghuitouzaiyanjiu"
            item['link'] =  info.xpath('/@href').extract()
            items.append(item)
        
        return items
