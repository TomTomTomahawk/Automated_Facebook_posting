# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 00:47:39 2019

@author: User
"""

import numpy as np
import random

list_of_options=np.loadtxt('/Users/User/Desktop/Vegan pack/vegan meme/piclinks.txt',dtype='str')

rank=random.randint(0,len(list_of_options)-1)

link=list_of_options[rank]

from selenium import webdriver

from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.firefox.options import Options
options = Options()
options.set_preference("dom.webnotifications.enabled", False)
#browser = webdriver.Firefox(firefox_options=options)
"""
_browser_profile = webdriver.FirefoxProfile()
_browser_profile.set_preference("dom.webnotifications.enabled", False)
"""

#driver=webdriver.Firefox(executable_path=r'\Users\User\Desktop\fonctions_python\geckodriver.exe',firefox_options=options)

driver=webdriver.Firefox(executable_path=r'C:\Users\User\Desktop\fonctions_python\geckodriver.exe',log_path=r'C:\Users\User\Desktop\fonctions_python\geckodriver.log',firefox_options=options)


driver.get('http://facebook.com')
emailelement=driver.find_element(By.XPATH,'.//*[@id="email"]')
emailelement.send_keys('type your Facebook email address here')

passelement=driver.find_element(By.XPATH,'.//*[@id="pass"]')
passelement.send_keys('type your Facebook password here')

elem=driver.find_element(By.XPATH,'.//*[@id="loginbutton"]')
elem.click() 

time.sleep(2)

statuselement=driver.find_element(By.XPATH,"//*[@name='xhpc_message']")

statuselement.send_keys(link)
statuselement.send_keys(' ')
time.sleep(5)

#statuselement.send_keys(Keys.CONTROL+'a')
#statuselement.send_keys(Keys.BACKSPACE)

#driver.execute_script("window.scrollTo(0,150)")

#time.sleep(2)
buttons=driver.find_elements_by_tag_name('button')

for button in buttons:
    if button.text=='Share':
        button.click()

time.sleep(10)

driver.quit()

input('Press Enter to finish')














"""

like=driver.find_elements_by_css_selector(".UFILikeLink._4x9-._4x9_._48-k")
like.click()


statuselement=driver.find_element(By.XPATH,"//*[@name='xhpc_message']")


"""
"""
like_buttons = driver.find_elements_by_xpath('//a[contains(@class,"likeButton")]')
for like in like_buttons:
    print(like)

postBtn = driver.find_element(By.xpath("//button[contains(.,'Post')]"))
postBtn.click()

share = driver.find_element_by_xpath
share.click()
"""
#search=driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
#search.send_keys('vegan outreach')
#driver.find_element_by_css_selector("button[aria-label='Search']").click()

#time.sleep(3)


"""
page=driver.find_element(By.NAME,'Vegan Outreach')
page.click()

page=driver.find_element_by_partial_link_text('veganoutreach')
page.click()


#“//div[contains(@class,’_586i’)]”


driver.find_element_by_css_selector("div[aria-label='Search Facebook']").send_keys("We are Ankara")
driver.find_element_by_css_selector("button[aria-label='Search']").click()
#search.submit()
#driver.find_element(By.XPATH,".//div[contains(@class,'_586i')]").send_keys("vegan outreach")

__enter__'
'execute'
searchelement=driver.find_element_by_css_selector("button[aria-label='Search']")
searchelement.click()
#driver.find_element_by_css_selector("button[aria-label='Search']").click()
searchelement.send_keys('vegan outreach')

elem=driver.find_element(By.XPATH,'.//*[@id="facebar_search_button"]')
elem.click()


searchelement=driver.find_element(By.XPATH,'.//*[@name="search"]')



statuselement=driver.find_element(By.XPATH,"//*[@name='xhpc_message']")

time.sleep(5)

statuselement.send_keys('Simon Vogel is my best friend.')

time.sleep(5)

buttons=driver.find_elements_by_tag_name('button')

time.sleep(5)

for button in buttons:
    if button.text=='Share':
        button.click()

"""