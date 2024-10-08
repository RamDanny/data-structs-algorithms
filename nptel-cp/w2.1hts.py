t = int(input())
x, n = 0, 0
arr = []
ans = []

for i in range(t):
    possible = True
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    for index in range(n):
        if arr[index] - arr[n + index] < x:
            possible = False
            break
    if possible:
        ans.append("YES")
    else:
        ans.append("NO")

for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end="")
    else:
        print(ans[i])
