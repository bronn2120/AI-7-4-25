from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from ..items import LutronScraperItem
from dotenv import load_dotenv
import os
import logging
import time

class LutronSpider(CrawlSpider):
    name = 'lutron'
    allowed_domains = ['lutron.com', 'support.lutron.com']
    start_urls = [
        'https://support.lutron.com/us/en',
        'https://www.lutron.com/TechnicalDocumentLibrary'
    ]

    rules = (
        Rule(LinkExtractor(allow=('/support/', '/article/', '/products/', '/technical/', '/resources/', '/help/', '/instructions/', '/search')), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=('/page/[0-9]+', '/next', '/more')), follow=True),
)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_logger = logging.getLogger(__name__)
        self.custom_logger.info("LutronSpider initialized")
        load_dotenv(dotenv_path='/home/vincent/ixome/.env')
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.binary_location = '/opt/google/chrome/chrome'
        service = Service('/usr/local/bin/chromedriver')
        self.driver = webdriver.Chrome(service=service, options=options)
        self.custom_logger.info("ChromeDriver initialized")

    def start_requests(self):
        for url in self.start_urls:
            self.driver.get(url)
            time.sleep(3)
            try:
                cookie_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
                )
                cookie_button.click()
                self.custom_logger.info("Accepted cookie consent")
            except Exception:
                self.custom_logger.debug("No cookie consent popup found")
            yield Request(
                url=url,
                callback=self.parse,
                meta={'selenium_response': self.driver.page_source}
            )

    def parse(self, response):
        sel = Selector(response)
        links = sel.css('a[href*="/support/"][href*="/article/"]::attr(href), a[href*="/instructions/"]::attr(href), a[href*="/product/"]::attr(href)').getall()
        for link in links:
            absolute_url = response.urljoin(link)
            if any(domain in absolute_url for domain in self.allowed_domains):
                try:
                    self.driver.get(absolute_url)
                    time.sleep(3)
                    try:
                        cookie_button = WebDriverWait(self.driver, 5).until(
                            EC.element_to_be_clickable((By.ID, 'onetrust-accept-btn-handler'))
                        )
                        cookie_button.click()
                        self.custom_logger.info(f"Accepted cookie consent for {absolute_url}")
                    except Exception:
                        self.custom_logger.debug(f"No cookie consent popup found for {absolute_url}")
                    # Scroll to load dynamic content
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(1)
                    yield Request(
                        url=absolute_url,
                        callback=self.parse_item,
                        meta={'selenium_response': self.driver.page_source}
                    )
                except Exception as e:
                    self.custom_logger.error(f"Error accessing {absolute_url}: {e}")
        yield from super().parse(response)

    def parse_item(self, response):
        if 'selenium_response' in response.meta:
            sel = Selector(text=response.meta['selenium_response'])
        else:
            sel = response
        item = LutronScraperItem()
        item['issue'] = sel.css('h1::text, h2::text, h3::text, h4::text, .coh-heading::text, .card-title::text, .panel-title::text').get(default='').strip()
        item['solution'] = ' '.join(sel.css('div.card-content p::text, div.panel-body p::text, div.top-category-list-content p::text, ul li::text, .faq-answer::text, .instructions::text, div.modal-body p::text, div.content p::text, div.article-content p::text').getall()).strip()
        item['product'] = sel.css('h3::text, .coh-heading::text, .card-title::text, .product-name::text, .product-detail::text').get(default='').strip()
        item['category'] = (
            'Troubleshooting' if any(x in response.url.lower() for x in ['troubleshoot', 'support', 'technical', 'help', 'faq', 'instructions'])
            else 'General'
        )
        item['url'] = response.url

        if item['issue'] or item['solution'] or item['product']:
            self.custom_logger.info(f"Scraped item from {response.url}: issue='{item['issue'][:50]}...'")
            yield item
        else:
            self.custom_logger.debug(f"Discarded item from {response.url}: no meaningful content")

    def closed(self, reason):
        try:
            self.driver.quit()
            self.custom_logger.info("ChromeDriver closed")
        except Exception as e:
            self.custom_logger.error(f"Error closing driver: {e}")
        self.custom_logger.info(f"Spider closed: {reason}")