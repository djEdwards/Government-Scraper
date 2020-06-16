import scrapy

class getLinks_Alabama(scrapy.Spider):
    name = "AL_links"

    start_urls = [
        
        'https://governor.alabama.gov/newsroom/tag/covid-19/'
    ]

    def parse(self, response):
        links = response.css('.story-title ::attr(href)').getall()
        filename = 'all_AL_links.txt'
        with open(filename,'w') as f:
            f.write(','.join(links))