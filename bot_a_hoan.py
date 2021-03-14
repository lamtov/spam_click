from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import io, json,os
import time
soup = BeautifulSoup("")
import platform
from fake_useragent import UserAgent

# def init_driver_window():
#     chrome_options = Options()
#
#     # chrome_options.add_argument("ignore-certificate-errors")
#     # chrome_options.add_argument('--headless')
#     # chrome_options.add_argument('--no-sandbox')
#     # chrome_options.add_argument('--disable-dev-shm-usage')
#     # chrome_options.add_argument("--incognito")
#     chrome_options.add_argument("--disable-extensions")
#     chrome_options.add_argument("user-data-dir=selenium")
#     chrome_options.add_argument("--window-size=1920x1080")
#     driver = webdriver.Chrome(chrome_options=chrome_options)
#     return driver


from selenium.webdriver.support.expected_conditions import staleness_of

def wait_for_page_load(browser, timeout=30):
    old_page = browser.find_element_by_tag_name('html')
    yield
    WebDriverWait(browser, timeout).until(
        staleness_of(old_page)
    )
def init_driver(_proxy, _change_agent):
    chrome_options = Options()
    if _proxy is not None and _proxy != "0.0.0.0:0":
        PROXY = _proxy.replace('\n', '')
        print(PROXY)
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
    if _change_agent == True:
        ua = UserAgent()
        user_agent = ua.random
        print(user_agent)
        chrome_options.add_argument(f'user-agent={user_agent}')
    chrome_options.add_argument("ignore-certificate-errors")
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-extensions")
    # chrome_options.add_argument("user-data-dir=selenium")
    chrome_options.add_argument("--window-size=1920x1080")
    if 'ubuntu' in platform.platform().lower() or 'linux' in platform.platform().lower():
        print('using ubuntu or linux')
        driver = webdriver.Chrome(chrome_options=chrome_options)
    else:
        cur_dir = os.getcwd()
        driver = webdriver.Chrome(chrome_options=chrome_options,
                                  executable_path=cur_dir+ "/window_driver"+"/chromedriver.exe")
        print(driver.execute_script("return navigator.userAgent;"))
    return driver




class Bot():
    def __init__(self,_proxy, link_spam,):
        try:
            self.browser = init_driver(_proxy, True)
            self.status = 'init'
            self.link_spam=link_spam


        except Exception as e:
            print(e)
            self.status = str(traceback.format_exc())

    def spam(self):
        try:
            self.browser.get(self.link_spam)

            self.status = 'OK'
            # time.sleep(6)
            btnNextPage = WebDriverWait(self.browser, 10).until(ec.visibility_of_element_located(
                (By.XPATH, '''//span[@id='skip_button']''')))
            current = self.browser.window_handles[0]
            btnNextPage.click()
            WebDriverWait(self.browser, 20).until(ec.number_of_windows_to_be(2))

            newWindow = [window for window in self.browser.window_handles if window != current][0]
            windows = self.browser.window_handles
            print("opened windows length: ", len(windows))
            self.browser.switch_to.window(newWindow)
            # time.sleep(4)
            wait_for_page_load(self.browser,10)
            newPage = WebDriverWait(self.browser, 3).until(ec.visibility_of_element_located(
                (By.XPATH, '''//body''')))
            time.sleep(1)
            self.browser.quit()



        except Exception as e:
            self.browser.quit()
            print(e)
            self.status = str('SPAM_FAILED')



import os.path

if __name__ == "__main__":
    link_spam = "http://gestyy.com/et51fF"
    # proxy='41.238.115.218:8080'
    # link_spam ="https://translate.google.com/"
    # proxy="178.128.65.181:3128"
    proxy='0.0.0.0:0'

    t = Bot(proxy,link_spam)
    t.spam()

