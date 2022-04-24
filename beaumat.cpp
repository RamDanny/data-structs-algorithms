# include <stdio.h>

int main()
{
    int a[5][5], x, y;
    for (int i = 0; i < 5; i++)
    {
        scanf("%d %d %d %d %d", &a[i][0], &a[i][1], &a[i][2], &a[i][3], &a[i][4]);
        if (a[i][0] == 1) {y = 0; x = i;}
        else if (a[i][1] == 1) {y = 1; x = i;}
        else if (a[i][2] == 1) {y = 2; x = i;}
        else if (a[i][3] == 1) {y = 3; x = i;}
        else if (a[i][4] == 1) {y = 4; x = i;}
    }
    int moves = 0;
    moves += (x > 2 ? x-2 : 2-x);
    moves += (y > 2 ? y-2 : 2-y);
    printf("%d\n", moves);
    return 0;
}