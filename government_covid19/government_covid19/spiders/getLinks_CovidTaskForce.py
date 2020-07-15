#################
## Covid Task Force Transcripts - GET LINKS - Scraper
## 07/13/20
## DJ Edwards
#################
import scrapy

class getLinks_CovidTaskForce(scrapy.Spider):
    name = "CTF_links"

    start_urls = ['https://www.rev.com/blog/transcript-tag/trump-coronavirus-task-force-briefing-transcripts',
                  'https://www.rev.com/blog/transcript-tag/trump-coronavirus-task-force-briefing-transcripts/page/2',
                  'https://www.rev.com/blog/transcript-tag/trump-coronavirus-task-force-briefing-transcripts/page/3',
                  'https://www.rev.com/blog/transcript-tag/trump-coronavirus-task-force-briefing-transcripts/page/4',
                  'https://www.rev.com/blog/transcript-tag/trump-coronavirus-task-force-briefing-transcripts/page/5'
                  
    ]
    def parse(self, response):
        filename = 'all_CTF_links.txt'
        links = response.css('.fl-post-grid a::attr(href)').getall()
        with open(filename,'a') as f:
            f.write(','.join(links))