#################
## Golden State Scraper
## 06/11/20
## DJ Edwards
#################

import scrapy

from datetime import datetime

import html2text


class californiaSpider(scrapy.Spider):

    linksFile = open('all_CA_links.txt','r')

    name = "california"# - this is what you you use to run. (scrapy crawl califonia -o CA_result.json -t json)

    start_urls = map(lambda link: 'https://covid19.ca.gov'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)

            converter = html2text.HTML2Text()

            converter.ignore_links = True  

            classes = ['Governemnt','News','Social Media']

            languages = ['English(US)','Spanish','Chinese','French','Chinese','Japanese','German','Portuguese']

            date = response.css('time::text').extract()

            title = response.css('h1::text').get()

            url = response.url

            source = 'California State Government'

            text = response.css('p::text').getall()

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            manicipality = "California"

            langauge = languages[0]

            yield {

                'title':title,

                'source':source,

                'date':date,

                 'url':url,

                'scraped':currentDate,

                'class': Class,

                'manicipality': manicipality,

                'language':langauge,

                'text':text


               

                
                }