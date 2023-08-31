# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class LagrandeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    draw_number = scrapy.Field()
    number1 = scrapy.Field()
    number2 = scrapy.Field()
    number3 = scrapy.Field()
    number4 = scrapy.Field()
    number5 = scrapy.Field()
    gold_number = scrapy.Field()
    date_string = scrapy.Field()
    draw_time = scrapy.Field()

class TerminacionItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    draw_number = scrapy.Field()
    winning_number = scrapy.Field()
    date_string = scrapy.Field()
    draw_time = scrapy.Field()