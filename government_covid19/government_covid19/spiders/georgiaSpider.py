#################
## Georgia  Scraper
## 06/18/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class georgiaSpider(scrapy.Spider):
    linksFile = open('all_GA_links.txt', 'r')

    name = "georgia"
    start_urls = map(lambda link: 'https://gov.georgia.gov' + link if link.startswith(
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
        title = response.css('h1::text').getall()
        contentArray = response.css('p::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace('\\','')
        language = details[0].language_name
        yield{

            'title': title,
            'source': 'Georgia State Government',
            'published': updatedDateTime,
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States',
            'municipality': 'Georgia',
            'language': language,
            'text': textMinusUnnecessaryChars
        }
 