# -*- coding: utf-8 -*-

import scrapy
from display.items import DisplayItem
from scrapy.selector import Selector
class DisplaySpider(scrapy.Spider):
  name = "display"
  #allowed_domains = ["sh.ganji.com"]
  start_urls = [ "http://sh.ganji.com/site/s/_" ]
  def __init__(self, category=None, *args, **kwargs):
    super(DisplaySpider, self).__init__(*args, **kwargs)
    self.start_urls = [ "http://sh.ganji.com/site/s/_%s" % category ]

  def printhxs(self, hxs):
    for i in hxs:
      print i.encode('utf-8')

  def parse (self, response):
    sel = Selector(response)
    sites = sel.xpath('//div[@class="job-wanted"]/dl')
    for site in sites:
      item = DisplayItem()
      #item['title'] = site.xpath('dt[@class="f-introd"]/a/text()').extract()
      #item['address'] = site.xpath('dd[@class="addr"]/a/text()').extract()
      #item['time'] = site.xpath('dd[@class="j-time"]/text()').extract()
      #item['url'] = site.xpath('dt[@class="f-introd"]/a/@href').extract()
      titletmp = site.xpath('dt[@class="f-introd"]/a/text()').extract()
      addresstmp = site.xpath('dd[@class="addr"]/a/text()').extract()
      timetmp = site.xpath('dd[@class="j-time"]/text()').extract()
      urltmp = site.xpath('dt[@class="f-introd"]/a/@href').extract()
      for title, address, time, url in zip(titletmp,addresstmp,timetmp,urltmp):
        item['title'] = title.encode('utf-8')
        item['address'] = address.encode('utf-8')
        item['time'] = time.encode('utf-8')
        item['url'] = url
      yield item
