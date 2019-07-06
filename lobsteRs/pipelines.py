# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import CsvItemExporter

class LobsteRsPipeline(object):
    def __init__(self):
        self.filename = "lobsteRs.csv"

    def open_spider(self, spider):
        self.csvfile = open(self.filename, 'wb')
        self.exporter = CsvItemExporter(self.csvfile)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item, LobsteRsItem):
            self.exporter.export_item(item)
        return item

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.csvfile.close()

# class CommentsPipeline(object):
#     def __init__(self):
#         self.filename = "comments.csv"
#
#     def open_spider(self,spider):
#         self.csvfile = open(self.filename, 'wb')
#         self.exporter = CsvItemExporter(self.csvfile)
#         self.exporter.start_exporting()
#
#     def process_item(self, item, spider):
#         if isinstance(item, CommentsItem):
#             self.exporter.export_item(item)
#         return item
#
#     def close_spider(self, spider):
#         self.exporter.finish_exporting()
#         self.csvfile.close()
