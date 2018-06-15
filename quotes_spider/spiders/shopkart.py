# -*- coding: utf-8 -*-
import scrapy


class ShopkartSpider(scrapy.Spider):
    name = 'shopkart'
    allowed_domains = ['easyday.in/']
    start_urls = ['https://www.easyday.in//']

    def parse(self, response):
        items = response.xpath('//*[@class="prod-list home-prod"]/li/a')
        for item in items:
            discount = item.xpath('.//*[@class="discount"]/text()').extract_first()
            image_url = item.xpath('.//*[@class="img-box"]/img/@src').extract_first()
            name = item.xpath('.//*[@class="name"]/text()').extract_first()
            category = item.xpath('.//*[@class="category"]/text()').extract_first()
            weight = item.xpath('.//*[@class="weight"]/text()').extract_first()
            market_price = item.xpath('.//*[@class="strike"]/text()').extract_first()
            easyday_price = item.xpath('.//*[@class="price right"]/h2/span/text()').extract_first()

            yield {
                'discount': discount,
                'image_url': image_url,
                'name': name,
                'category': category,
                'weight': weight,
                'market_price': market_price,
                'easyday_price': easyday_price
            }
