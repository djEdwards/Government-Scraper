#################
## Golden State - GET LINKS - Scraper
## 06/11/20
## DJ Edwards
#################import scrapy

import scrapy

class getLinks_California(scrapy.Spider):
    name = "CA_links"

    start_urls = [
        
        'https://covid19.ca.gov/latest-news/'
    ]

    def parse(self, response):
        links = response.css('.row ::attr(href)').getall()
        filename = 'all_CA_links.txt'
        with open(filename,'w') as f:
            f.write(','.join(links))