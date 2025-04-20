# Лабораторная работа №14
1. Спроектируйте БД с использованием crow’s foot notation.
2. Создайте таблицы БД и заполните данными. Для генерации данных можно использовать сервис https://www.mockaroo.com/.
3. Напишите несколько запросов для выборки данных из всех таблиц.
4. Оформите отчёт в README.md. Отчёт должен содержать:
- Условия задач
- Описание проделанной работы
- Скриншоты результатов
# База данных для учета книг в книжном магазине

## Описание

База данных предназначена для учета книг, авторов и заказов в книжном магазине. Она включает в себя следующие таблицы:

- **Authors**: Информация об авторах книг.
- **Books**: Информация о книгах в магазине.
- **Customers**: Информация о клиентах.
- **Orders**: Информация о заказах книг.

## Создание таблиц БД
``` sql
-- Таблица Авторы
CREATE TABLE Authors (
    author_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    biography TEXT
);

-- Таблица Книги
CREATE TABLE Books (
    book_id INT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    author_id INT,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- Таблица Клиенты
CREATE TABLE Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    customer_address VARCHAR(200)
);

-- Таблица Заказы
CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    order_date DATE NOT NULL,
    delivery_status VARCHAR(50),
    book_id INT,
    customer_id INT,
    FOREIGN KEY (book_id) REFERENCES Books(book_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);
```
## Заполнение таблиц данными
- Для генерации данных воспользовался сервисом Mockaroo. Ниже приведены примеры данных для каждой таблицы.
``` sql
  -- Данные для таблицы Авторы
INSERT INTO Authors (author_id, name, biography) VALUES
(1, 'Джоан Роулинг', 'Британская писательница, известная по серии книг о Гарри Поттере.'),
(2, 'Джордж Оруэлл', 'Английский писатель, автор известных романов "1984" и "Скотный двор".');

-- Данные для таблицы Книги
INSERT INTO Books (book_id, title, price, author_id) VALUES
(1, 'Гарри Поттер и философский камень', 250.00, 1),
(2, '1984', 150.00, 2),
(3, 'Гарри Поттер и Тайная комната', 300.00, 1);

-- Данные для таблицы Клиенты
INSERT INTO Customers (customer_id, customer_name, customer_address) VALUES
(1, 'Иван Иванов', 'Москва, ул. Ленина, 1'),
(2, 'Петр Петров', 'Санкт-Петербург, ул. Невский, 2');

-- Данные для таблицы Заказы
INSERT INTO Orders (order_id, order_date, delivery_status, book_id, customer_id) VALUES
(1, '2023-10-01', 'Доставлено', 1, 1),
(2, '2023-10-05', 'В процессе', 2, 2),
(3, '2023-10-10', 'Доставлено', 3, 1);
```
## Таблицы

### Authors

| Поле        | Тип          | Описание                  |
|-------------|--------------|---------------------------|
| author_id   | INT          | Уникальный идентификатор автора |
| name        | VARCHAR(100) | Имя автора                |
| biography   | TEXT         | Биография автора          |

### Books

| Поле      | Тип          | Описание                          |
|-----------|--------------|-----------------------------------|
| book_id   | INT          | Уникальный идентификатор книги    |
| title     | VARCHAR(200) | Название книги                    |
| price     | DECIMAL(10,2)| Цена книги                        |
| author_id | INT          | Идентификатор автора книги        |

### Customers

| Поле            | Тип          | Описание                          |
|-----------------|--------------|-----------------------------------|
| customer_id     | INT          | Уникальный идентификатор клиента |
| customer_name   | VARCHAR(100) | Имя клиента                       |
| customer_address | VARCHAR(200) | Адрес клиента                     |

### Orders

| Поле          | Тип          | Описание                          |
|---------------|--------------|-----------------------------------|
| order_id      | INT          | Уникальный идентификатор заказа   |
| order_date    | DATE         | Дата заказа                       |
| delivery_status | VARCHAR(50) | Статус доставки                   |
| book_id       | INT          | Идентификатор книги               |
| customer_id   | INT          | Идентификатор клиента             |

## Примеры запросов

1. **Выбор всех книг с информацией об авторах:**

```sql
SELECT Books.title, Books.price, Authors.name
FROM Books
JOIN Authors ON Books.author_id = Authors.author_id;
```
2. Выбор всех заказов с информацией о книгах и клиентах:
``` sql
SELECT Orders.order_id, Orders.order_date, Orders.delivery_status, Books.title, Customers.customer_name
FROM Orders
JOIN Books ON Orders.book_id = Books.book_id
JOIN Customers ON Orders.customer_id = Customers.customer_id;
```
3. Выбор всех авторов и количества написанных ими книг:
``` sql
SELECT Authors.name, COUNT(Books.book_id) AS book_count
FROM Authors
LEFT JOIN Books ON Authors.author_id = Books.author_id
GROUP BY Authors.name;
```
4. Выбор всех клиентов, которые сделали заказы:
``` sql
SELECT DISTINCT Customers.customer_id, Customers.customer_name
FROM Customers
JOIN Orders ON Customers.customer_id = Orders.customer_id;
```
