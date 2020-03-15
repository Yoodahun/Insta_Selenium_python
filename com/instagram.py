from selenium import webdriver
from com import login
import time


def log():
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input'
                                  ).send_keys(login.username)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input'
                                  ).send_keys(login.password)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[1]/div/form/div[4]/button'
                                  ).click()

def close_noti():
    browser.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]'
                                  ).click()

def likes():
    browser.get("https://www.instagram.com/explore/tags/xpro3/")
    size = 50 #int(browser.find_element_by_xpath('//*[@id="react-root"]/section/main/header/div[2]/div[1]/div[2]/span/span').text.replace(",", ""))
    print(size)
    browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]'
                                  ).click()  # click the post
    # browser.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.zZYga > div > article > div.eo2As > section.ltpMr.Slqrh > span.FY9nT.fr66n > button')  # click like


    for i in range(size):
        time.sleep(2)
        try:
            browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button'
                                      ).click() # click like
            if i == 0:
                browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a'
                                              ).click()  # move next post
            else:
                browser.find_element_by_xpath('/html/body/div[4]/div[1]/div/div/a[2]'
                                              ).click()  # move next post
        except:
            browser.find_element_by_xpath("/html/body/div[4]/div[2]/div/article/div[2]/section[1]/span[1]/button/svg[@aria-label='좋아요 취소']")
        time.sleep(2)




browser = webdriver.Chrome(
    executable_path='../Driver/chromedriver'
)
browser.get("https://www.instagram.com/")

time.sleep(5)
log()
time.sleep(5)
close_noti()
time.sleep(5)
likes()
browser.close()