import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

t = int(input())
n, m = 0, 0
a, b, ans = [], [], []

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    am = max(a)
    bm = max(b)
    if am > bm:
        ans.append(['Ankita', 'Ankita'])
    elif am < bm:
        ans.append(['Biswas', 'Biswas'])
    else:
        ans.append(['Ankita', 'Biswas'])

for i in range(len(ans)):
    for j in range(2):
        if i == len(ans)-1 and j == 1:
            print(ans[i][j], end="")
        else:
            print(ans[i][j])

