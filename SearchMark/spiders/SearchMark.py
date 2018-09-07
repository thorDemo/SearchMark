# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from twisted.web._newclient import ResponseNeverReceived
from twisted.internet.error import DNSLookupError
from random import sample

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
            start_urls.append(line.replace('%s', target).strip('\n'))
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


def get_char(num):
    chars = 'zyxwvutsrqponmlkjihgfedcba'
    result = ''.join(sample(chars, num))
    return result
