# include <bits/stdc++.h>

int main()
{
    char s[200], t[200]; int i = 0, dig = 0;
    scanf("%s", s);
    while (i < strlen(s))
    {
        if (s[i] == '.')
        {
            t[dig++] = '0'; i++;
        }
        else if (s[i] == '-' && s[i+1] == '.')
        {
            t[dig++] = '1'; i += 2;
        }
        else if (s[i] == '-' && s[i+1] == '-')
        {
            t[dig++] = '2'; i += 2;
        }
        t[dig] = '\0';
    }
    printf("%s", t);
    return 0;
}