#include "tbb/task_scheduler_init.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "time.h"
#include "stdio.h"
using namespace tbb;
void Foo(int value)
{
    value = value*value;
}
class ApplyFoo
{
    int * const my_a;
    public:
    void operator() (const blocked_range<size_t> & r) const
    {
        int *a = my_a;
        int k = r.begin();
        int d = r.end();
        printf("begin = %d,end = %d\n",k,d);
        for(size_t i = r.begin();i != r.end();++i)
            Foo(a[i]);
    }

    ApplyFoo(int a[]) : my_a(a){}
};

int main()
{
    task_scheduler_init init;
    const int n = 1000000;
    int a[n];
    for(int i = 0; i < n; i++)
    a[i] = i;
    clock_t start,end;
    double total;
    start = clock(); 

    parallel_for(blocked_range<size_t>(0,n),ApplyFoo(a),auto_partitioner());
    end = clock();
    total = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f \n",total);
    return 0;
}