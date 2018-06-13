# -*- coding: utf-8 -*-
import scrapy


class MoviesexampleSpider(scrapy.Spider):
    name = 'moviesexample'
    allowed_domains = ['showmymovie.herokuapp.com']
    start_urls = ['http://showmymovie.herokuapp.com/']

    def parse(self, response):
        pass
