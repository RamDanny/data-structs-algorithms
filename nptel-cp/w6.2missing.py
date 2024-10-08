import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

n, m, l, s, t = list(map(int, input().split()))

graph = [[999 for i in range(n)] for j in range(n)]
adj = [[999 for i in range(n)] for j in range(n)]
detour = [[-1 for i in range(n)] for j in range(n)]
parent = [-1 for i in range(n)]

for i in range(m):
    b, e, w = list(map(int, input().split()))
    adj[b][e] = w
    adj[e][b] = w
    graph[b][e] = w
    graph[e][b] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]
                detour[i][j] = k
                parent[k] = i
                parent[j] = k

path = [s]
def paths(s, t):
    global path, detour
    if detour[s][t] == -1:
        path.append(t)
    else:
        paths(s, detour[s][t])
        paths(detour[s][t], t)

paths(s, t)
zero = False
for i in range(len(path)-1):
    if graph[path[i]][path[i+1]] == 0:
        zero = True
        break
print(path, zero)
if adj[s][t] > l:
    print('NO')
elif adj[s][t] == l:
    print('YES')
elif zero:
    print('YES')
else:
    print('NO')

'''zero = False
x, y = s, t
while detour[x][y] != -1:
    if graph[parent[y]][y] == 0:
        zero = True
        break
    y = parent[y]'''

'''if adj[s][t] <= l:
    ifzero(s, t, graph, parent)
    if adj[s][t] == l:
        print('YES')
    elif zero:
        print('YES')
    else:
        print('NO')
else:
    print('NO')'''
'''
path = []
zero = False
def ifzero(s, t, graph, parent):
    global path
    if detour[s][t] == -1:
        path.append(t)
    else:
        ifzero(s, detour[s][t], graph, parent)
        ifzero(detour[s][t], t, graph, parent)
    x = t
    path = []
    path.append(x)
    while parent[x] != -1:
        x = parent[x]
        path.append(x)
    if x != s:
        return False
for i in range(len(path)-1):
    if graph[i+1][i] == 0:
        #return True
        zero = True
        break
    #return False

if adj[s][t] <= l:
    ifzero(s, t, graph, parent)
    if adj[s][t] == l:
        print('YES')
    elif zero:
        print('YES')
    else:
        print('NO')
else:
    print('NO')'''
