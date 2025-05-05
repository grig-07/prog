# Лабораторная работа №15
1. Спроектируйте БД с использованием crow’s foot notation.
2. Реализуйте парсер для сбора данных с веб-страницы.
3. С помощью DB API cоздайте таблицы БД и заполните их данными, полученными с помощью парсера.
4. Напишите запросы для выборки данных из БД.
5. Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
- Ссылки на используемые материалы
## Реализация парсера для сбора данных с веб-страницы
``` py
import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Список_созвездий_по_площади"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Найдите таблицу с данными о созвездиях
table = soup.find('table', {'class': 'wikitable'})

# Извлеките данные из таблицы
data = []
for row in table.find_all('tr')[1:]:
    cols = row.find_all('td')
    if cols:
        name = cols[0].text.strip()
        area = cols[1].text.strip()
        number_of_stars = cols[2].text.strip()
        mythology = cols[3].text.strip() if len(cols) > 3 else ""
        data.append({
            'name': name,
            'area': area,
            'number_of_stars': number_of_stars,
            'mythology': mythology
        })
```
## Проектирование БД
``` py
import sqlite3

# Подключение к базе данных (или создание, если не существует)
conn = sqlite3.connect('constellations.db')
cursor = conn.cursor()

# Создание таблицы
cursor.execute('''
    CREATE TABLE IF NOT EXISTS constellations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        area TEXT,
        number_of_stars TEXT,
        mythology TEXT
    )
''')

# Вставка данных
for entry in data:
    cursor.execute('''
        INSERT INTO constellations (name, area, number_of_stars, mythology)
        VALUES (?, ?, ?, ?)
    ''', (entry['name'], entry['area'], entry['number_of_stars'], entry['mythology']))

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()
## Парсинг данных
```
## Написание запросов для выборки данных из БД
``` py
SELECT * FROM constellations ORDER BY area DESC;
```
``` py
SELECT * FROM constellations ORDER BY area DESC LIMIT 1;
```
``` py
SELECT * FROM constellations WHERE number_of_stars > 100;
```
