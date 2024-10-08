import sys
import copy

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def f(a):
    maxi = 0
    sums = 0
    index = 0
    while index < len(a):
        sums += a[index]
        if sums > maxi:
            maxi = sums
        index += 1
    return maxi

t = int(input())
n, r, m, b = 0, [], 0, []

for i in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    if i == t-1:
        print(f(r) + f(b), end='')
    else:
        print(f(r) + f(b))
