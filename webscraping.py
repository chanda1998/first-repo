from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyautogui
import time

# xpath of from inputbox //*[@id="origin"]/span/input
# xpath of to inputbox  //*[@id="destination"]/span/input
# xpath of find train button
#//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div/div/div[1]/div/app-jp-input/div[3]/form/div[7]/button
# xpath of category //*[@id="journeyClass"]/div/label
# for sakri --> SAKRI JN - SKI
# for new delhi --> NEW DELHI - NDLS

#linking the drivers

driver = webdriver.Chrome("""D:/CHANDAN/pythonpracrtice/chromedriver_win32/chromedriver.exe""")
driver.get("https://www.irctc.co.in/nget/train-search")

assert "IRCTC" in driver.title


pyautogui.hotkey('win', 'up')
#loging in account

driver.find_element_by_xpath('//*[@id="loginText"]').click()
driver.find_element_by_xpath('//*[@id="userId"]').send_keys('ch78277')
driver.find_element_by_xpath('//*[@id="pwd"]').send_keys('Ch24111998')


time.sleep(15)

#from element filling

from_element = driver.find_element_by_xpath('//*[@id="origin"]/span/input')
from_element.clear()
from_element.send_keys('NEW DELHI - NDLS')


#to element filling

to_element = driver.find_element_by_xpath('//*[@id="destination"]/span/input')
to_element.clear()
to_element.send_keys('SAKRI JN - SKI')


#selecting the category
select = driver.find_element_by_xpath('//*[@id="journeyClass"]/div/label')
select.click()
driver.find_element_by_xpath('//*[@id="journeyClass"]/div/div[4]/div/ul/li[10]').click()





###clicking the find train

driver.find_element_by_xpath('''//*[@id="divMain"]/div/app-main-page/div[2]/div/div[1]/div
                        /div/div[1]/div/app-jp-input/div[3]/form/div[7]/button''').click()













