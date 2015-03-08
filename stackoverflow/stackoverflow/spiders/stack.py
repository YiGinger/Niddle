# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from stackoverflow.items import StackoverflowItem


class StackSpider(CrawlSpider):
    name = 'stack'
    allowed_domains = ['careers.stackoverflow.com']
    start_urls = ['http://careers.stackoverflow.com/jobs/tag/data-science']

    rules = (
        Rule(LinkExtractor(allow=r'http://careers.stackoverflow.com/jobs/tag/data-science\?pg=\d*',
            restrict_xpaths=('//a[@class="prev-next job-link test-pagination-next"]')), 
        callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print 'start to scrapy\n\n'
        item = StackoverflowItem()
        res = Selector(response)
        blocks = res.xpath('//div[@class="listResults"]//div[@class="-item -job"]')
        items = []
        for block in blocks:
            item = StackoverflowItem()
            item['jobtitle'] = block.xpath('.//h3//@title').extract()
            item['job_url'] = block.xpath('.//h3//a//@href').extract()
            item['job_tag'] = block.xpath('.//a[@class="post-tag job-link"]//text()').extract()
            item['time'] = block.xpath('.//p[@class="text _small _muted posted top"]//text()').extract()
            item['company'] = block.xpath('.//p[@class="text _small location"]//text()').extract()[1]
            item['location'] = block.xpath('.//p[@class="text _small location"]//text()').extract()[2]
            items.append(item)
            
        return items


    
