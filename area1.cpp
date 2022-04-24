#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <math.h>

using namespace std;
double tarea(double s1, double s2, double s3);
bool search(double a[], int len, double item);


int main()
{
    int t; 
    cin >> t;
    int n, tmp;
    const int N = 50;
    
    int coord[N];
    double areas[1225]; int k = 0;
    int ans[100]; int g = 0;
    
    double a, b, c, ar;
    for (int i = 0; i < t; i++)
    {
        int n1 = 0;
        cin >> n;
        k = 0;
        // max no. of areas possible = Nc2 = 50c2 = 1225
        // to get single-line input for array
        while( n1 < n && scanf( "%d", &tmp) != EOF) 
        {
            coord[n1++] = tmp;
        }
        
        for (int x1 = 0; x1 < n; x1++)
        {
            for (int x2 = x1 + 1; x2 < n; x2++)
            {
                a = sqrt(1 + (coord[x1] * coord[x1]));
                b = sqrt(1 + (coord[x2] * coord[x2]));
                c = coord[x2] - coord[x1];
                ar = tarea(a, b, c);
                bool search_result = search(areas, k, ar);
                if (search_result == false && ar != 0)
                {
                    areas[k++] = (double)ar;
                }
            }
        }
        ans[g++] = k;
    }
    for(int i = 0; i < g; i++)
    {
        cout << ans[i] << endl;
    }
    return 0;
}


double tarea(double s1, double s2, double s3)
{
    double s = (s1 + s2 + s3) / 2;
    double a = sqrt(s * (s - s1) * (s - s2) * (s - s3));
    return a;
}

bool search(double a[], int len, double item)
{
    bool flag = false;
    for (int i = 0; i < len; i++)
    {
        if (abs(a[i] - item) < 0.001)
        {
            flag = true;break;
        }
    }
    return flag;
}