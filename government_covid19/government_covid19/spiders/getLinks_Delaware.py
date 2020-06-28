#################
## Delaware - GET LINKS - Scraper
## 06/18/20
## DJ Edwards
#################
import scrapy

class getLinks_Delaware(scrapy.Spider):
    name = "DE_links"

    start_urls = ['https://news.delaware.gov/tag/coronavirus/'
    
    ]
    global filename
    def parse(self, response):
        filename = 'all_DE_links.txt'
        links = response.css('h3 a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))