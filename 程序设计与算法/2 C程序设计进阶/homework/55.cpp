#include<stdio.h>
#include<string.h>
#define N 256
int main()
{
    int n;
    char arr[N];
    char *p = arr;
    scanf("%d",&n);
    for(int i =0;i<n;i++)
    {
        scanf("%s",p);
        int len = strlen(arr);
        for(int j = 0;j<len;j++)
        {
              if(*(p+j) =='A')
                *(p+j)  = 'T';
             else if(*(p+j)  =='T')
                *(p+j)  = 'A';
             else if(*(p+j)  =='G')
                *(p+j)  = 'C';
             else if(*(p+j)  =='C')
                *(p+j)  = 'G';
        }
        printf("%s\n",p);
      }

    return 0;
}