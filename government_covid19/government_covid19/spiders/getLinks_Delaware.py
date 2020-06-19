#################
## DELAWARE - GET LINKS - Scraper
## 06/18/20
## DJ Edwards
#################
import scrapy

class getLinks_Delaware(scrapy.Spider):
    name = "DE_links"

    start_urls = ['https://news.delaware.gov/tag/coronavirus/',
                  'https://news.delaware.gov/tag/coronavirus/page/2/',
                  'https://news.delaware.gov/tag/coronavirus/page/3/',
                  'https://news.delaware.gov/tag/coronavirus/page/4/',
                  'https://news.delaware.gov/tag/coronavirus/page/5/',
                  'https://news.delaware.gov/tag/coronavirus/page/6/',
                  'https://news.delaware.gov/tag/coronavirus/page/7/',
                  'https://news.delaware.gov/tag/coronavirus/page/8/',
                  'https://news.delaware.gov/tag/coronavirus/page/9/',
                  'https://news.delaware.gov/tag/coronavirus/page/10/',
                  'https://news.delaware.gov/tag/coronavirus/page/11/',
                  'https://news.delaware.gov/tag/coronavirus/page/12/',
                  'https://news.delaware.gov/tag/coronavirus/page/13/',
                  'https://news.delaware.gov/tag/coronavirus/page/14/',
                  'https://news.delaware.gov/tag/coronavirus/page/15/',
                  'https://news.delaware.gov/tag/coronavirus/page/16/',
                  'https://news.delaware.gov/tag/coronavirus/page/17/',
                  'https://news.delaware.gov/tag/coronavirus/page/18/',
                  'https://news.delaware.gov/tag/coronavirus/page/19/',
                  'https://news.delaware.gov/tag/coronavirus/page/20/',
                  'https://news.delaware.gov/tag/coronavirus/page/21/',
    
    ]
    global filename
    filename = 'all_DE_links.txt'
    def parse(self, response):
        links = response.css('h3 ::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))