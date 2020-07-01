#################
## Massachusetts Scraper
## 06/27/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class massachusettsSpider(scrapy.Spider):
    linksFile = open('all_MA_links.txt', 'r')

    name = "massachusetts"
    start_urls = map(lambda link: 'https://www.mass.gov' + link if link.startswith(
        'https') == False else link, linksFile.read().split(','))

    def parse(self, response):
        now = datetime.utcnow().replace(microsecond=0).isoformat()
        url = response.url
        datetimeToday = now + 'Z'
        textContent = 'todo'
        dateElement = response.css('.ma__press-status__date::text').get()
        dateElementText = dateElement.replace('\t', '').replace('\n', '').replace('                                 ', '').replace('                 ', '')
        dateElementArray = dateElementText.split(',')
        updatedDateISO = dateparser.parse(dateElementArray[0], languages=['en']).date()
        updatedDateTime = str(updatedDateISO)
        title = response.css('h1::text').get()
        titleMinusUnnecessaryChars = title.replace('\n      ','')
        contentArray = response.css('.ma__rich-text::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace('\n',' ')
        language = details[0].language_name
        yield{

            'title': titleMinusUnnecessaryChars,
            'source': 'Massachusetts State Government',
            'published': updatedDateTime,
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States',
            'municipality': 'Massachusetts',
            'language': language,
            'text': textMinusUnnecessaryChars
        }
 
