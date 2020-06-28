
#################
## Idaho - GET LINKS - Scraper
## 06/19/20
## DJ Edwards
#################
import scrapy

class getLinks_Idaho(scrapy.Spider):
    name = "ID_links"

    start_urls = ['https://coronavirus.idaho.gov/governors-actions/'
    ]

    filename = 'all_ID_links.txt'
    def parse(self, response):
        links = response.css('li a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))