import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def mod(x):
    return x if x >= 0 else 0-x

t = int(input())
s, f = '', ''
#sset, fset = set(), set()
minop = []

for i in range(t):
    s = input()
    f = input()
    #sl, fset = list(s), set(f)
    minop.append(0)
    mind = 30
    for i in range(len(s)):
        mind = 30
        for j in range(len(f)):
            if mod(ord(s[i]) - ord(f[j])) < mind:
                mind = mod(ord(s[i]) - ord(f[j]))
        minop[-1] += mind

for i in range(1, len(minop)+1):
    print('Case #'+str(i)+': '+str(minop[i-1]))

