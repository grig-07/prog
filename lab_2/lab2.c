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
