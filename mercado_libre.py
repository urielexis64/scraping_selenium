from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
)

driver = webdriver.Chrome('./chromedriver.exe', options=opts)

driver.get('https://listado.mercadolibre.com.mx/guitarra')
while True:
    products_link = driver.find_elements(By.XPATH, '//div[@class="ui-search-result__image"]/a[1]')
    page_links = []
    for tag_a in products_link:
        page_links.append(tag_a.get_attribute('href'))

    for link in page_links:
        try:
            driver.get(link)
            title = driver.find_element_by_xpath('//h1[@class="ui-pdp-title"]').text
            price = driver.find_element_by_xpath(
                '//div[@class="ui-pdp-price mt-16 ui-pdp-price--size-large"]//span[@class="price-tag-fraction"]').text
            print(title, price, sep=' | ')
            driver.back()
        except Exception as e:
            print(e)
            driver.back()
    try:
        nextButton = driver.find_element_by_xpath('//span[text()="Siguiente"]')
        nextButton.click()
    except:
        break
