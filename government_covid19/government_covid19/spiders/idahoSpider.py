#################
## Golden State Scraper
## 06/11/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

class idahoSpider(scrapy.Spider):

    linksFile = open('all_ID_links.txt','r')

    name = "idaho"# - this is what you you use to run. (scrapy crawl califonia -o CA_result.json -t json)

    start_urls = map(lambda link: 'hhttps://coronavirus.idaho.gov'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']

            date = response.css('.pr-date.col-12::text').get()

            title = response.css('h2::text').get()

            url = response.url

            source = 'Office Of The Governor Of Idaho'

            text = response.css('p::text').getall()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            municipality = "Idaho"

            langauge = detect(title)

            yield {

                'title':title,

                'source':source,

                'date':date,

                 'url':url,

                'scraped':currentDate,

                'class': Class,

                'municipality': municipality,

                'language':langauge,

                'text':text


               

                
                }
