# Лабораторная работа №8
##Задание
1. Решите обе задачи своего варианта.
2. Примените декоратор к замыканию.
3. Оформите отчёт в README.md. Отчёт должен содержать:
-Условия задач
-Описание проделанной работы
-Скриншоты результатов
## Вариант 4
1. Замыкание, отбирающее только уникальные значения из переданных.
2. Декоратор, который будет ограничивать количество вызовов функций.
# 1.
``` py
def unique_generator():
  seen = set()
  for value in data:
    if value not in seen:
      seen.add(value)
      yield value


# Пример использования
data = [1, 2, 2, 3, 4, 4, 5]

# Используем генератор для получения уникальных значений
unique_values = list(unique_generator())

print(unique_values)  # Вывод: [1, 2, 3, 4, 5]
```
## Вывод терминала
![№1](lab8(1).PNG)


# 2.
```py
def limit_calls(max_calls, error_message='Function called too many times'):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            if count < max_calls:
                count += 1
                return func(*args, **kwargs)
            else:
                raise Exception(error_message)

        return wrapper

    return decorator


@limit_calls(3, "Function 'my_function' has been called too many times")
def my_function():
    print("Function called")


# Пример использования
try:
    my_function()  # Вывод: Function called
    my_function()  # Вывод: Function called
    my_function()  # Вывод: Function called
    my_function()  # Вызовет исключение
except Exception as e:
    print(e)  # Вывод: Function 'my_function' has been called too ma
```
limit_calls — это функция-декоратор, которая принимает два аргумента: max_calls (максимальное количество вызовов) и error_message (сообщение об ошибке).
Внутри limit_calls определяется функция decorator, которая принимает функцию func для декорирования.
wrapper — это внутренняя функция, которая увеличивает счетчик count при каждом вызове и проверяет, не превышено ли максимальное количество вызовов. Если количество вызовов превышено, то выбрасывается исключение. Таким образом, декорируем функцию my_function и вызываем её несколько раз. После трех вызовов, следующий вызов приведет к выбросу исключения.
# Вывод терминала
[№2](lab8(2).PNG)
