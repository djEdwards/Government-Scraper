#################
## Alabama Scraper
## 06/11/20
## DJ Edwards
#################
import scrapy
from datetime import datetime
import html2text
class alabamaSpider(scrapy.Spider):
    linksFile = open('all_AL_links.txt','r')
    name = "alabama"# - this is what you you use to run. (scrapy crawl alabama -o AL_result.json -t json)
    start_urls = map(lambda link: 'https://governor.alabama.gov/'+ link if link.startswith('https') == False else link,linksFile.read().split(','))


    def parse(self, response):# - Scrapes title, date, and url (working on excerpt)
            converter = html2text.HTML2Text()
            converter.ignore_links = True
            classes = ['Governemnt','News','Social Media']

            manicipalities = ['Multi-National','National','State','Global']

            languages = ['English(US)','Spanish','Chinese','French','Chinese','Japanese','German','Portuguese']

            title = response.css('title::text').get()

            text = response.css('p::text')[6].get()

            date = response.css('time ::text').get()

            url = response.url

            source = 'Office of the Governer of Alabama'

            currentDate = datetime.today().strftime('%Y-%m-%d')

            Class = classes[0]

            manicipality = manicipalities[2]

            langauge = languages[0]

            yield {
                'Title':title,

                'Source':source,

                'Date':date,

                'Url':url,

                'Scraped':currentDate,

                'Class': Class,

                'Manicipality': manicipality,

                'language':langauge,

                # 'text':text

                'text':converter.handle(text)

                }
               