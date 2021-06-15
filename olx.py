from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome('chromedriver.exe')

driver.get('https://www.olx.com.ec/autos_c378')

for _ in range(3):
    try:
        loadMoreButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//button[@data-aut-id="btnLoadMore"]'))
        )
        loadMoreButton.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, '//li[@data-aut-id="itemBox"]//span[@data-aut-id="itemTitle"]'))
        )
    except Exception as e:
        print(e)
        break

autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')

for auto in autos:
    price = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    details = auto.find_element_by_xpath('.//span[@data-aut-id="itemDetails"]').text
    title = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print(price, details, title, sep=' | ')
