#################
## COLORADO (ROCK MT) - GET LINKS - Scraper
## 06/15/20
## DJ Edwards
#################
import scrapy

class getLinks_Colorado(scrapy.Spider):
    name = "CO_links"

    start_urls = [
        
        'https://covid19.colorado.gov/category/press-release'
    ]

    def parse(self, response):
        links = response.css('.views-row ::attr(href)').getall()
        filename = 'all_CO_links.txt'
        with open(filename,'w') as f:
            f.write(','.join(links))