#################
## Delaware Scraper
## 06/11/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text

from langdetect import detect

class delawareSpider(scrapy.Spider):

    linksFile = open('all_DE_links.txt','r')

    name = "delaware"# - this is what you you use to run. (scrapy crawl califonia -o CA_result.json -t json)

    start_urls = map(lambda link: 'https://news.delaware.gov/'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']

            date = response.css('p::text')[608].get()#IS INCORRECT GO BACK LATER AND FIX.

            title = response.css('h1::text')[1].get()

            url = response.url

            source = 'Delaware State Government'

            text = response.css('p::text')[609].get()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            municipality = "Delaware"

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