# -*- coding: utf-8 -*-

# Scrapy settings for mycrawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mycrawler'

SPIDER_MODULES = ['mycrawler.spiders']
NEWSPIDER_MODULE = 'mycrawler.spiders'
DEFAULT_ITEM_CLASS = 'mycrawler.items.MycrawlerItem'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mycrawler (+http://www.yourdomain.com)'
