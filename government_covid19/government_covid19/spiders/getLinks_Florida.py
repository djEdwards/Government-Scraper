#################
## FLORIDA - GET LINKS - Scraper
## 06/18/20
## DJ Edwards
#################
import scrapy

class getLinks_Florida(scrapy.Spider):
    name = "FL_links"

    start_urls = [
        'http://www.floridahealth.gov/newsroom/all-articles.html'
    ]

    def parse(self, response):
        links = response.css('h4 > a::attr(href)').getall()
        filename = 'all_FL_links.txt'
        with open(filename,'w') as f:
            f.write(','.join(links))