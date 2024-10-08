import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

order = []

def path(src, dest, adj):
    global order
    q, visited = [], [False for i in range(n)]
    grp = 0
    q.append(src)
    visited[src-1] = True
    grp = (grp + 1) % 2
    while len(q) > 0:
        z = q.pop(0)
        if len(adj[z]) == 0:
            continue
        for nei in adj[z]:
            if visited[nei-1] == False and order.index(z) < order.index(nei):
                if nei == dest:
                    return True
                visited[nei-1] = True
                q.append(nei)
        grp = (grp + 1) % 2
    return False

n = int(input())
adj = dict()
for i in range(n):
    adj[i+1] = []
for i in range(n-1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)
v = list(map(int, input().split()))
d = list(map(int, input().split()))

tree = {0:[], 1:[]}
q, visited = [], [False for i in range(n)]

grp = 0
q.append(1)
order.append(1)
visited[1-1] = True
tree[grp].append(1)
grp = (grp + 1) % 2
while len(q) > 0:
    z = q.pop(0)
    for nei in adj[z]:
        if not visited[nei-1]:
            visited[nei-1] = True
            tree[grp].append(nei)
            q.append(nei)
            order.append(nei)
    grp = (grp + 1) % 2

#print(tree)
#print(order)

flips = 0

#print(v, d)
for k in range(2):
    for i in range(len(tree[k])):
        if v[tree[k][i]-1] != d[tree[k][i]-1]:
            v[tree[k][i]-1] = d[tree[k][i]-1]
            flips += 1
#            print(k,i,v,d)
            for j in range(i+1, len(tree[k])):
                if order.index(tree[k][i]) < order.index(tree[k][j]):
                    if path(tree[k][i], tree[k][j], adj):
                        v[tree[k][j]-1] = (v[tree[k][j]-1] + 1) % 2
    #                    print(k,i,v,d)
#    print(v, d)

#print(v, d)
print(flips, end='')