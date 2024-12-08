# Лабораторная работа №2
# Вариант 4
## Задание
1. Написать программу собственного варианта, используя оператор цикла while или do while.
2. Написать программу, используя оператор цикла for.
3. Построить график с использованием gnuplot.
4. Составить блок-схемы.
5. Оформить отчёт в README.md.
## Программа
#include <math.h>
#include <stdio.h>
int main(){
    double h;
    FILE *graph;
    printf(Enter h: ");
    scanf("%lf", &h);
    graph = fopen("graph.txt", "w");
      for (double x=0;x<=2;x=x+h;){
          if (x <= 2){
              fprinf(graph, "%lf\t%lf\n", x, sqrt(x+1) - sqrt(x) - 0,5);
              prinf("%lf\t%lf\n", x, sqrt(x+1) - sqrt(x) - 0,5);
          }else{
              fprinf(graph, "%lf\t%lf\n", x, exp(-x - 1/x));
          }
          fclose(graph);
          return 0;
      }
}
