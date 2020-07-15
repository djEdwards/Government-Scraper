#################
## Utah - GET LINKS - Scraper
## 07/06/20
## DJ Edwards
#################

import scrapy

class getLinks_Utah(scrapy.Spider):
    name = "UT_links"

    start_urls = [
        
        'https://health.utah.gov/news',
        'https://health.utah.gov/news/page/2'
    ]

    def parse(self, response):
        filename = 'all_UT_links.txt'
        links = response.css('.entry-title a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))