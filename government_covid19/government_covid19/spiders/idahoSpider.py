#################
## Idaho  Scraper
## 06/19/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class idahoSpider(scrapy.Spider):
    linksFile = open('all_ID_links.txt', 'r')

    name = "idaho"
    start_urls = map(lambda link: 'hhttps://coronavirus.idaho.gov' + link if link.startswith(
        'https') == False else link, linksFile.read().split(','))

    def parse(self, response):
        now = datetime.utcnow().replace(microsecond=0).isoformat()
        url = response.url
        datetimeToday = now + 'Z'
        textContent = 'todo'
        dateElement = response.css('.pr-date.col-12::text').get()
        dateElementText = dateElement.replace('\t', '').replace('\n', '').replace('                                 ', '').replace('                 ', '')
        dateElementArray = dateElementText.split(',')
        updatedDateISO = dateparser.parse(dateElementArray[0], languages=['en']).date()
        # if (dateElement[2][1:]!= None):
        #     updatedTimeISO = dateElementArray[2][1:].replace('h', ':')+'-03:00'  INDEX OUT OF RANGE HERE. SO I AM WORKING AROUND IT FOR NOW.
        updatedDateTime = str(updatedDateISO)
        title = response.css('h2::text').getall()
        contentArray = response.css('p::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace('\\','')
        language = details[0].language_name
        yield{

            'title': title,
            'source': 'Office Of The Governor Of Idaho',
            'published': updatedDateISO,#change it later...
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States',
            'municipality': 'Idaho',
            'language': language,
            'text': textMinusUnnecessaryChars
        }
 