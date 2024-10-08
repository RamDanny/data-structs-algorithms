import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def diff(x, y):
    return x - y if x > y else y - x

def manh(x1, x2, y1, y2):
    return diff(x1, x2) + diff(y1, y2)

t = int(input())
n, m = 0, 0
graph = []
ans = []
result = []

for i in range(t):
    graph, ans = [], []
    n, m = list(map(int, input().split()))
    for j in range(n):
        graph.append(list(map(int, input().split())))
    for k in range(n):
        for l in range(m):
            #print(f'-{i, j, k, l}-')
            if graph[k][l] == 0:
                ans.append((k,l))
    #print(graph)
    #print(ans)
    #### brute force
    dmin = n * m
    for i in range(len(ans)):
        for j in range(i+1, len(ans)):
            mand = manh(ans[i][0], ans[j][0], ans[i][1], ans[j][1])
            if mand < dmin:
                dmin = mand
                #print(ans[i],ans[j])
    if dmin == n * m:
        result.append(-1)
    else:
        result.append(dmin)

for i in range(len(result)):
    if i == len(result)-1:
        print(result[i], end='')
    else:
        print(result[i])

'''fr = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            fr.append(i)
            fr.append(j)
            break
    if len(fr) > 0:
        break
if len(fr) == 0:
    print(-1)
'''
