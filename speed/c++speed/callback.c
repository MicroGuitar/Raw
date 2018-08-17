#include <stdio.h>
#include <stdlib.h>
#include <time.h>

const int R = 1280;
const int L = 960;
const int Length = 1843200;

int main()
{   
    double total;
    clock_t start,end;
    start = clock(); 
    const char *file_name = "1.RAW";
    FILE *fp;
    fp = fopen(file_name,"rb");
    int i , j = 0;
    short int p0 = 0;
    short int p1 = 0;

    if(fp == NULL)
    {
        printf("can not open file\n");
    }
    unsigned char Raw[Length];
    unsigned char px_bytes[3];
    short int img[1228800];
    
    fread(Raw,sizeof(unsigned char),Length,fp);
    fclose(fp);    

    for(i = 0,j = 0; i < Length;j = j+2, i = i+3)
    {
        px_bytes[0] = Raw[i];
        px_bytes[1] = Raw[i+1];
        px_bytes[2] = Raw[i+2];
        p0 = ( (px_bytes[0] << 4) | (px_bytes[1]&0x0F) ) << 4;
        p1 = ( (px_bytes[2] << 4) | ((px_bytes[1] >> 4)&0x0F) ) << 4;

        img[j] = p0;
        img[j+1] = p1;
    }
    end = clock();
    total = (double)(end-start)/CLOCKS_PER_SEC;
    printf("%f \n",total);
    return 0;
}
