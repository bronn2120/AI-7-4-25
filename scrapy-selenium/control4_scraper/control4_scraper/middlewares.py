# scrapy-selenium/control4_scraper/control4_scraper/middlewares.py (Overwrite; 100% complete, copy-paste to VSCode, save. Patched for Selenium 4+ - uses Service instead of executable_path, fits existing without deletions)
from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.options import Options as IEOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.chrome.webdriver import WebDriver as ChromeDriver
from selenium.webdriver.firefox.webdriver import WebDriver as FirefoxDriver
from selenium.webdriver.edge.webdriver import WebDriver as EdgeDriver
from selenium.webdriver.ie.webdriver import WebDriver as IEDriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.ie.service import Service as IEService
import time

class SeleniumMiddleware(object):
    """Scrapy middleware handling the requests using selenium"""

    def __init__(self, driver_name, driver_executable_path, browser_executable_path, command_executor, driver_arguments, driver_headless):
        """Initialize the selenium webdriver

        Parameters
        ----------
        driver_name: str
            The selenium ``WebDriver`` to use
        driver_executable_path: str
            The path of the executable binary of the driver
        browser_executable_path: str
            The path of the executable binary of the browser
        command_executor: str
            The comand executor url for remote web driver
        driver_arguments: list
            A list of arguments to initialize the driver
        driver_headless: bool
            Whether to use headless mode or not

        """
        driver_klass = self.load_driver_klass(driver_name)
        driver_options_klass = self.load_driver_options_klass(driver_name)
        service_klass = self.load_service_klass(driver_name)

        driver_options = driver_options_klass()
        if driver_headless:
            driver_options.add_argument('--headless')

        for argument in driver_arguments:
            driver_options.add_argument(argument)

        if browser_executable_path:
            driver_options.binary_location = browser_executable_path

        driver_kwargs = {}
        if command_executor:
            driver_kwargs['command_executor'] = command_executor

        service = service_klass(executable_path=driver_executable_path)
        self.driver = driver_klass(service=service, options=driver_options, **driver_kwargs)

    @staticmethod
    def load_driver_klass(driver_name):
        driver_name = driver_name.lower()
        if driver_name == 'firefox':
            return FirefoxDriver
        elif driver_name == 'chrome':
            return ChromeDriver
        elif driver_name == 'ie':
            return IEDriver
        elif driver_name == 'edge':
            return EdgeDriver
        elif driver_name == 'remote':
            return RemoteWebDriver
        else:
            raise ValueError("No supported driver named {}".format(driver_name))

    @staticmethod
    def load_driver_options_klass(driver_name):
        driver_name = driver_name.lower()
        if driver_name == 'firefox':
            return FirefoxOptions
        elif driver_name == 'chrome':
            return ChromeOptions
        elif driver_name == 'ie':
            return IEOptions
        elif driver_name == 'edge':
            return EdgeOptions
        else:
            raise ValueError("No supported driver named {}".format(driver_name))

    @staticmethod
    def load_service_klass(driver_name):
        driver_name = driver_name.lower()
        if driver_name == 'firefox':
            return FirefoxService
        elif driver_name == 'chrome':
            return ChromeService
        elif driver_name == 'ie':
            return IEService
        elif driver_name == 'edge':
            return EdgeService
        else:
            raise ValueError("No supported driver named {}".format(driver_name))

    @classmethod
    def from_crawler(cls, crawler):
        """Initialize the middleware with the crawler settings"""

        driver_name = crawler.settings.get('SELENIUM_DRIVER_NAME')
        driver_executable_path = crawler.settings.get('SELENIUM_DRIVER_EXECUTABLE_PATH')
        browser_executable_path = crawler.settings.get('SELENIUM_BROWSER_EXECUTABLE_PATH')
        command_executor = crawler.settings.get('SELENIUM_COMMAND_EXECUTOR')
        driver_arguments = crawler.settings.get('SELENIUM_DRIVER_ARGUMENTS')
        driver_headless = crawler.settings.get('SELENIUM_HEADLESS', True)

        if driver_name is None:
            raise ValueError("You need to specify SELENIUM_DRIVER_NAME in settings.py")

        middleware = cls(
            driver_name=driver_name,
            driver_executable_path=driver_executable_path,
            browser_executable_path=browser_executable_path,
            command_executor=command_executor,
            driver_arguments=driver_arguments,
            driver_headless=driver_headless
        )

        crawler.signals.connect(middleware.spider_closed, signals.spider_closed)

        return middleware

    def process_request(self, request, spider):
        """Process a request using the selenium driver if applicable"""

        if not request.meta.get('selenium'):
            return None

        self.driver.get(request.url)

        for cookie_name, cookie_value in request.meta.get('cookies', {}).items():
            self.driver.add_cookie(
                {
                    'name': cookie_name,
                    'value': cookie_value
                }
            )

        if request.meta.get('wait_until'):
            WebDriverWait(self.driver, request.meta['wait_time']).until(
                request.meta['wait_until']
            )

        if request.meta.get('screenshot'):
            request.meta['screenshot'] = self.driver.get_screenshot_as_png()

        if request.meta.get('script'):
            self.driver.execute_script(request.meta['script'])

        body = to_bytes(self.driver.page_source)  # body must be of type bytes

        return HtmlResponse(
            self.driver.current_url,
            body=body,
            encoding='utf-8',
            request=request
        )

    def spider_closed(self):
        """Shutdown the driver when spider is closed"""

        self.driver.quit()