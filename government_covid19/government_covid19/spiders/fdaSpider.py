#################
## FDA- Scraper
## 07/08/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class fdaSpider(scrapy.Spider):
    linksFile = open('all_FDA_links.txt', 'r')

    name = "fda"
    start_urls = map(lambda link: 'https://www.fda.gov/' + link if link.startswith(
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
        tempTitle = response.css('.content-title.text-center::text').get()
        if( tempTitle == '\n  '):
            title = response.css(".field--item::text").get()
        else:
            title = tempTitle
        contentArray = response.css('p::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace("Federal government websites often end in .gov or .mil. Before sharing\nsensitive information, make sure you're on a federal government site. The\nensures that you are connecting to the official website and that any\ninformation you provide is encrypted and transmitted securely.","").replace('\\','')
        language = details[0].language_name
        yield{
            'title': title,
            'source': 'Federal Dept. Of Agriculture',
            'published': updatedDateISO,
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States of America',
            'municipality': 'Federal Government',
            'language': language,
            'text': textMinusUnnecessaryChars
        }
