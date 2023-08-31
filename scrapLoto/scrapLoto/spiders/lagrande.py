import scrapy
from bs4 import BeautifulSoup
from scrapLoto.utils import get_logger, time_dic, abort_request
from scrapLoto.api import ApiHelper
from scrapLoto.items import LagrandeItem

logger = get_logger()


class LagrandeSpider(scrapy.Spider):
    name = "lagrande"
    allowed_domains = ["loto.com.ni"]
    start_urls = ["https://loto.com.ni/lagrande/"]
    custom_settings = {
        'PLAYWRIGHT_ABORT_REQUEST': abort_request
    }
    api = ApiHelper()
    
    def start_requests(self):
        logger.debug("--- Start requests ---")
        yield scrapy.Request(
            url='https://loto.com.ni/lagrande/',
            meta={'playwright': True},
            callback=self.parse, errback=self.errback_close_page)

    async def parse(self, response):
        soup = BeautifulSoup(response.xpath("//div[@class='listingTable']").get(), 'html.parser')
        logger.info("--- Parse response ---")
        for d in soup.select('div>div.Rtable--6cols'):
            item = {}
            
            headers = d.select('div.Rtable-cell--head>span')
            item["date_string"] = f"{headers[0].text} | {headers[1].text}"
            item["draw_number"] = headers[2].text[1:]
            item["draw_time"] = time_dic.get(headers[1].text, 0)

            spheres = d.select('div>div.esferas>span')
            item["number1"] = spheres[0].text
            item["number2"] = spheres[1].text
            item["number3"] = spheres[2].text
            item["number4"] = spheres[3].text
            item["number5"] = spheres[4].text
            item["gold_number"] = spheres[5].text
            self.api.save_lagrande(item)
            yield item
          
    
    async def errback_close_page(self, response):
        page = response.request
        logger.error(page)
        logger.error(response)
        
