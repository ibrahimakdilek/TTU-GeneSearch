from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support import expected_conditions as Ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException

import undetected_chromedriver as uc
from fake_useragent import UserAgent
import time, os, zipfile

class Config:
        
    def __init__(self):
        pass

    def ChromeSetUp(self, use_proxy=False, user_agent=None):
        path = os.path.dirname(os.path.abspath(__file__))
        chromeOptions = Options()
        if use_proxy:
            pluginFile = "proxyAuthPlugin.zip"

            with zipfile.ZipFile(pluginFile, "w") as zipFile:
                zipFile.writestr("manifest.json", self.manifest_json)
                zipFile.writestr("background.js", self.background_js)
           

        if user_agent:
            chromeOptions.add_argument("--user-agent=%s" % user_agent)
        
        option = webdriver.ChromeOptions()
        chrome_prefs = {}
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2} 
        option.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        option.add_argument("--headless")
        option.add_argument("window-size=1920x1480")
        option.add_argument("disable-dev-shm-usage")
        chromeOptions.add_argument("--disable-blink-features=AutomationControlled")
        driver = webdriver.Chrome("./chromedriver", chrome_options=option)
        return driver

if __name__ == "__main__":
    gleam = Config()
    gleam.ChromeSetUp(use_proxy=False, user_agent=None)