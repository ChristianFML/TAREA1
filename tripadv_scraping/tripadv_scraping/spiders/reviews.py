import scrapy
from scrapy.responseTypes import Response
from tripadv_scraping.TripadvScrapingItem import TripadvScrapingItem

class ReviewsSpider(scrapy.Spider):
    name = 'tripadv_scraping'
    # allowed_domains = ['host_base']
    start_urls = ['https://www.tripadvisor.com/Hotels-g295366-Antigua_Sacatepequez_Department-Hotels.html']

    def parse(self, response):
        pass
