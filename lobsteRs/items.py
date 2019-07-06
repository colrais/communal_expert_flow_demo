# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
class LobsteRsItem(scrapy.Item):
    post_title = scrapy.Field()
    op_upvotes = scrapy.Field()
    poster = scrapy.Field()
    age = scrapy.Field()
    num_comments = scrapy.Field()
    tags = scrapy.Field()
    reflink = scrapy.Field()
    commenter = scrapy.Field()
    com_upvotes = scrapy.Field()
    comment = scrapy.Field()
    com_age = scrapy.Field()
    net = scrapy.Field()
#     postID = scrapy.Field()
#
# class CommentsItem(scrapy.Item):
#     postID = scrapy.Field()
#     commentID = scrapy.Field()
#     commenter = scrapy.Field()
#     com_upvotes = scrapy.Field()
#     comment = scrapy.Field()
#     com_age = scrapy.Field()
