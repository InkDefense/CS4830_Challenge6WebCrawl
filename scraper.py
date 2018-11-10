import scrappy
import time

x = 0
class MasterySpider(scrapy.Spider):
  name = "masteryrank_spider"
   start_urls = ['http://smite.guru/profile/xb/Ink%20Defense/matches']
   
   def parse(self, response):
      global x
      yield {
        'mastery': response.css('.profile-header-stat strong ::text').extract_first()
      }
      next_page = response.css('.team a ::attr(href)').extract_first()
      if x < 8:
        print(x)
        x = x + 1
        time.sleep(3)
        yield scrappy.Request(response.urljoin(next_page))
   
