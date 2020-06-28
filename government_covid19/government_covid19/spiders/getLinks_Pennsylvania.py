#################
## Pennsylvania - GET LINKS - Scraper
## 06/25/20
## DJ Edwards
#################
import scrapy

class getLinks_Louisana(scrapy.Spider):
    name = "PA_links"

    start_urls = ['https://www.health.pa.gov/topics/disease/coronavirus/Pages/Fact-Sheets.aspx'
    ]


    def parse(self, response):
        filename = 'all_PA_links.txt'
        links = response.css('li a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))