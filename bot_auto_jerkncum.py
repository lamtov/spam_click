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
TIME_BETWEEN_CLICK = 0.2




def get_random(list_string):
    return list_string[random.randint(0,len(list_string)-1)]
def click_and_sleep(btn):
    try:
        btn.click()
        time.sleep(TIME_BETWEEN_CLICK)
    except:
        pass

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
        if random.random() > 0.5:
            user_agent = ua.chrome
        else:
            user_agent = ua.firefox

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


    # def spam_click_on_gesty(self):
    #     pass
    #     # current = self.browser.window_handles[0]
    #     # try:
    #     #     divTop = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
    #     #         (By.XPATH, '''//body''')))
    #     #     divTop.click()
    #     #
    #     #     WebDriverWait(self.browser, 5).until(ec.number_of_windows_to_be(2))
    #     #     time.sleep(0.1)
    #     #     self.browser.switch_to.window(current)
    #     # except:
    #     #     pass
    #     # try:
    #     #
    #     #     divTop = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
    #     #         (By.XPATH, '''//div[@class='skip-top-bar']''')))
    #     #     divTop.click()
    #     #     WebDriverWait(self.browser, 5).until(ec.number_of_windows_to_be(2))
    #     #     self.browser.switch_to.window(current)
    #     # except:
    #     #     pass
    #     #
    #     # try:
    #     #
    #     #     divTop = WebDriverWait(self.browser, 5).until(ec.visibility_of_element_located(
    #     #         (By.XPATH, '''//div[@class='information-container']''')))
    #     #     divTop.click()
    #     #     WebDriverWait(self.browser, 5).until(ec.number_of_windows_to_be(2))
    #     #     self.browser.switch_to.window(current)
    #     # except:
    #     #     pass
    #
    # def spam_click_and_scroll(self):
    #     try:
    #         try:
    #             # RANDOM CLICK BUTTON
    #             if len(self.browser.find_elements_by_tag_name("button"))>0:
    #                 count_click=0
    #                 for button in reversed(self.browser.find_elements_by_tag_name("button")):
    #                     try:
    #                         button.click()
    #                         time.sleep(BUTTON_CLICK_PAUSE_TIME)
    #                         count_click=count_click+1
    #                         print(count_click)
    #                         if count_click>=3:
    #                             break
    #                     except :
    #                         pass
    #
    #             # RANDOM CLICK LINK
    #             if len(self.browser.find_elements_by_partial_link_text('')) > 0:
    #                 links = self.browser.find_elements_by_partial_link_text('')
    #                 for i in range(0,3):
    #                     print(i)
    #                     l = links[random.randint(0, len(links) - 1)]
    #                     l.click()
    #                     time.sleep(BUTTON_CLICK_PAUSE_TIME)
    #         except Exception as e:
    #             print(e)
    #             self.status = str('SPAM_FAILED')
    #         try:
    #             # RANDOM SCROLL
    #             last_height = self.browser.execute_script("return document.body.scrollHeight")
    #             rd = random.randint(10, 100)
    #             for i in range(0, rd):
    #                 self.browser.execute_script("window.scrollTo(0," + str(last_height * i / 100) + ");")
    #                 time.sleep(SCROLL_PAUSE_TIME)
    #         except Exception as e:
    #             print(e)
    #             self.status = str('SPAM_FAILED')
    #
    #     except Exception as e:
    #         self.browser.quit()
    #         print(e)
    #         self.status = str('SPAM_FAILED')

    def spam(self):
        try:
            self.browser.get(self.link_spam)

            self.status = 'OK'

            time.sleep(NEW_PAGE_LOAD_PAUSE_TIME)

            # STA

            btnStartPage = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
                (By.XPATH, '''//button[contains(text(),'Start')]''')))
            click_and_sleep(btnStartPage)


            btnContinuePage = WebDriverWait(self.browser, 15).until(ec.visibility_of_element_located(
                (By.XPATH, '''//button[contains(text(),'Continue')]''')))
            click_and_sleep(btnContinuePage)


            # Which type of girl do you actually prefer?
            list_type0=["Asian", "Ebony",  "Caucasian", "Latina",  "Love All!"]
            li_0 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q0 current"]''')))
            rd_asw0=get_random(list_type0)
            btn_as0 = WebDriverWait(li_0, 15).until(ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw0))))
            click_and_sleep(btn_as0)

            # What about her hair color?
            list_type1 = ["Blonde", "Redhead", "Brunette", "Whatever!"]
            li_1 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q1 current"]''')))
            rd_asw1 = get_random(list_type1)
            btn_as1 = WebDriverWait(li_1, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw1))))
            click_and_sleep(btn_as1)

            # How would you prefer her tits?
            list_type2 = ["Small", "Medium", "Big", "Doesn’t matter"]
            li_2= WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q2 current"]''')))
            rd_asw2= get_random(list_type2)
            btn_as2 = WebDriverWait(li_2, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw2))))
            click_and_sleep(btn_as2)

            # How do you prefer her pussy?
            list_type3 = ["Shaved", "Trimmed", "Hairy"]
            li_3 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q3 current"]''')))
            rd_asw3 = get_random(list_type3)
            btn_as3 = WebDriverWait(li_3, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw3))))
            click_and_sleep(btn_as3)

            # What are you looking for?
            list_type4 = ["Sneak and Jerk Off", "Be part of the cam community"]
            li_4 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q4 current"]''')))
            rd_asw4 = get_random(list_type4)
            btn_as4 = WebDriverWait(li_4, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw4))))
            click_and_sleep(btn_as4)

            btn_CONTINUE_1 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
            click_and_sleep(btn_CONTINUE_1)



            # Are you into hardcore?
            list_type5 = ["Yes","No"]
            li_5 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q5 'current' current "]''')))
            rd_asw5 = "Yes"
            btn_as5 = WebDriverWait(li_5, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw5))))
            click_and_sleep(btn_as5)

            # Would you like her to use accessories?
            list_type6 = ["Yes","No"]
            li_6 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q6 'current' current "]''')))
            rd_asw6 = "No"
            btn_as6 = WebDriverWait(li_6, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw6))))
            click_and_sleep(btn_as6)

            # What's your favorite hole?
            list_type7 = ["Pussy","Ass","Mouth"]
            li_7 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q7 'current' current "]''')))
            rd_asw7 = get_random(list_type7)
            btn_as7= WebDriverWait(li_7, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw7))))
            click_and_sleep(btn_as7)

            # What should she put in it?
            list_type8 = ["Vibrator","Dildo","Vegetable"]
            li_8 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q8 'current' current "]''')))
            rd_asw8 = get_random(list_type8)
            btn_as8 = WebDriverWait(li_8, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw8))))
            click_and_sleep(btn_as8)

            # What’s your favorite age group?
            list_type9 = ["Teen (18-34)", "Milf (35-50)","Mature (50+)"]
            li_9 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, '''//li[@class="question q9 'current' current "]''')))
            rd_asw9 = get_random(list_type9)
            btn_as9 = WebDriverWait(li_9, 15).until(
                ec.visibility_of_element_located((By.XPATH, ".//button[contains(text(), '{0}')]".format(rd_asw9))))
            click_and_sleep(btn_as9)

            btn_ANALYZE_1 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Analyze')]")))
            click_and_sleep(btn_ANALYZE_1)

            btn_CONTINUE_2 = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Continue')]")))
            click_and_sleep(btn_CONTINUE_2)

            btn_I_AGREE = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, "//button[contains(text(),'I Agree')]")))
            click_and_sleep(btn_I_AGREE)

            btn_CREATE_ACCOUNT = WebDriverWait(self.browser, 15).until(
                ec.visibility_of_element_located((By.XPATH, "//a[contains(text(),'Create Account')]")))
            click_and_sleep(btn_CREATE_ACCOUNT)

            # current = self.browser.window_handles[0]
            # WebDriverWait(self.browser, 20).until(ec.number_of_windows_to_be(2))

            # newWindow = [window for window in self.browser.window_handles if window != current][0]
            windows = self.browser.window_handles
            print("opened windows length: ", len(windows))
            # self.browser.switch_to.window(newWindow)
            time.sleep(1)
            wait_for_page_load(self.browser,10)
            newPage = WebDriverWait(self.browser, 3).until(ec.visibility_of_element_located(
                (By.XPATH, '''//body''')))
            time.sleep(NEW_PAGE_LOAD_PAUSE_TIME)
            # self.spam_click_and_scroll()
            # time.sleep(AFTER_RANDOM_CLICK_ANDSCROLL_PAUSE_TIME)
            # time.sleep(100)
            # self.browser.quit()



        except Exception as e:
            self.browser.quit()
            print(e)
            self.status = str('SPAM_FAILED')



import os.path

if __name__ == "__main__":
    link_spam = "https://v2.jerkncum.com/?transaction_id=10243326461b76e10ea6f9881b82ea&aff_id=171541&aff_sub=&aff_sub2=&source=&url=1&bg=4"
    # proxy='41.238.115.218:8080'
    # link_spam ="https://coinmarketcap.com/currencies/kava/"
    # proxy="178.128.65.181:3128"
    proxy='0.0.0.0:0'

    t = Bot(proxy,link_spam)
    t.spam()

