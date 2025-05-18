# Инициализация Selenium
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Парсинг данных с Best Buy
driver.get('https://www.bestbuy.com/site/laptops/pcmcat247400050000.c?id=pcmcat247400050000')
time.sleep(3)  # Подождать загрузки страницы

laptops = driver.find_elements(By.CLASS_NAME, 'sku-item')

data_laptops = []
for laptop in laptops:
    try:
        title = laptop.find_element(By.CSS_SELECTOR, 'h4').text
        price = laptop.find_element(By.CSS_SELECTOR, '.priceView-customer-price').text
        data_laptops.append((title, price))
    except:
        continue

driver.quit()