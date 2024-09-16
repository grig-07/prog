# Лабораторная работа №0
## Задание
Написать програму на языке C.
## Проделанная работа
1. Написан файл "hello.c":
""""c
#include <stdio.h>

int main() {
 printf("Hello world!\n");
 return 0;
}
2. Препроцессор: "cpp lab0.c -o pp.c"
3. Запущен компилятор: "cc -S pp.c -o lab0.S"
4. Запущен ассемблер: "as lab0.S -o lab.o"
5. Запущен линковщик: "cc lab0.o -o lab"
## Скриншот
! [Компиляция и запуск](screenshot.png)
