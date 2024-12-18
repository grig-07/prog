# Лабораторная работа №2
# Вариант 4
## Задание
``` c
1. Написать программу собственного варианта, используя оператор цикла while или do while.
2. Написать программу, используя оператор цикла for.
3. Построить график с использованием gnuplot.
4. Составить блок-схемы.
5. Оформить отчёт в README.md.
## Программа
``` c
#include <stdio.h>
#include <math.h>
int main(){
    double h, x=-1;
    FILE "graph;
    printf ("Enter h: ");
    scanf (*%1f*, &h);
    graph = fopen ("graph.txt", "w");
    while (x<=2){ 
        if (x<=1)(
            fprintf(graph, "%1f\t%1f\n*, x, exp(-2*sin(x)));
            printf("%1f\t%1f\n", x, exp(-2*sin(x)));
        } else(
            fprintf(graph, "X1f\t%1f\n*, x, pow(x,2) - cos(x)/sin(x));
            printf("x1f\t%1f\n", x, pow(x,2) -cos(x)/sin(x));
        }
        x+=h;
        x-round (x*1000000)/1000000;
    }
    fclose(graph);
    return 0;
}
```
