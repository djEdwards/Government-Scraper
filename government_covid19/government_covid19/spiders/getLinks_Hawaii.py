#################
## Hawai'i - GET LINKS - Scraper
## 06/19/20
## DJ Edwards
#################
import scrapy

class getLinks_Hawaii(scrapy.Spider):
    name = "HI_links"

    start_urls = [
    'https://governor.hawaii.gov/category/newsroom/press-releases/',
    'https://governor.hawaii.gov/category/newsroom/press-releases/page/2/',
    'https://governor.hawaii.gov/category/newsroom/press-releases/page/3/',
    'https://governor.hawaii.gov/category/newsroom/press-releases/page/4/',
    'https://governor.hawaii.gov/category/newsroom/press-releases/page/5/'
    ]

    def parse(self, response):
        filename = 'all_HI_links.txt'
        links = response.css('h3 a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))