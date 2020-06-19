#################
## FLORIDA "SUNSHINE" Scraper
## 06/18/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

class floridaSpider(scrapy.Spider):

    linksFile = open('all_FL_links.txt','r')

    name = "florida"# - this is what you you use to run. (scrapy crawl florida -o FL_result.json -t json)

    start_urls = map(lambda link: 'http://www.floridahealth.gov/'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']

            date = response.css('.date::text').extract()

            title = response.css('.headline h::text').get()

            url = response.url

            source = 'Florida State Government'

            text = response.css('p::text')[2].get()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            municipality = "Florida"

            langauge = detect(text)

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