#################
## Alabama - GET LINKS - Scraper
## 06/11/20
## DJ Edwards
#################
import scrapy

class getLinks_Alabama(scrapy.Spider):
    name = "AL_links"

    start_urls = [
        
        'https://governor.alabama.gov/newsroom/tag/covid-19/',
        'https://governor.alabama.gov/newsroom/tag/covid-19/page/2/',
        'https://governor.alabama.gov/newsroom/tag/covid-19/page/3/',
        'https://governor.alabama.gov/newsroom/tag/covid-19/page/4/',
        'https://governor.alabama.gov/newsroom/tag/covid-19/page/5/'

    ]

    def parse(self, response):
        filename = 'all_AL_links.txt'
        links = response.css('.story-title ::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))