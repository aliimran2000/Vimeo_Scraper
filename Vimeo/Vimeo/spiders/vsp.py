import scrapy
from bs4 import BeautifulSoup
import json
from scrapy.http.request import Request


class V_item(scrapy.Item):
    # define the fields for your item here like:
    videoid = scrapy.Field()
    name = scrapy.Field()
    title = scrapy.Field()
    pass

def video_id_url_generator(number,endnum):
    urldat1 = 'https://player.vimeo.com/video/'
    urldat2 = '/config' 
    
    list_urls = []
    for i in range(number,endnum):
        urlgend = urldat1 + str(i) + urldat2
        list_urls.append(urlgend)

    return list_urls




class VspSpider(scrapy.Spider):
    name = 'vsp'
    allowed_domains = ['https://player.vimeo.com']
    start_urls = ['https://player.vimeo.com/video/441120486/config']
    

    def start_requests(self):
        #ENTER THE STRTUNG VIDEO ID AND ENDING ID BELOW 
       
        start_id = 4000000 
        end_id = 4001000
       
        urls = video_id_url_generator(start_id,end_id)
        #urls = self.start_urls 
        for url in urls:
          yield Request(url, self.parse)
          

    def parse(self, response):
        VI = V_item()

        try:
                
            data = json.loads(response.text)
            name = data['video']['owner']['name']
            title = data['video']['title']
            
            
            VI['name'] = name
            VI['title'] = title
            VI['videoid'] = response.request.url[31:][:7]
  
        except:
            VI['name'] = 'not found'
            VI['title'] = 'not found'
            VI['videoid'] = response.request.url[31:][:7]

        yield VI


