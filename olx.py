import random
from time import sleep
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.olx.com.ec/autos_c378')

loadMoreButton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')

for _ in range(3):
    try:
        loadMoreButton.click()
        sleep(random.uniform(6, 8))
        loadMoreButton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        break

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')
i = 0
for auto in autos:
    i+=1
    print(i)
    price = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    details = auto.find_element_by_xpath('.//span[@data-aut-id="itemDetails"]').text
    title = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(price, details, title)