
from scrapy import Spider, Request
from lobsteRs.items import LobsteRsItem, CommentsItem
import re, itertools

class LobsteRsSpider(Spider):
    name = "lobsteRs_spider"
    allowed_urls = ['https://lobste.rs/']
    start_urls = ['https://lobste.rs/page/1']

    global POSTS
    POSTS = 0

    def parse(self, response):
        all_urls = ['https://lobste.rs/page/{}'.format(x) for x in range(1, 2154)]
        for url in all_urls[::]:
            yield Request(url=url, callback=self.parse_aggregates)
        # pass

    def parse_aggregates(self, response):
        global POSTS

        story_idx = response.xpath('//div[@class = "story_liner h-entry"]')

        for idx in story_idx:
            POSTS += 1

            post_title = idx.xpath('.//span[@class = "link h-cite u-repost-of"]/a[@class= "u-url"]/text()').get()
            op_upvotes = idx.xpath('.//div[@class = "score"]/text()').get()
            poster = idx.xpath('.//a[contains(@class, "u-author h-card ")]/text()').get()
            age = idx.css('span::attr(title)').get()

            num_comments = idx.xpath('.//span[@class = "comments_label"]/a/text()').get()
            num_comments = [re.findall('\d+', num_comments)]
            [empty.append('0') for empty in num_comments if empty == []]
            # num_comments = list(itertools.chain.from_iterable(num_comments))

            tags = idx.xpath('.//span[@class = "tags"]/*/text()').getall()
            reflink = idx.xpath('.//a[@class = "domain"]/text()').get()

            net = LobsteRsItem()
            net['post_title'] = post_title
            net['op_upvotes'] = op_upvotes
            net['poster'] = poster
            net['age'] = age
            net['num_comments'] = num_comments[0]
            net['tags'] = tags
            net['reflink'] = reflink
            net['postID'] = POSTS
            yield net

            if num_comments != '0':
                to_append = idx.xpath('.//span[@class = "comments_label"]/a/@href').get()
                yield Request(url='https://lobste.rs' + to_append, meta ={'postID': net['postID']},
                    callback=self.parse_comments)

            # for num in net['num_comments']:
            # if num_comments == ['0']:
            #     net['commenter'] = ""
            #     net['com_upvotes'] = ""
            #     net['comment'] = ""
            #     net['com_age'] = ""
            #     yield net
            # else:
            #     to_append = idx.xpath('.//span[@class = "comments_label"]/a/@href').get()
            #     yield Request(url='https://lobste.rs' + to_append, meta ={'net': net},
            #         callback=self.parse_comments)

                # for tail in to_append:
                #     yield Request(url='https://lobste.rs' + tail, meta ={'net': net},
                #         callback=self.parse_comments)


    def parse_comments(self, response):
        postID = response.meta['postID']
        print(postID)

        # global COMMENTS
        # COMMENTS += 1
        COMMENTS = 0

        # Isolate an index of root urls for comments
        comment_idx = response.xpath('//div[@class = "comment \n  "]')

        # Extract fields from the
        for idx in comment_idx:
            COMMENTS += 1

            commenter = idx.xpath('.//div[@class = "byline"]/a[@class]/text()').get()
            comment = idx.xpath('.//div[@class = "comment_text"]/*/text()').getall()
            com_upvotes = idx.xpath('.//div[@class = "voters"]/div[@class="score"]/text()').get()
            com_age = idx.xpath('.//div[@class = "byline"]').css('span::attr(title)').get()

            hotpot = CommentsItem()
            hotpot['postID'] = postID
            hotpot['commentID'] = COMMENTS
            hotpot['commenter'] = commenter
            hotpot['comment'] = comment
            hotpot['com_upvotes'] = com_upvotes
            hotpot['com_age'] = com_age
            # hotpot['net'] = net

            yield hotpot
