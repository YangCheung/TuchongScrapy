import re
import json


from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import HtmlResponse
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle


from tuchong.items import *


class TencentSpider(CrawlSpider):
    name = "tuchong"
    allowed_domains = ["tuchong.com"]
    start_urls = [
        "http://tuchong.com/tags/%E9%A3%8E%E5%85%89/"
    ]
    # rules = [ 
    #     Rule(sle(allow=("/position.php\?&start=\d{,4}#a")), follow=True, callback='parse_item')
    # ]

    def parse_dummy_list(self, dummy_list):
        if dummy_list:
            return dummy_list[0]
        else:
            return ""

    def parse(self, response): 
        sel = HtmlXPathSelector(response)
        base_url = get_base_url(response)

        sites = sel.xpath('//article[@class="post-grid"]')
        
        items = []
        for site in sites:
            item = TuchongItem()
            item["name"] = self.parse_dummy_list(site.xpath('div[@class="caption"]/h3/a[@class="theatre-view"]/text()').extract())
            item["img"] = self.parse_dummy_list(site.xpath('a[@class="post-cover theatre-view"]/img/@src').extract())
            item["url"] = self.parse_dummy_list(site.xpath('div[@class="caption"]/h3/a[@class="theatre-view"]/@href').extract())
            items.append(item)

        # sites_even = sel.css('table.tablelist tr.even')
        # for site in sites_even:
        #     item = TencentItem()
        #     item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
        #     relative_url = site.css('.l.square a').xpath('@href').extract()[0]
        #     item['detailLink'] = urljoin_rfc(base_url, relative_url)
        #     item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
        #     item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
        #     item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
        #     item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
        #     items.append(item)
        #     #print repr(item).decode("unicode-escape") + '\n'

        # sites_odd = sel.css('table.tablelist tr.odd')
        # for site in sites_odd:
        #     item = TencentItem()
        #     item['name'] = site.css('.l.square a').xpath('text()').extract()[0]
        #     relative_url = site.css('.l.square a').xpath('@href').extract()[0]
        #     item['detailLink'] = urljoin_rfc(base_url, relative_url)
        #     item['catalog'] = site.css('tr > td:nth-child(2)::text').extract()[0]
        #     item['workLocation'] = site.css('tr > td:nth-child(4)::text').extract()[0]
        #     item['recruitNumber'] = site.css('tr > td:nth-child(3)::text').extract()[0]
        #     item['publishTime'] = site.css('tr > td:nth-child(5)::text').extract()[0]
        #     items.append(item)
            #print repr(item).decode("unicode-escape") + '\n'

        # info('parsed ' + str(response))
        return items




    # def _process_request(self, request):
    #     info('process ' + str(request))
    #     return request
