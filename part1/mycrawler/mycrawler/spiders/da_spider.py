# -*- coding: utf-8 -*-

# KonanAcademy's DA class page spider

import re

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http import Request

from ..items import MycrawlerItem

print "==============================================="
print "start KonanAcademy's DA class page crawling...."
print "==============================================="

max_url_count = 1
current_url_count = 1

DA_URL = u"http://konanacademy.github.io/da/"

class DaSpider(Spider) :
    name = "da"
    start_urls = [DA_URL]

    def parse(self, response) :

        global current_url_count, max_url_count

        # 셀렉터 생성
        sel = Selector(response)
        
        # 원하는 태그 리스트 가져오기
        href_list = sel.css('a::attr(href)').extract()

        # http나 https 링크만 추출하자
        links = [link for link in href_list if bool(re.compile("http").match(link))]
        
        items = []
        for link in links :
            item = MycrawlerItem()
            item['url'] = link

            items.append(item)

        return items


