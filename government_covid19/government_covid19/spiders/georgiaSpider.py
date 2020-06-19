#################
## Golden State Scraper
## 06/11/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

class californiaSpider(scrapy.Spider):

    linksFile = open('all_GA_links.txt','r')

    name = "georgia"# - this is what you you use to run. (scrapy crawl califonia -o CA_result.json -t json)

    start_urls = map(lambda link: 'https://gov.georgia.gov/'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']

            date = response.css('time::text').extract()

            title = response.css('.page-top__title--news::text').get()

            url = response.url

            source = 'Office of the Governer of Georgia'

            text = response.css('p::text')[7].get()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            municipality = "Georgia"

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