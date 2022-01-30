# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter


class BiliPipeline(object):
    def __init__(self):
        # a为追加写入模式，这里要用二进制的方式打开
        self.fp=open('bilibili.csv','ab')
        #include_headers_line默认为True
        # 能够帮我们自动写入表头，并且在追加写入数据的时候不会造成表头重复
        self.exportre=CsvItemExporter(
            self.fp,
            include_headers_line=True,
            encoding='utf-8-sig'
        )
    def open_spider(self,spider):
        pass

    # 向csv文件中写入数据
    def process_item(self,item,spider):
        self.exportre.export_item(item)
        return item

    def close_spider(self,spider):
        self.fp.close()
