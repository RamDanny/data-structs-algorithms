import math

def value(n):
    global s
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return (n//2) ** 2 + (2 * value(n//2))
    else:
        return ((n//2) * (n - (n//2)))  + (value(n//2) + value(n - (n//2)))

t = int(input())

ans = []

for i in range(t):
    n = int(input())
    ans.append(value(n))

print("Testcases")
for num in ans:
    print(num)
