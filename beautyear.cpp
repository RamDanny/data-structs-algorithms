# include <bits/stdc++.h>

int distinct(int y);

int main()
{
    int y, i;
    scanf("%d", &y);
    for (i = y + 1; distinct(i) != 1; i++);
    printf("%d", i);
    return 0;
}

int distinct(int y)
{
    int x = y, r, a[4], k = 0;
    while (x > 0)
    {
        r = x % 10;
        for (int i = 0; i < k; i++)
        {
            if (r == a[i])
            {
                return 0;
            }
        }
        a[k++] = r;
        x = x / 10;
    }
    return 1;
}