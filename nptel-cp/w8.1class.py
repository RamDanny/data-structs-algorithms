import sys
import copy

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

n, m = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

siz = n+m+2
initial = [[0 for i in range(siz)]for j in range(siz)]

# src to a[i]
for i in range(1, n+1):
    initial[0][i] = 1

# b[i] to dest
for i in range(1, m+1):
    initial[n + i][siz-1] = 1

# a[i] to b[i]
for i in range(1, n+1):
    for j in range(n+1, n+m+1):
        if a[i-1] <= b[j-n-1]:
            initial[i][j] = 1

#for row in initial:
#    print(row)

def dfs(adj, src, dest, path):
  vertices = len(adj)
  visited = [False for i in range(vertices)]
  stack = []
  stack.append(src)
  visited[src] = True
  path[src] = -1
  isunv = False
  while len(stack) != 0:
    top = stack.pop()
    visited[top] = True
    for i in range(vertices):
      if visited[i] == False and adj[top][i] > 0:
        stack.append(i)
        path[i] = top
        visited[i] = True
  return visited[dest] == 1

def ff(adj, src, dest):
  path = [-1 for i in range(len(adj))]
  vertices = len(adj)
  maxflow = 0
  # algo runs as long as augementing path found
  while dfs(adj, src, dest, path):
    bottleneck = 999
    node = dest
    while node != src:
      parent = path[node]
      bottleneck = adj[parent][node] if adj[parent][node] < bottleneck else bottleneck
      node = parent
    maxflow += bottleneck
    v2 = dest
    v1 = path[v2]
    while v2 != src:
      adj[v1][v2] -= bottleneck # subtracting bottleneck
      adj[v2][v1] += bottleneck # adding back edge
      v2 = path[v2]
      v1 = path[v1]
  return maxflow

src, dest = 0, siz-1
adj = copy.deepcopy(initial)
print(ff(adj, src, dest))
