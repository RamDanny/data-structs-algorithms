import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def ascendants(l, x):
    asc = []
    node = x
    while l[node-1] != -1:
        asc.append(l[node-1])
        node = l[node-1]
    return asc

def subset(a, b):
    s = a if len(a) < len(b) else b
    l = a if len(a) > len(b) else b
    for i in s:
        if i in l:
            continue
        else:
            return False
    return True

n = int(input())
parent, asc = [], []

for i in range(n):
    parent.append(int(input()))

m = -1

for i in range(n):
    #asc.append(ascendants(parent, i+1))
    asc = ascendants(parent, i+1)
    if len(asc) + 1 > m:
        m = len(asc) + 1

print(m)
#print(parent, asc)
