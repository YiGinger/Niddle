# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from stackoverflow.items import StackoverflowItem

class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["careers.stackoverflow.com"]
    start_urls = (
        'http://careers.stackoverflow.com/jobs/tag/data-science',
    )

    def parse(self, response):
        print 'start to scrapy\n'
        res=Selector(response)
        blocks=res.xpath('//div[@class="listResults"]//div[@class="-item -job"]')
        items=[]
        for block in blocks:
	        item=StackoverflowItem()
            item['jobtitle']=block.xpath('.//h3//@title').extract()
            item['job_url']=block.xpath('.//h3//a//@href').extract()
            item['job_tag']=block.xpath('.//a[@class="post-tag job-link"]//text()').extract()
            item['time']=block.xpath('.//p[@class="text _small _muted posted top"]//text()').extract()
            item['company']=block.xpath('.//p[@class="text _small location"]//text()').extract()[1]
            item['location']=block.xpath('.//p[@class="text _small location"]//text()').extract()[2]
        items.append(item)

        return items
     
