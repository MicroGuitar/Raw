#include<stddef.h>
#include<stdio.h>
#include <time.h>
int main()
{

    int m1[3][3] = {{1,1,1},{1,1,1},{1,1,1}};
    int m2[3][3] = {{2,2,2},{2,2,2},{2,2,2}};
    int result[3][3] = {0};
    clock_t start,end;
    double total;
    start = clock(); 
    for(int a = 0; a <1000000; a++)
    {
        for(size_t i = 0; i < 3; i++)
        {
            for(size_t j = 0; j < 3; j++)
            {
                int temp = 0;
                for(int k = 0; k < 3; k++)
                {
                    temp += m1[i][k]*m2[k][j];
                }
                result[i][j] = temp;
            }
        } 
    }
    end = clock();
    total = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f \n",total);
    // for(size_t i = 0; i < 3; i++)
    // {
    //     for(size_t j = 0; j < 3; j++)
    //     {
    //         int temp = 0;
    //         for(int k = 0; k < 3; k++)
    //         {
    //             temp += m1[i][k]*m2[k][j];
    //         }
    //         result[i][j] = temp;
    //     }
    // }
    // for(size_t i = 0; i < 3; i++)
    // {
    //     for(size_t j = 0; j < 3; j++)
    //     {
    //         printf("%d ",result[i][j]);
    //     }
    //     printf("\n");
    // }
    return 0;
}