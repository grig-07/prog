# Задание 1
import itertools
alphabet = "НАСТЯ"
ar = itertools.product(alphabet, repeat = 6)
arl = []
for i in ar:
    arl.append(list(i))
count = 0
for e in arl:
    if e.count("A") <= 1 and e.count("Я") <= 1:
        count += 1
print(count)

# Задание 2
x = 16 ** 8 * 4 ** 10 - 46 - 16
a = ''
while x != 0:
    a += str(x % 4)
    x //= 4
a = a[::-1]
print(a.count("3"))

# Задание 3
def find_numbers(start):
    result = []
    for num in range(start, float('inf')):
        min_divisor, max_divisor = find_min_max_divisors(num)
        M = min_divisor + max_divisor
        if M % 7 == 3:
            result.append((num, M))
            if len(result) == 5:
                break
    return result
    
from math import sqrt

def find_min_max_divisors(num):
    if num == 1:
        return None, None # Нет делителей, кроме 1
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return i, num // i
    return num, 1 # Число простое

# Вывод результата
    for num, M in result:
        print(f"Число: {num}, M: {M}")