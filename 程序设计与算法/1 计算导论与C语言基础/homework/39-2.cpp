# include<stdio.h>
# include<string.h>

int main(void)
{
    char s1[11], s2[4];
    int i;
    while(scanf("%s%s", s1, s2)!=EOF)
    {
        int max=0;
        int len=strlen(s1);
        for(i=0; i<len; i++)
        {
            if(s1[i]>s1[max])
            {
                max=i;
            }
        }
        for(i=0; i<=max; i++)
        printf("%c", s1[i]);
        printf("%s", s2);
        for(i=max+1; i<len; i++)
        printf("%c", s1[i]);
        printf("\n");
    }

    return 0;
}