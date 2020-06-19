#################
## ARIZONA Scraper
## 06/11/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

import re

class arizonaSpider(scrapy.Spider):

    linksFile = open('all_AZ_links.txt','r')

    name = "arizona"# - this is what you you use to run. (scrapy crawl arizona -o AZ_result.json -t json)

    start_urls = map(lambda link: 'https://ein.az.gov/'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']



            # tempDate = str(response.css('.field_date_created::text').get())
            # date = re.search('        (.*)     ', tempDate)

            date = response.css('.field_date_created::text').get()

            title = response.css('h1::text').get()

            url = response.url

            source = 'Arizona Emergency Information Netowrk'

            text = response.css('p::text')[1].get()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            municipality = "Arizona"

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