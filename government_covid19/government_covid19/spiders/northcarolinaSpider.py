#################
## North Carolina - Scraper
## 06/29/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class northcarolinaSpider(scrapy.Spider):
    linksFile = open('all_NC_links.txt', 'r')

    name = "northcarolina"
    start_urls = map(lambda link: 'https://www.nc.gov' + link if link.startswith(
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
        title = response.css('h1::text').get()
        titleMinusUnecessary = title.replace('\n                  ','').replace('                                                      ','').replace('                                                    ','')
        contentArray = response.css('p::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace('\n',' ').replace('\\','')
        language = details[0].language_name
        yield{
            'title': titleMinusUnecessary,
            'source': 'Carolina State Government',
            'published': updatedDateISO,
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States',
            'municipality': 'North Carolina',
            'language': language,
            'text': textMinusUnnecessaryChars
        }

