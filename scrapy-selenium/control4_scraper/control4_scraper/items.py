from scrapy.item import Item, Field

class Control4ScraperItem(Item):
    issue = Field()
    solution = Field()
    product = Field()
    category = Field()
    url = Field()