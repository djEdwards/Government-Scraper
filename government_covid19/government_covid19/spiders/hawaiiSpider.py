#################
## Hawaii Scraper
## 06/19/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

class hawaiiSpider(scrapy.Spider):

    linksFile = open('all_HI_links.txt','r')

    name = "hawaii"# - this is what you you use to run. (scrapy crawl califonia -o CA_result.json -t json)

    start_urls = map(lambda link: 'https://governor.hawaii.gov'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']

            date = response.css('.pagetitle ::text')[3].get()

            title = response.css('.pagetitle h2::text').get()

            url = response.url

            source = "Governor of the State of Hawai'i"

            text = response.css('p::text').getall()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            municipality = "Hawai'i"

            # langauge = detect(title)

            yield {

                'title':title,

                'source':source,

                'date':date,

                 'url':url,

                'scraped':currentDate,

                'class': Class,

                'municipality': municipality,

                # 'language':langauge,

                'text':text


               

                
                }