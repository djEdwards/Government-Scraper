#################
## GEORGIA - GET LINKS - Scraper
## 06/18/20
## DJ Edwards
#################
import scrapy

class getLinks_Georgia(scrapy.Spider):
    name = "GA_links"

    start_urls = [
        'https://gov.georgia.gov/press-releases',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=1',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=2',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=3',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=4',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=5',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=6',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=7',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=8',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=9',
        'https://gov.georgia.gov/press-releases?field_press_release_type_target_id=All&page=10'
    ]
    global filename
    def parse(self, response):
        links = response.css('.more-link__link::attr(href)').getall()
        filename = 'all_GA_links.txt'
        with open(filename,'a') as f:
            f.write(','.join(links))