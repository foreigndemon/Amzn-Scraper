import scrapy

class ScraperItem(scrapy.Item):
    title=scrapy.Field()
    price=scrapy.Field()
    img_url=scrapy.Field()