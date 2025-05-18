# Инициализация Selenium
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Парсинг данных с Wikipedia
driver.get('https://www.wikipedia.org/')
time.sleep(3)  # Подождать загрузки страницы

technology_link = driver.find_element(By.LINK_TEXT, 'Technology')
technology_link.click()
time.sleep(3)

articles = driver.find_elements(By.CSS_SELECTOR, '.mw-category-group a')

data_articles = []
for article in articles:
    title = article.text
    link = article.get_attribute('href')
    data_articles.append((title, link))

driver.quit()