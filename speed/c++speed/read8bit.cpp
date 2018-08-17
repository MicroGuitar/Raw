#include <fstream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
const int R = 1280;
const int L = 960;

int main(int atgc,char **argv)
{
    const char *file_name = "uint8.RAW";
    FILE *fp;
    fp = fopen(file_name,"rb");
    int k = 0;
    int i , j = 0;

    if(fp == NULL)
    {
        printf("can not open file\n");
    }
    unsigned char image[L][R];
    fread(image,sizeof(unsigned char),R*L,fp);
    fclose(fp);
    for(i = 0; i < 10; i++)
    {
        for(j = 0; j < 10; j++)
        {
            printf("%d ",image[i][j]);
            
        }
        printf("\n");
    }
    
    return 0;
}
