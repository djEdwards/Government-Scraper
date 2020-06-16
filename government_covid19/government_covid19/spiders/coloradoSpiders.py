#################
## Colorado Scraper
## 06/11/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

class coloradoSpider(scrapy.Spider):

    linksFile = open('all_CO_links.txt','r')

    name = "colorado"# - this is what you you use to run. (scrapy crawl alabama -o AL_result.json -t json)

    start_urls = map(lambda link: 'https://covid19.colorado.gov/'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True

            classes = ['Governemnt','News','Social Media']

            languages = ['English(US)','Spanish','Chinese','French','Chinese','Japanese','German','Portuguese']

            title = response.css('.page-header::text').getall()

            # text = response.css('p::text').get()

            date = response.css('time ::text').get()

            url = response.url

            source = 'Colorado Dept. of Health and Environment'

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            manicipality = "Colorado"

            langauge = detect()

            yield {

                'title':title,

                'source':source,

                'date':date,

                'url':url,

                'scraped':currentDate,

                'class': Class,

                'manicipality': manicipality,

                'language':langauge

                # 'text':text

                # 'text':converter.handle(text)

                }
               