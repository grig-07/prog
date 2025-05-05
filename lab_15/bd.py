import sqlite3

# Подключение к базе данных
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