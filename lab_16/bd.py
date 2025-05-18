# Подключение к базе данных
conn = sqlite3.connect('scraped_data.db')
cursor = conn.cursor()

# Создание таблиц
cursor.execute('''
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        price TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        link TEXT,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories (id)
    )
''')

# Вставка данных в таблицы
# Вставка категорий
cursor.execute('INSERT INTO categories (name) VALUES (?)', ('Books',))
cursor.execute('INSERT INTO categories (name) VALUES (?)', ('Laptops',))
cursor.execute('INSERT INTO categories (name) VALUES (?)', ('Technology',))
conn.commit()

# Вставка данных о книгах
for book in data_books:
    cursor.execute('INSERT INTO products (title, price, category_id) VALUES (?, ?, ?)', (book[0], book[1], 1))

# Вставка данных о ноутбуках
for laptop in data_laptops:
    cursor.execute('INSERT INTO products (title, price, category_id) VALUES (?, ?, ?)', (laptop[0], laptop[1], 2))

# Вставка данных об статьях
for article in data_articles:
    cursor.execute('INSERT INTO articles (title, link, category_id) VALUES (?, ?, ?)', (article[0], article[1], 3))

conn.commit()