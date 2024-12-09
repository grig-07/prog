# Решение с рекурсией
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
print(to_str_recursive(lst)) # Вывод: 1 -> 2 -> 3 -> 4 -> 5 -> None
# Без рекурсии
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