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