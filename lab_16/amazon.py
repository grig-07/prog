from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlite3
from pypika import Query, Table, Column, functions
import time

# Инициализация Selenium
driver = webdriver.Chrome(executable_path='path_to_chromedriver')

# Парсинг данных с Amazon
driver.get('https://www.amazon.com/books')
time.sleep(3)  # Подождать загрузки страницы

books = driver.find_elements(By.CLASS_NAME, 's-result-item')

data_books = []
for book in books:
    try:
        title = book.find_element(By.CSS_SELECTOR, 'h2').text
        price = book.find_element(By.CSS_SELECTOR, '.a-price-whole').text
        data_books.append((title, price))
    except:
        continue

driver.quit()