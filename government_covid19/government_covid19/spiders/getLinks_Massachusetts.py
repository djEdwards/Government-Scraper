#################
## Massachusetts - GET LINKS - Scraper
## 06/27/20
## DJ Edwards
#################
import scrapy

class getLinks_Massachusetts(scrapy.Spider):
    name = "MA_links"

    start_urls = ['https://www.mass.gov/orgs/department-of-public-health/news',
                  'https://www.mass.gov/orgs/department-of-public-health/news?page=1',
                  'https://www.mass.gov/orgs/department-of-public-health/news?page=2',
                  'https://www.mass.gov/orgs/department-of-public-health/news?page=3',
                  'https://www.mass.gov/orgs/department-of-public-health/news?page=4',
                  'https://www.mass.gov/orgs/department-of-public-health/news?page=5'
    ]
    def parse(self, response):
        filename = 'all_MA_links.txt'
        links = response.css('h2 a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))