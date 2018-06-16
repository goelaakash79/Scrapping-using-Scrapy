# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    # allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/login']

    def parse(self, response):
        token = response.xpath('//*[@name="csrf_token"]/@value').extract_first()

        return FormRequest.from_response(response,
                                        formdata={'csrf_token':token,
                                                'password':'password',
                                                'username':'hacker'},
                                        callback=self.scrape_home_page)

    def scrape_home_page(self, response):
        open_in_browser(response)
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="keywords"]/@content').extract_first()

            yield { 'Text' : text,
                    'Author' : author,
                    'Tags' : tags }

        next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
        if(next_page_url):
            absolute_next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(absolute_next_page_url, dont_filter=True, callback=self.scrape_home_page)
