from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
import time
import webdriver_manager.chrome
from selenium import webdriver

class SeleniumMiddleware:
    def __init__(self, driver_name, driver_executable_path, browser_executable_path, driver_arguments, driver_headless):
        options = ChromeOptions()
        if driver_headless:
            options.add_argument('--headless')
        for argument in driver_arguments:
            options.add_argument(argument)
        if browser_executable_path:
            options.binary_location = browser_executable_path
        service = ChromeService(executable_path=driver_executable_path)
        self.driver = webdriver.Chrome(service=service, options=options)

    @classmethod
    def from_crawler(cls, crawler):
        driver_name = crawler.settings.get('SELENIUM_DRIVER_NAME')
        driver_executable_path = crawler.settings.get('SELENIUM_DRIVER_EXECUTABLE_PATH')
        browser_executable_path = crawler.settings.get('SELENIUM_BROWSER_EXECUTABLE_PATH')
        driver_arguments = crawler.settings.get('SELENIUM_DRIVER_ARGUMENTS')
        driver_headless = crawler.settings.get('SELENIUM_HEADLESS', True)
        if driver_name is None:
            raise ValueError("You need to specify SELENIUM_DRIVER_NAME in settings.py")
        middleware = cls(driver_name, driver_executable_path, browser_executable_path, driver_arguments, driver_headless)
        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)
        return middleware

    def process_request(self, request, spider):
        if not request.meta.get('selenium'):
            return None
        self.driver.get(request.url)
        for cookie_name, cookie_value in request.meta.get('cookies', {}).items():
            self.driver.add_cookie({'name': cookie_name, 'value': cookie_value})
        if request.meta.get('wait_until'):
            WebDriverWait(self.driver, request.meta['wait_time']).until(request.meta['wait_until'])
        if request.meta.get('screenshot'):
            request.meta['screenshot'] = self.driver.get_screenshot_as_png()
        if request.meta.get('script'):
            self.driver.execute_script(request.meta['script'])
        body = to_bytes(self.driver.page_source)
        return HtmlResponse(self.driver.current_url, body=body, encoding='utf-8', request=request)

    def spider_closed(self):
        self.driver.quit()