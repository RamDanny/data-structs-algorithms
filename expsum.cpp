#include <bits/stdc++.h>
using namespace std;

int main()
{
    int T;
    scanf("%d", &T);
    long int a[1000];
    long int n; long int sum = 0, sum2 = 0;
    for (int t = 0; t < T; t++)
    {
        scanf("%ld", &a[t]);
    }
    int now = -1, isone = -1;
    for (int t = 0; t < T; t++)
    {
        sum = 0;
        n = a[t];
        now = -1;
        isone = -1;
        for (long int i = 2; i <= n; i++)
        {
            if (now == 1)
            {
                sum += 1;
            }
            else
            {
                for (int j = 1; pow((double)(i), (double)(j)) <= n; j++)
                {
                    sum += j;
                    if (j == 1)
                    {
                        if (isone == -1){isone = 1;}
                        else if (isone = 1) {now = 1;}
                    }
                    else {isone = -1;}
                }
            }
        }
        printf("%ld\n", sum);
    }
    return 0;
}