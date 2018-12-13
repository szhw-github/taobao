# -*- coding: utf-8 -*-
import scrapy
from log import log
from taobaosearch.settings import START_URL,query
from taobaosearch.items import TaobaosearchItem


class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    page=44
    log('SPIDER START')
    start_urls=[START_URL.format(datavalue=page,query=query)]


    def parse(self, response):
        log('parse response')
        text=response.text
        import json
        json_=json.loads(text)

        datapath = 'log/latestpage{}.txt'.format(self.page)
        with open(datapath, 'wt', encoding='utf-8') as f:
            f.write(text)
            f.close()
        auctions=None
        try:
            auctions = json_['mods']['itemlist']['data']['auctions']
        except:
            log('warning:json data error')

        finally:
            if auctions:
                item = TaobaosearchItem()
                for auction in auctions:
                    item['id'] = auction['nid']
                    item['title'] = auction['title']
                    item['pic_url'] = auction['pic_url']
                    item['detail_url'] = auction['detail_url']
                    item['view_price'] = auction['view_price']
                    item['item_loc'] = auction['item_loc']
                    item['view_sales'] = auction['view_sales']
                    item['comment_count'] = auction['comment_count']
                    item['nick'] = auction['nick']
                    yield item

                self.page=self.page+44
                yield scrapy.Request(url=START_URL.format(datavalue=self.page,query=query))



