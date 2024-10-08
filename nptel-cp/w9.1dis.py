import sys
import copy

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def bip(adj, u, visited, matched, n):
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            if matched[v] < 0 or bip(adj, matched[v], visited, matched, n):
                matched[v] = u
                return True
    return False

def mm(adj, k, n):
    matched = [-1 for i in range(2*n)]
    maxmat = 0
    for u in range(n):
        visited = [False for i in range(2*n)]
        if bip(adj, u, visited, matched, n):
            maxmat += 1
    if maxmat >= n-k:
        return 'YES'
    else:
        return 'NO'

n, m = list(map(int, input().split()))
k = int(input())
adj = [[] for i in range(n)]
for i in range(m):
    u, v = list(map(int, input().split()))
    adj[u-1].append(v-1)

adj2 = [[] for i in range(2*n)]
for i in range(n):
    for j in adj[i]:
        adj2[i].append(n+j)
        adj2[n+j].append(i)

print(mm(adj2, k, n), end='')
