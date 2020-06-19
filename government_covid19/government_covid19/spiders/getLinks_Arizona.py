#################
## ARIZONA - GET LINKS - Scraper
## 06/18/20
## DJ Edwards
#################
import scrapy

class getLinks_Arizona(scrapy.Spider):
    name = "AZ_links"

    start_urls = [
        
        'https://ein.az.gov/search/node/COVID-19',
        'https://ein.az.gov/search/node/COVID-19?page=1',
        'https://ein.az.gov/search/node/COVID-19?page=2',
        'https://ein.az.gov/search/node/COVID-19?page=3',
        'https://ein.az.gov/search/node/COVID-19?page=4',
        'https://ein.az.gov/search/node/COVID-19?page=5',
        'https://ein.az.gov/search/node/COVID-19?page=6',
        'https://ein.az.gov/search/node/COVID-19?page=7',
        'https://ein.az.gov/search/node/COVID-19?page=8'

        
    ]

    def parse(self, response):
        links = response.css('.title a::attr(href)').getall()
        filename = 'all_AZ_links.txt'
        with open(filename,'a') as f:
            f.write(','.join(links))
