#################
## COVID TASK FORCE  Scraper
## 07/13/20
## DJ Edwards
#################
import scrapy
import html2text
import cld2
import dateparser
from datetime import datetime
from functools import reduce


class covidtaskforceSpider(scrapy.Spider):
    linksFile = open('all_CTF_links.txt', 'r')

    name = "covidtaskforce"
    start_urls = map(lambda link: 'https://www.rev.com' + link if link.startswith(
        'https') == False else link, linksFile.read().split(','))

    def parse(self, response):
        now = datetime.utcnow().replace(microsecond=0).isoformat()
        url = response.url
        datetimeToday = now + 'Z'
        textContent = 'todo'
        dateElementText = response.xpath('//*[@id="fl-main-content"]/div[1]/div/div/div/div[2]/div/div/div[1]/div/div/p/text()').get()
        dateElementArray = dateElementText.split(',')
        updatedDateISO = dateparser.parse(dateElementArray[0], languages=['en']).date()
        updatedDateTime = str(updatedDateISO)
        title = response.css('.fl-heading-text::text').get()
        contentArray = response.css('.fl-callout-text p::text').extract()
        converter = html2text.HTML2Text()
        converter.ignore_links = True
        text = reduce(lambda first, second: converter.handle(first)+converter.handle(second), contentArray)
        isReliable, textBytesFound, details = cld2.detect(text)
        textMinusUnnecessaryChars = text.replace('\\','')
        language = details[0].language_name
        yield{

            'title': title,
            'source': 'Covid-19 Presidential Task Force ',
            'published': updatedDateTime,
            'url': url,
            'scraped': datetimeToday,
            'classes': ['Government'],
            'country': 'United States of America',
            'municipality': 'US Government',
            'language': language,
            'text': textMinusUnnecessaryChars
        }
 