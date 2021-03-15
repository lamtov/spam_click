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
import random
from selenium.webdriver import ActionChains
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
NEW_PAGE_LOAD_PAUSE_TIME=1
AFTER_RANDOM_CLICK_ANDSCROLL_PAUSE_TIME=2
BUTTON_CLICK_PAUSE_TIME=1
SCROLL_PAUSE_TIME = 0.01




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
    chrome_options.add_argument("--disable-notifications")
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


    def spam_click_on_gesty(self):
        pass
        # current = self.browser.window_handles[0]
        # try:
        #     divTop = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
        #         (By.XPATH, '''//body''')))
        #     divTop.click()
        #
        #     WebDriverWait(self.browser, 5).until(ec.number_of_windows_to_be(2))
        #     time.sleep(0.1)
        #     self.browser.switch_to.window(current)
        # except:
        #     pass
        # try:
        #
        #     divTop = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
        #         (By.XPATH, '''//div[@class='skip-top-bar']''')))
        #     divTop.click()
        #     WebDriverWait(self.browser, 5).until(ec.number_of_windows_to_be(2))
        #     self.browser.switch_to.window(current)
        # except:
        #     pass
        #
        # try:
        #
        #     divTop = WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(
        #         (By.XPATH, '''//div[@class='information-container']''')))
        #     divTop.click()
        #     WebDriverWait(self.browser, 5).until(ec.number_of_windows_to_be(2))
        #     self.browser.switch_to.window(current)
        # except:
        #     pass

    def spam_click_and_scroll(self):
        try:
            try:
                # RANDOM CLICK BUTTON
                if len(self.browser.find_elements_by_tag_name("button"))>0:
                    count_click=0
                    for button in reversed(self.browser.find_elements_by_tag_name("button")):
                        try:
                            button.click()
                            time.sleep(BUTTON_CLICK_PAUSE_TIME)
                            count_click=count_click+1
                            print(count_click)
                            if count_click>=3:
                                break
                        except :
                            pass

                # RANDOM CLICK LINK
                if len(self.browser.find_elements_by_partial_link_text('')) > 0:
                    links = self.browser.find_elements_by_partial_link_text('')
                    for i in range(0,3):
                        print(i)
                        l = links[random.randint(0, len(links) - 1)]
                        l.click()
                        time.sleep(BUTTON_CLICK_PAUSE_TIME)
            except Exception as e:
                print(e)
                self.status = str('SPAM_FAILED')
            try:
                # RANDOM SCROLL
                last_height = self.browser.execute_script("return document.body.scrollHeight")
                rd = random.randint(10, 100)
                for i in range(0, rd):
                    self.browser.execute_script("window.scrollTo(0," + str(last_height * i / 100) + ");")
                    time.sleep(SCROLL_PAUSE_TIME)
            except Exception as e:
                print(e)
                self.status = str('SPAM_FAILED')

        except Exception as e:
            self.browser.quit()
            print(e)
            self.status = str('SPAM_FAILED')

    def spam(self):
        try:
            self.browser.get(self.link_spam)

            self.status = 'OK'

            time.sleep(NEW_PAGE_LOAD_PAUSE_TIME)

            self.spam_click_on_gesty()

            btnNextPage = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
                (By.XPATH, '''//span[@id='skip_button']''')))
            current = self.browser.window_handles[0]
            btnNextPage.click()
            WebDriverWait(self.browser, 20).until(ec.number_of_windows_to_be(2))

            newWindow = [window for window in self.browser.window_handles if window != current][0]
            windows = self.browser.window_handles
            print("opened windows length: ", len(windows))
            self.browser.switch_to.window(newWindow)
            time.sleep(1)
            wait_for_page_load(self.browser,10)
            newPage = WebDriverWait(self.browser, 3).until(ec.visibility_of_element_located(
                (By.XPATH, '''//body''')))
            time.sleep(NEW_PAGE_LOAD_PAUSE_TIME)
            self.spam_click_and_scroll()
            time.sleep(AFTER_RANDOM_CLICK_ANDSCROLL_PAUSE_TIME)
            # time.sleep(100)
            self.browser.quit()



        except Exception as e:
            self.browser.quit()
            print(e)
            self.status = str('SPAM_FAILED')



import os.path

if __name__ == "__main__":
    link_spam = "http://gestyy.com/et51fF"
    # proxy='41.238.115.218:8080'
    # link_spam ="https://coinmarketcap.com/currencies/kava/"
    # proxy="178.128.65.181:3128"
    proxy='0.0.0.0:0'

    t = Bot(proxy,link_spam)
    t.spam()

