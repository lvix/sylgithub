# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sylgithub.models import GitBase, engine
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class SylgithubPipeline(object):
    def process_item(self, item, spider):
        item['update_time'] = datetime.strptime(item['update_time'], '%Y-%m-%dT%H:%M:%SZ')
        self.session.add(GitBase(**item))
        return item 

    def open_spider(self, siper):
        '''
        called when spider being opened
        '''
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def close_spider(self, spider):
        '''
        called when sipder is being closed 
        '''
        # print('close spider')
        self.session.commit()
        self.session.close()
