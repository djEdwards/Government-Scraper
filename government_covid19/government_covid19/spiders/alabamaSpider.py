
#################
## Alabama  Scraper
## 06/11/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class alabamaSpider(scrapy.Spider):
    linksFile = open('all_AL_links.txt', 'r')

    name = "alabama"
    start_urls = map(lambda link: 'https://governor.alabama.gov/' + link if link.startswith(
        'https') == False else link, linksFile.read().split(','))

    def parse(self, response):
        now = datetime.utcnow().replace(microsecond=0).isoformat()
        url = response.url
        datetimeToday = now + 'Z'
        textContent = 'todo'
        dateElement = response.css('time::text').get()
        dateElementText = dateElement.replace('\t', '').replace('\n', '').replace('                                 ', '').replace('                 ', '')
        dateElementArray = dateElementText.split(',')
        updatedDateISO = dateparser.parse(dateElementArray[0], languages=['en']).date()
        updatedDateTime = str(updatedDateISO)
        title = response.css('title::text').get()
        contentArray = response.css('p::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace('\\','')
        language = details[0].language_name
        yield{

            'title': title,
            'source': 'Office of the Governor of Alabama',
            'published': updatedDateTime,
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States of America',
            'municipality': 'Alabama',
            'language': language,
            'text': textMinusUnnecessaryChars
        }
 