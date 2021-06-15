from time import sleep
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

scrollingScript = """document.getElementsByClassName('section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc')[0].scroll(0, 100000)"""

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
)
driver = webdriver.Chrome('chromedriver.exe', options=opts)
driver.get("https://www.google.com/maps/place/Incl%C3%A1n+Brutal+Bar/@40.4158233,-3.7015035,16.02z/data=!4m14!1m6!3m5!1s0x86bcd7a645c2718d:0x3e36289272bc1af9!2sHamburguesas+Flor!8m2!3d24.7731918!4d-107.3728335!3m6!1s0xd42288066c3fa3f:0x4c115f1b554bf55a!8m2!3d40.4151108!4d-3.7019311!9m1!1b1")

sleep(random.uniform(4, 6))

SCROLLS = 0
while SCROLLS != 3:
    driver.execute_script(scrollingScript)
    sleep(random.uniform(3, 5))
    SCROLLS += 1

reviews = driver.find_elements(By.XPATH, '//div[@class="ODSEW-ShBeI NIyLF-haAclf gm2-body-2"]')

for review in reviews:
    user_link = review.find_element_by_xpath('.//div[@class="ODSEW-ShBeI-tXxcle ODSEW-ShBeI-tXxcle-SfQLQb-menu"]')
    try:
        user_link.click()
        driver.switch_to.window(driver.window_handles[1])
        opinionsButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="s4ghve-AznF2e-ZMv3u-AznF2e NIyLF-haAclf s4ghve-AznF2e-ZMv3u-AznF2e-selected"]')))
        opinionsButton.click()

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[@class="section-layout section-scrollbox cYB2Ge-oHo7ed cYB2Ge-ti6hGc"]')))

        USER_SCROLLS = 0
        while USER_SCROLLS != 3:
            driver.execute_script(scrollingScript)
            sleep(random.uniform(1, 3))
            USER_SCROLLS += 1

        user_reviews = driver.find_elements_by_xpath('//div[@class="ODSEW-ShBeI NIyLF-haAclf gm2-body-2 ODSEW-ShBeI-d6wfac ODSEW-ShBeI-SfQLQb-QFlW2 ODSEW-ShBeI-De8GHd-KE6vqe-purZT"]')

        for user_review in user_reviews:
            title = user_review.find_element_by_xpath('.//div[@class="ODSEW-ShBeI-title ODSEW-ShBeI-title-juPPCf-SfQLQb-ShBeI-text"]/span').text
            content = user_review.find_element_by_xpath('.//span[@class="ODSEW-ShBeI-text"]').text
            rating = len(user_review.find_elements_by_xpath('.//img[@src="//maps.gstatic.com/consumer/images/icons/2x/ic_star_rate_14.png"]'))
            print(f'Title: {title}')
            print(f'Content: {content}')
            print(f'Rating: {rating} stars')

        driver.close()
        sleep(random.uniform(2, 3))
        driver.switch_to.window(driver.window_handles[0])
    except Exception as e:
        print(e)
        driver.switch_to.window(driver.window_handles[0])
