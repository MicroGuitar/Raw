#include "time.h"
#include "stdio.h"
void Foo(int value)
{
    value = value*value;
}
int main()
{
    const int n = 1000000;
    int a[n];
    clock_t start,end;
    double total;
    for(int i = 0; i < n; i++)
        a[i] = i;

    start = clock(); 
    for(size_t i = 0;i < n;i++)
        Foo(a[i]);
    end = clock();
    total = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f \n",total);
    return 0;
}