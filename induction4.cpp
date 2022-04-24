#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;
bool search(int a[], int len, int item);

int main()
{
    int t; 
    cin >> t;
    int input[128]; int x[128], x1 = 0, X, y[128], y1 = 0, Y;
    int n = 0, tmp;
    // to get single-line input
    while( n < t && scanf( "%d", &tmp) != EOF) 
    {
            input[n++] = tmp;
    }
    
    // to find x
    int max = 0;
    for (int i = 0; i < t; i++)
    {
        if (input[i] > max) {max = input[i];}
    }
    X = max;

    // to find factors of x
    for (int i = 0; i < t; i++)
    {
        if (X % input[i] == 0 && search(x, t, input[i]) == false)
        {
            x[x1++] = input[i];
        }
        else {y[y1++] = input[i];}
    }

    // to find y
    max = 0;
    for (int i = 0; i < y1; i++)
    {
        if (y[i] > max) {max = y[i];}
    }
    Y = max;
    cout << X << " " << Y << endl;
    return 0;
}

bool search(int a[], int len, int item)
{
    bool flag = false;
    for (int i = 0; i < len; i++)
    {
        if (a[i] == item)
        {
            flag = true;break;
        }
    }
    return flag;
}