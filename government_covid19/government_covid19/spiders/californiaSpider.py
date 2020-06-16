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

            manicipalities = ['Multi-National','National','State','Global']

            languages = ['English(US)','Spanish','Chinese','French','Chinese','Japanese','German','Portuguese']

            date = response.css('time::text').extract(),

            title = response.css('h1::text').get(),

            url = response.url,

            source = 'California State Government',

            text = response.css('p::text').getall(),

            currentDate = datetime.today().strftime('%Y-%m-%d'),

            Class = classes[0],

            manicipality = manicipalities[2],

            langauge = languages[0]

            yield {

                'Title':title,

                'Source':source,

                'Date':date,

                 'URL':url,

                'Scraped':currentDate,

                'Class': Class,

                'Manicipality': manicipality,

                'language':langauge,

                'text':text


               

                
                }

                ##NEXT: figure out next page.