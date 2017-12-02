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
        for item in repos:
            name = item.xpath('div[1]/h3/a/text()').re_first('[\s*](\S.*)'),
            update_time = item.xpath("div[3]/relative-time/@datetime").extract_first()
            yield GitItem({'name':name, 'update_time':update_time})