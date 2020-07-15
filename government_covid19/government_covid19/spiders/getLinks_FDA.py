#################
## FDA - GET LINKS - Scraper
## 07/08/20
## DJ Edwards
#################
import scrapy

class getLinks_FDA(scrapy.Spider):
    name = "FDA_links"

    start_urls = ['https://www.fda.gov/emergency-preparedness-and-response/counterterrorism-and-emerging-threats/coronavirus-disease-2019-covid-19'
    ]

    def parse(self, response):
        filename = 'all_FDA_links.txt'
        links = response.css('p a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))