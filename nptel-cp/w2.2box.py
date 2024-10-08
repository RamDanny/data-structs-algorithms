t = int(input())
n, q = 0, 0
arr = []
que = []
ans = []

for i in range(t):
    n, q = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    que = []
    for j in range(q):
        que.append(int(input()))
    for j in range(len(que)):
        if que[j] <= arr[0]:
            ans.append(1)
        else:
            sum, k = 0, 0
            while sum < que[j] and k < len(arr):
                sum += arr[k]
                k += 1
            if sum < que[j]:
                ans.append(-1)
            else:
                ans.append(k)

for i in range(len(ans)):
    if i == len(ans)-1:
        print(ans[i], end="")
    else:
        print(ans[i])
