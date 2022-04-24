#include <iostream>
#include <conio.h>
#include <stdio.h>

using namespace std;

int main()
{
    /*int n, f = 0; 
    cin >> n;
    for (int i = 0; i < n/2; i++)
    {
        int j = n - i;
        if (i % 2 == 0 && j % 2 == 0)
        {
            cout << "yes\n"; f = 1;
            break;
        }
    }    
    if (f == 0) {cout << "no\n";}
    return 0; */
    int n; cin >> n;
    if (n%2 == 0) {cout << "yes\n";}
    else {cout << "no\n";}
    return 0;
}
