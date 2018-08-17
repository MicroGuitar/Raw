#include "tbb/task_scheduler_init.h"
#include "tbb/blocked_range.h"
#include "tbb/parallel_for.h"
#include "time.h"
#include "stdio.h"
using namespace tbb;
/*************gcc tbb_read.cpp -ltbb -std=c++11 -lstdc++ -o tbb_read************/
class ApplyFoo
{
    unsigned char * const my_a;
    short * const dst;
    const int Length_12 = 1843200;
    public:
    void operator() (const blocked_range<size_t> & r)  const
    {
        unsigned char *a = my_a;
        short *b = dst;
        short int p0 = 0;
        short int p1 = 0;
        unsigned char px_bytes[3] = {0};
        size_t i , j = 0;
        printf("coming\n");
        int k = r.begin()/1.5;
        int e = r.end();
        printf("%d\n",k);
        printf("%d\n",e);
        for( i = r.begin(), j = r.begin()/1.5; i != r.end();j = j+2, i = i+3)
        {
            px_bytes[0] = my_a[i];
            px_bytes[1] = my_a[i+1];
            px_bytes[2] = my_a[i+2];
            p0 = ( (px_bytes[0] << 4) | (px_bytes[1]&0x0F) ) << 4;
            p1 = ( (px_bytes[2] << 4) | ((px_bytes[1] >> 4)&0x0F) ) << 4;

            b[j] = p0;
            b[j+1] = p1;
            
        }
    }

    ApplyFoo(unsigned char a[],short b[]) 
    : my_a(a),dst(b)
    {

    }
};

int main()
{
    task_scheduler_init init;
    const int R = 1280;
    const int L = 960;
    const int Length_12 = 1843200;
    double total;
    clock_t start,end;
    const char *file_name = "1.RAW";
    FILE *fp;
    fp = fopen(file_name,"rb");
    int i , j = 0;
    short int p0 = 0;
    short int p1 = 0;
    unsigned char Raw[Length_12];
    unsigned char px_bytes[3];
    short int img[1228800];
    size_t grainsize = 1843200;
    start = clock(); 
    if(fp == NULL)
    {
        printf("can not open file\n");
    }
    fread(Raw,sizeof(unsigned char),Length_12,fp);
    fclose(fp);

    parallel_for(blocked_range<size_t>(0,1843200, grainsize),ApplyFoo(Raw,img),simple_partitioner());
    end = clock();
    printf("%d\n",img[0]);
    total = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f \n",total);
    return 0;
}