# include <stdio.h>

int main()
{
    int t;
    scanf("%d", &t);
    int c[100][3], sum[] = {0, 0, 0};
    for (int i = 0; i < t; i++)
    {
        scanf("%d %d %d", &c[i][0], &c[i][1], &c[i][2]);
        sum[0] += c[i][0]; sum[1] += c[i][1]; sum[2] += c[i][2];
    }
    if (sum[0] == 0 && sum[1] == 0 && sum[2] == 0)
    {
        printf("YES\n");
    }
    else {printf("NO\n");}
    return 0;
}