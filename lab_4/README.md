# Лабораторная работа №4
# Основные типы и операции Python
## Задание:
1. Скачайте архив и распакуйте его в свой репозиторий. В нём 11 заданий, которые вам нужно выполнить.
2. Оформите отчёт в README.md. По каждому из заданий - описание задачи, скриншот работы программы.
## Программы:
## (вывод терминала в конце или же должен присутствовать в файлах репризитория)
```py
#ФАЙЛ                                              * 00_distance.py  *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

for s1 in sites:
    distances[s1]={}
    for s2 in sites:
        if s1==s2:
            continue
        x1, y1 = sites[s1]
        x2, y2 =sites[s2]
        dist=((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        distances[s1][s2]=dist

print(distances)

# ФАЙЛ                                                   *  01_circle.py  *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42

# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()
# TODO здесь ваш код
pi=3.1415926
print(round(radius*pi**2,4))
# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
# TODO здесь ваш код
print((point_1[0]**2+point_1[1]**2)**0.5<radius)
# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
# TODO здесь ваш код
print((point_2[0]**2+point_2[1]**2)**0.5<radius)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False

#ФАЙЛ                                                *  02_operations.py  *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Расставьте знаки операций "плюс", "минус", "умножение" и скобки
# между числами "1 2 3 4 5" так, что бы получилось число "25".
#
# Использовать нужно только указанные знаки операций, но не обязательно все перечесленные.
# Порядок чисел нужно сохранить.

# Пример для чисел "1 2 3" и "9"
result = (1 + 2) * 3
print(result)

# TODO написать формулу для 1 2 3 4 5 и вывести значение на консоль
result = 1 * 2 + 3 + 4 * 5
print(result)

#ФАЙЛ                                               *  03_FAVORITE_MOVIES.PY  *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

# TODO здесь ваш код
print(my_favorite_movies[:10])

print(my_favorite_movies[-15:])

print(my_favorite_movies[12:25])

print(my_favorite_movies[-22:-17])

#ФАЙЛ                                                      * 04MY_FAMILY.PY *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['Dad', 178],
    ['Mom', 160],
    ['i',176],
    ['litle sister', 150]
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца -",my_family_height[0][1],"см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
rost = 0
for i in my_family_height:
      rost+=i[1]
print("Общий рост моей семьи -", rost,"см")

#ФАЙЛ                                                              * 05_ZOO.PY *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
# TODO здесь ваш код
zoo.insert(1,"bear")
print(zoo)
# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
# TODO здесь ваш код
for i in birds:
    zoo.append(i)
print(zoo)
# уберите слона
#  и выведите список на консоль
# TODO здесь ваш код
zoo.__delitem__(3)
print(zoo)
# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
# TODO здесь ваш код
for i in zoo:
    if i=="lion":
        print("Лев сидит в клетке №",zoo.index(i)+1)
    elif i=="lark":
        print("Жаворонок сидит в клетке №",zoo.index(i)+1)

#ФАЙЛ                                             * 06_SONG_LIST.PY  *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# распечатайте общее время звучания трех песен: 'Halo', 'Enjoy the Silence' и 'Clean' в формате
#   Три песни звучат ХХХ.XX минут
# Обратите внимание, что делать много вычислений внутри print() - плохой стиль.
# Лучше заранее вычислить необходимое, а затем в print(xxx, yyy, zzz)

# TODO здесь ваш код
summa=0
for i in violator_songs_list:
    if i[0]=='Halo':
        summa+=i[1]
    elif i[0]=='Enjoy the Silence':
        summa+=i[1]
    elif i[0]=='Clean':
        summa+=i[1]
summa = "{:06.2f}".format(summa)
print("Три песни звучат",summa,"минут")

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
songs=violator_songs_dict['Sweetest Perfection']+violator_songs_dict['Policy of Truth']+violator_songs_dict['Blue Dress']
songs="{:03d}".format(int(round(songs)))
print("А другие три песни звучат",songs,"минут")

#ФАЙЛ                                          *  07_SECRET.PY  *
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# Нужно его расшифровать и вывести на консоль в удобочитаемом виде.
# Должна получиться фраза на русском языке, например: как два байта переслать.

# Ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Обратите вниманме:
#   даны номера букв, а не индексы
#   срез не включает последний индекс
#   подробную информацию об обратных срезах см https://clck.ru/MfEMS
#
# Подсказки:
#   В каждом элементе списка защифровано одно слово.
#   Требуется задать конкретные индексы, например secret_message[3][12:23:4]
#   4е и 5е слова нужно получить за 1 срез
#   Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

# TODO вывести расшифрованное сообщение
print(secret_message[0][3:4],secret_message[1][9:13],secret_message[2][5:15:2],secret_message[3][12:6:-1],secret_message[4][20:15:-1])

#ФАЙЛ                                      *   08_GARDEN.PY   *
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
# выведите на консоль все виды цветов
# TODO здесь ваш код
all_flowers = garden_set.union(meadow_set)
print(all_flowers)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
i_tam_i_tam = garden_set.intersection(meadow_set)
print(i_tam_i_tam)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print(garden_set-i_tam_i_tam)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
print(meadow_set-i_tam_i_tam)

#ФАЙЛ                                                    *   09_SHOPPING.PY   *
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    'печенье': [
        # {'shop': 'название магазина', 'price': 99.99},
        # TODO тут с клавиатуры введите магазины и цены (можно копипастить ;)
        {'shop': 'ашан', 'price': 10.99},
        {'shop': 'пятерочка', 'price': 9.99},
        {'shop': 'магнит', 'price': 11.99},
    ],
    # TODO тут с клавиатуры введите другую сладость и далее словарь магазинов
   'конфеты': [
        {'shop': 'ашан', 'price': 34.99},
        {'shop': 'пятерочка', 'price': 32.99},
        {'shop': 'магнит', 'price': 30.99},
    ],
    
    'карамель': [
        {'shop': 'ашан', 'price': 45.99},
        {'shop': 'пятерочка', 'price': 46.99},
        {'shop': 'магнит', 'price': 41.99},
    ],
    
    'пирожное': [
        {'shop': 'ашан', 'price': 67.99},
        {'shop': 'пятерочка', 'price': 59.99},
        {'shop': 'магнит', 'price': 62.99},
    ],
}
# Указать надо только по 2 магазина с минимальными ценами
lowprice={}
for i in sweets:
    lowprice[i]=[]
    for k in sweets[i]:
        a=k['price']
        for j in sweets[i]:
            if j['price'] > a:
                a=j['price']
    for j in sweets[i]:
        if j['price'] < a:
            lowprice[i].append(j)
for i in lowprice:
    print(i)
    for j in lowprice[i]:
        print(j['shop'],j['price'])
    print("\n")

#ФАЙЛ                                    *   10_STORE.PY  *

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
table_code = goods['Стол']
table_item = store[table_code][0]
table_item2 = store[table_code][1]
table_quantity = table_item['quantity']
table_quantity2 = table_item2['quantity']
table_price = table_item['price']
table_price2 =table_item2['price']
table_cost = table_quantity * table_price + table_quantity2 * table_price2
print('Стол -', table_quantity+table_quantity2, 'шт, стоимость', table_cost, 'руб')
# один раз распечать сколько всего стульев и их общая стоимость,
chair_code = goods['Стул']
chair_item = store[chair_code][0]
chair_item2 = store[chair_code][1]
chair_item3 = store[chair_code][2]
chair_quantity = chair_item['quantity']
chair_quantity2 = chair_item2['quantity']
chair_quantity3 = chair_item3['quantity']
chair_price = chair_item['price']
chair_price2 = chair_item2['price']
chair_price3 = chair_item3['price']
chair_cost = chair_quantity * chair_price + chair_quantity2 * chair_price2 + chair_quantity3 * chair_price3
print('Стул -', chair_quantity+chair_quantity2+chair_quantity3, 'шт, стоимость', chair_cost, 'руб')
#   и т.д. на складе
sofa_code = goods['Диван']
sofa_item = store[sofa_code][0]
sofa_item2 = store[sofa_code][1]
sofa_quantity = sofa_item['quantity']
sofa_quantity2 = sofa_item2['quantity']
sofa_price = sofa_item['price']
sofa_price2 = sofa_item2['price']
sofa_cost = sofa_quantity * sofa_price + sofa_quantity2 * sofa_price2
print('Диван -', sofa_quantity+sofa_quantity2, 'шт, стоимость', sofa_cost, 'руб')
```
