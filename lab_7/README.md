# Лабораторная работа №7
## Вариант 4
## Задание
1. Напишите две функции для решения задач своего варианта - с использованием рекурсии и без.
2. Оформите отчёт в README.md. Отчёт должен содержать:
    1. Условия задач;
    2. Описание проделанной работы;
    3. Скриншоты результатов.
## Условие задачи:
Требуется создать функцию для преобразования вложенных списков в строку:
>>> to_str([1, [2, [3, [4, [5]]]]])
'1 -> 2 -> 3 -> 4 -> 5 -> None'

Функция для расчёта ai=ai−2+ai−12i−1 a_i = a_{i-2} + \frac{a_{i-1}}{2^{i-1}} ai​=ai−2​+2i−1ai−1​​. a0=a1=1 a_0 = a_1 = 1 a0​=a1​=1.
## С использованием рекурсии:
``` py
def to_str_recursive(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.append(to_str_recursive(item)) # Рекурсивный вызов для вложенных списков
        else:
            result.append(str(item))
    return " -> ".join(result)

# Пример использования:
lst = [[1, 2], [3, [4, 5]]]
print(to_str_iterative(lst)) # Вывод: 1 -> 2 -> 3 -> 4 -> 5 -> None
```
## Без рекурсии:
``` py
def to_str_iterative(lst):
    result = []
    stack = [lst]
    
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1]) # Добавляем элементы в обратном порядке
        else:
            result.append(str(current))

    final_string = " -> ".join(result) + " -> None"
    return final_string # Возвращаем строку

lst = [[1, 2], [3, [4, 5]]]
output = to_str_iterative(lst)
print(output)
``` 
## Скриншоты вывода терминала:
![result](resultlab7.png)

