# include <bits/stdc++.h>

using namespace std;

# define vi vector<int>
# define vll vector<long long int>

int main()
{
    int a[100], n;
    std::cin >> n;
    for (int i = 0; i < n; i++)
        std::cin >> a[i];
    for (int i = 0; i < n; i++)
        std::cout << a[i] << " ";
    std::cout << endl;
    return 0;
}
