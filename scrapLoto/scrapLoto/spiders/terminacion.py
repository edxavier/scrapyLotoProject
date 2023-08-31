import scrapy
from bs4 import BeautifulSoup
from scrapLoto.utils import get_logger, time_dic, abort_request
from scrapLoto.api import ApiHelper
from scrapLoto.items import TerminacionItem

logger = get_logger()


class TerminacionSpider(scrapy.Spider):
    name = "terminacion"
    allowed_domains = ["loto.com.ni"]
    start_urls = ["https://loto.com.ni/terminacion2/"]
    custom_settings = {
        'PLAYWRIGHT_ABORT_REQUEST': abort_request
    }
    api = ApiHelper()

    def start_requests(self):
        logger.debug("--- Start requests ---")
        yield scrapy.Request(
            url='https://loto.com.ni/terminacion2/',
            meta={'playwright': True},
            callback=self.parse, errback=self.errback_close_page)

    async def parse(self, response):
        soup = BeautifulSoup(response.xpath("//div[@class='listingTable']").get(), 'html.parser')
        logger.info("--- Parse response ---")
        for d in soup.select('div>div.Rtable--2cols'):
            item = {}
          
            headers = d.select('div.Rtable-cell--head>span')
            item["date_string"] = f"{headers[0].text} | {headers[1].text}"
            item["draw_number"] = headers[2].text[1:]
            item["draw_time"] = time_dic.get(headers[1].text, 0)

            spheres = d.select('div>div.esferas>span')
            item["winning_number"] = spheres[0].text
            self.api.save_terminacion(item)

    async def errback_close_page(self, response):
        page = response.request
        logger.error(page)
        logger.error(response)