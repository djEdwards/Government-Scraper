
#################
## New York (Big Apple) - GET LINKS - Scraper
## 06/23/20
## DJ Edwards
#################
import scrapy

class getLinks_NewYork(scrapy.Spider):
    name = "NY_links"

    start_urls = [
        
        'https://health.ny.gov/press/releases/2020/index.htm'
    ]

    def parse(self, response):
        links = response.css('li > a::attr(href)').getall()
        filename = 'all_NY_links.txt'
        with open(filename,'w') as f:
            f.write(','.join(links))