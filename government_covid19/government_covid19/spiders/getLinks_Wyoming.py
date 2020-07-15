#################
## Wyoming - GET LINKS - Scraper
## 07/06/20
## DJ Edwards
#################
import scrapy

class getLinks_Wyoming(scrapy.Spider):
    name = "WY_links"

    start_urls = ['https://health.wyo.gov/news/',
                  'https://health.wyo.gov/news/page/2/'
    ]


    def parse(self, response):
        filename = 'all_WY_links.txt'
        links = response.css('.entry-title a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))