#################
## North Carolina - GET LINKS - Scraper
## 06/29/20
## DJ Edwards
#################

import scrapy

class getLinks_NorthCarolina(scrapy.Spider):
    name = "NC_links"

    start_urls = [
        
        'https://www.nc.gov/covid19/covid19-news-releases',
        'https://www.nc.gov/covid19/covid19-news-releases?page=1',
        'https://www.nc.gov/covid19/covid19-news-releases?page=2',
        'https://www.nc.gov/covid19/covid19-news-releases?page=3',
        'https://www.nc.gov/covid19/covid19-news-releases?page=4',
        'https://www.nc.gov/covid19/covid19-news-releases?page=5',
        'https://www.nc.gov/covid19/covid19-news-releases?page=6',
        'https://www.nc.gov/covid19/covid19-news-releases?page=7',
        'https://www.nc.gov/covid19/covid19-news-releases?page=8'
    ]

    def parse(self, response):
        filename = 'all_NC_links.txt'
        links = response.css('h3 a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))