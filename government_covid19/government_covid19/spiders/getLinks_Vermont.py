#################
## Vermont - GET LINKS - Scraper
## 06/27/20
## DJ Edwards
#################
import scrapy

class getLinks_Vermont(scrapy.Spider):
    name = "VT_links"

    start_urls = ['https://governor.vermont.gov/press_releases',
                  'https://governor.vermont.gov/press_releases?page=1',
                  'https://governor.vermont.gov/press_releases?page=2',
                  'https://governor.vermont.gov/press_releases?page=3',
                  'https://governor.vermont.gov/press_releases?page=4',
                  'https://governor.vermont.gov/press_releases?page=5',
                  'https://governor.vermont.gov/press_releases?page=6'
    ]

    def parse(self, response):
        filename = 'all_VT_links.txt'
        links = response.css('h2 a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))