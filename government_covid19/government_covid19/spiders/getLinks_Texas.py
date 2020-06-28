#################
## Texas - GET LINKS - Scraper
## 06/26/20
## DJ Edwards
#################
import scrapy

class getLinks_Texas(scrapy.Spider):
    name = "TX_links"

    start_urls = ['https://gov.texas.gov/news/category/press-release',
                  'https://gov.texas.gov/news/category/press-release/P8',
                  'https://gov.texas.gov/news/category/press-release/P16',
                  'https://gov.texas.gov/news/category/press-release/P24',
                  'https://gov.texas.gov/news/category/press-release/P32',
                  'https://gov.texas.gov/news/category/press-release/P40',
                  'https://gov.texas.gov/news/category/press-release/P48',
                  'https://gov.texas.gov/news/category/press-release/P56',
                  'https://gov.texas.gov/news/category/press-release/P64',
                  'https://gov.texas.gov/news/category/press-release/P72',
                  'https://gov.texas.gov/news/category/press-release/P80',
                  'https://gov.texas.gov/news/category/press-release/P88',
                  'https://gov.texas.gov/news/category/press-release/P96',
                  'https://gov.texas.gov/news/category/press-release/P104',
                  'https://gov.texas.gov/news/category/press-release/P112',
                  'https://gov.texas.gov/news/category/press-release/P120',
                  'https://gov.texas.gov/news/category/press-release/P128',
                  'https://gov.texas.gov/news/category/press-release/P136'

    
    ]
    
    def parse(self, response):
        filename = 'all_TX_links.txt'
        links = response.css('h3 a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))