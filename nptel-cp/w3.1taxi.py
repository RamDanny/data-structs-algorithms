import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

t = int(input())
n, q = 0, 0
arr, ans = [], []
start, stop, sa, so = 0, 0, 0, 0

for i in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    ans.append(0)
    for j in range(q):
        start, stop = list(map(int, input().split()))
        try:
            sa = arr.index(start)
            try:
                so = arr.index(stop, sa)
                ans[-1] += 1
            except ValueError:
                continue
        except ValueError:
            continue

for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end="")
    else:
        print(ans[i])

