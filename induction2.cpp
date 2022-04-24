#include <iostream>
#include <conio.h>
#include <stdio.h>
#include <string.h>

using namespace std;
bool search(char s[], int len);

int main()
{
    int t; 
    cin >> t;
    char input[20000][200000], s[200000], ss[200000];
    int output[20000]; int len;
    for(int i = 0; i < t; i++)
    {
        gets(s); len = strlen(s);
        for (int j = 0; j < len; j++)
        {
            input[i][j] = s[j];
        }
    }
    bool flag;
    for (int i = 0; i < t; i++)
    {

    }
    return 0;
}

bool search(char s[], int len)
{
    int flag = 1;
    for (int i = 0; i < len; i++)
    {
        if (s[0] == 1)
        {
            if (s[i] == 2)
            {
                flag++;
            }
        }
    }
}