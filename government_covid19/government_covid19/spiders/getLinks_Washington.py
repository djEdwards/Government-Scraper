
#################
## Washington - GET LINKS - Scraper
## 06/24/20
## DJ Edwards
#################
import scrapy

class getLinks_Louisana(scrapy.Spider):
    name = "WA_links"

    start_urls = ['https://coronavirus.wa.gov/news',
                  'https://coronavirus.wa.gov/news?page=1',
                  'https://coronavirus.wa.gov/news?page=2',
                  'https://coronavirus.wa.gov/news?page=3',
                  'https://coronavirus.wa.gov/news?page=4',
                  'https://coronavirus.wa.gov/news?page=5',
                  'https://coronavirus.wa.gov/news?page=6'
    ]

    global filename
    def parse(self, response):
        filename = 'all_WA_links.txt'
        links = response.css('.field-content a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))