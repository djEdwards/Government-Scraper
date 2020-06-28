#################
## Maine - GET LINKS - Scraper
## 06/27/20
## DJ Edwards
#################
import scrapy

class getLinks_Maine(scrapy.Spider):
    name = "ME_links"

    start_urls = [
        
        'https://www.maine.gov/governor/mills/newsroom',
        'https://www.maine.gov/governor/mills/newsroom?q=newsroom&combine=&page=1',
        'https://www.maine.gov/governor/mills/newsroom?q=newsroom&combine=&page=2',
        'https://www.maine.gov/governor/mills/newsroom?q=newsroom&combine=&page=3',
        'https://www.maine.gov/governor/mills/newsroom?q=newsroom&combine=&page=4',
        'https://www.maine.gov/governor/mills/newsroom?q=newsroom&combine=&page=5',
        'https://www.maine.gov/governor/mills/newsroom?q=newsroom&combine=&page=6'

    ]

    def parse(self, response):
        filename = 'all_ME_links.txt'
        links = response.css('.views-row a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))