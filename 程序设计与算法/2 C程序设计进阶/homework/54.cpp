#include<stdio.h>
#define N 20
int main()
{
    int m,n;
    int high[N][N];
    int flag[N][N];
    int (*f)[N]=flag;
    int (*ph)[N] = high;
    scanf("%d %d",&m,&n);
    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            scanf("%d",*(ph+i)+j);
        }
    }

    for(int i=0;i<m;i++)
    {
        for(int j=0;j<n;j++)
        {
            bool shan = true;

            if (shan && i-1>=0) {
                if (ph[i][j]<ph[i-1][j]) {
                    shan = false;
                }
            }

            if (shan && i+1<m) {
                if (ph[i][j]<ph[i+1][j]) {
                    shan = false;
                }
            }

            if (shan && j-1>=0) {
                if (ph[i][j]<ph[i][j-1]) {
                    shan = false;
                }
            }

            if (shan && j+1<n) {
                if (ph[i][j]<ph[i][j+1]) {
                    shan = false;
                }
            }

            if (shan) {
                printf("%d %d\n", i, j);
        }
    }
    }


    return 0;
}