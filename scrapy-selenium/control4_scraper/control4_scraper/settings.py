# scrapy-selenium/control4_scraper/control4_scraper/settings.py (new file; 100% complete, copy-paste to VSCode, save in control4_scraper/control4_scraper/)
BOT_NAME = 'control4_scraper'

SPIDER_MODULES = ['control4_scraper.spiders']
NEWSPIDER_MODULE = 'control4_scraper.spiders'

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'control4_scraper.pipelines.Control4ScraperPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy_selenium.SeleniumMiddleware': 800,
}

SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = '/usr/local/bin/chromedriver'
SELENIUM_DRIVER_ARGUMENTS=['--headless']  # '--headless' is ok

# scrapy-selenium/control4_scraper/control4_scraper/items.py (new file; 100% complete, copy-paste to VSCode, save in control4_scraper/control4_scraper/)
from scrapy.item import Item, Field

class Control4ScraperItem(Item):
    issue = Field()
    solution = Field()
    product = Field()
    category = Field()
    url = Field()

# scrapy-selenium/control4_scraper/control4_scraper/pipelines.py (new file; 100% complete, copy-paste to VSCode, save in control4_scraper/control4_scraper/)
from itemadapter import ItemAdapter

class Control4ScraperPipeline:
    def process_item(self, item, spider):
        return item

# scrapy-selenium/control4_scraper/control4_scraper/middlewares.py (new file; 100% complete, copy-paste to VSCode, save in control4_scraper/control4_scraper/)
from scrapy import signals