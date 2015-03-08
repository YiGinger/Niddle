# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from indeed.items import IndeedItem


class AllSpider(CrawlSpider):
    name = 'all'
    allowed_domains = ['indeed.com']
    start_urls = ['http://www.indeed.com/jobs?q=data+scientist&l=']

    rules = (
        Rule(LinkExtractor(allow=(r'http://www.indeed.com/jobs\?q=data\+scientist&start=\d*'),
            restrict_xpaths=('//div[@class="pagination"]//a//span[@class="pn"]//span[@class="np"]//..//..')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print 'start to scrapy\n\n'
        response= Selector(response)
        infos=response.xpath('//td[@id="resultsCol"]//div[@class="row  result"]')
        items=[]
        for info in infos:
            item = IndeedItem()
                        #print 'this is a name ',info.xpath('.//a[@class="jobtitle"]//@title').extract()
            if info.xpath('./h2[@class="jobtitle"]//a/@title'):
                name=info.xpath('./h2[@class="jobtitle"]/a/@title').extract()
                url=['www.indeed.com'] + info.xpath('./h2[@class="jobtitle"]/a/@href').extract()
            else:
                name=info.xpath('./a[@class="jobtitle"]/@title').extract()
                url=['www.indeed.com'] + info.xpath('./a[@class="jobtitle"]/@href').extract()
            item['jobtitle'] = name
            item['company'] = info.xpath('.//span[@class="company"]//text()').extract()
            item['location'] =  info.xpath('.//span[@class="location"]//text()').extract()
            item['url']=url
            items.append(item)

        return items

        
