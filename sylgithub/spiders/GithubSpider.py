# -*- coding: utf-8 -*-
import scrapy
from sylgithub.items import GitItem

class GithubspiderSpider(scrapy.Spider):
    name = 'GithubSpider'
    # allowed_domains = ['http://github.com']
    # start_urls = ['http://http://github.com/']
    url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
    @property 
    def start_urls(self):
        return [self.url_tmpl.format(i) for i in range(1, 5)]

    def parse(self, response):
        repos = response.xpath('//*[@id="user-repositories-list"]/ul/li')
        for repo in repos:
            item = GitItem()      
            item['name'] = repo.xpath('div[1]/h3/a/text()').re_first('[\s*](\S.*)')
            item['update_time'] = repo.xpath("div[3]/relative-time/@datetime").extract_first()
            page_url = 'https://github.com' + repo.xpath('div[1]/h3/a/@href').extract_first()
            request = scrapy.Request(page_url, callback=self.parse_repo)
            request.meta['item'] = item
            yield request

    def parse_repo(self, response):
        item = response.meta['item']
        # item['author'] = response.xpath('//div[@class="mooc-info"]/div[@class="name"]/strong/text()').extract_first()
        item['commits'] = response.xpath('//span[@class="num text-emphasized"]/text()').re('[\s*]([\d,]*)[\s]*$')[0]
        item['branches'] = response.xpath('//span[@class="num text-emphasized"]/text()').re('[\s*]([\d,]*)[\s]*$')[1]
        item['releases'] = response.xpath('//span[@class="num text-emphasized"]/text()').re('[\s*]([\d,]*)[\s]*$')[2]
        yield item

