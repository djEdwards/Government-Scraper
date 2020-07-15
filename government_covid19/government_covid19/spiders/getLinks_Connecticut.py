#################
## Connecticut - GET LINKS - Scraper
## 06/29/20
## DJ Edwards
#################
import scrapy

class getLinks_Connecticut(scrapy.Spider):
    name = "CT_links"

    start_urls = ['https://portal.ct.gov/Coronavirus/Pages/Governors-Press-Releases'
    ]
    def parse(self, response):
        filename = 'all_CT_links.txt'
        links = response.css('td a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))