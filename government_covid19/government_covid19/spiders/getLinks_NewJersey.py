#################
## New Jersey - GET LINKS - Scraper
## 06/24/20
## DJ Edwards
#################
import scrapy

class getLinks_NewJersey(scrapy.Spider):
    name = "NJ_links"

    start_urls = ['https://nj.gov/governor/news/news/562020/approved/news_archive.shtml'
    ]
    def parse(self, response):
        filename = 'all_NJ_links.txt'
        links = response.css('.content a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))