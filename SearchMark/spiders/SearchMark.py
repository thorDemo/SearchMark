# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError
from twisted.web._newclient import ResponseNeverReceived
from twisted.internet.error import DNSLookupError

success = open('success.txt', 'w+')
error = open('error.txt', 'w+')
urls = open('urls.txt', 'r+')


class ExampleSpider(scrapy.Spider):
    name = 'SearchMark'
    start_urls = []
    for line in urls:
        target = 'www.%s' % line
        result = open('domain_1.txt', 'r+')
        for line in result:
            start_urls.append(line.replace('%s', target))
        result.close()

    def parse(self, response):
        se = Selector(response)
        try:
            title = se.xpath('//title/text()').extract()[0]
            success.write(response.url + '\n')
            print(title)
        except IndexError:
            # print(response.text)
            pass
        except ResponseNeverReceived:
            error.write(response.url + ' -- no response')
            print('no response ')
        except DNSLookupError:
            error.write(response.url + ' -- dns error')
