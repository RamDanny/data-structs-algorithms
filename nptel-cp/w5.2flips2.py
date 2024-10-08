import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

flips = 0

def printtree(root, parent, level=0):
    if len(adj[root]) > 0:
        print(('\t\t')*level, root)
        print(('\t\t')*level, s[root], t[root], c[root], ' ', visited[root])
        for nei in adj[root]:
            printtree(nei, parent, level+1)
    else:
        print('\t\t'*level, root)
        print(('\t\t')*level, s[root], t[root], c[root], ' ', visited[root])

def gparent(cur, parent):
    if parent[cur] != -1:
        if parent[parent[cur]] != -1:
            return parent[parent[cur]]
        return -1
    return -1

def traverse(root, parent):
    global flips
    gp = gparent(root, parent)
    if gp == -1:            # if no gparent
        if c[root] != t[root]:        # if src target diff
            c[root] = t[root]
            flips += 1
            print(f'Flipped {root}')
    else:                   # if gparent exists
        if c[gp] != s[gp]:        # if gparent flipped
            if c[root] == t[root]:            # if gparent flip disrupts cur
                flips += 1
                print(f'Flipped {root} due to {gp}')
            else:                       # if gparent resolves cur
                c[root] = t[root]
        else:                     # if gparent not flipped
            if c[root] != t[root]:            # if src target diff
                c[root] = t[root]
                flips += 1
                print(f'Flipped {root}')
    if len(adj[root]) > 0:
        for nei in adj[root]:
            traverse(nei, parent)

# building adj list
n = int(input())
adj = dict()
for i in range(n):
    adj[i+1] = []
for i in range(n-1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)
v = list(map(int, input().split())) # src list
d = list(map(int, input().split())) # target list

s, t, c = [-1], [-1], [-1]
s.extend(v) # s = v
t.extend(d) # t = d
c.extend(v) # current list

#print(s, t, c)

# building parent list
parent = [-1 for i in range(n+1)]
visited = [False for i in range(n+1)]
q = [1]
visited[1] = True
while len(q) > 0:
    z = q.pop(0)
    for nei in adj[z]:
        if not visited[nei]:
            visited[nei] = True
            parent[nei] = z
            q.append(nei)

# trimming parent
for nod in adj:
    topop = -1
    for i in range(len(adj[nod])):
        if parent[nod] == adj[nod][i]:
            topop = i
            break
    if topop > -1:
        temp = adj[nod].pop(i)

'''print(adj)
print(parent)
printtree(1, parent)'''

# global flips
flips = 0

# traversing tree
traverse(1, parent)

print(flips, end='')
