# -*- coding: utf-8 -*-
import scrapy


class GenreDramaSpider(scrapy.Spider):
    name = 'genre_drama'
    allowed_domains = ['https://www6.fmovies.io/genre/drama.html']
    start_urls = ['http://https://www6.fmovies.io/genre/drama.html/']

    def parse(self, response):
        movies = response.xpath('//figure/')
        for movie in movies:
            href = movie.xpath('.//a/@href').extract_first()
            title = movie.xpath('.//a/@title').extract_first()
            quality = movie.xpath('.//*[@class="quanlity"]/text()').extract_first()
            imdb = movie.xpath('.//*[@class="time"]/text()').extract_first()
            
