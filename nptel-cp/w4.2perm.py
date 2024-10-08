import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def make(p):
    marked = [0 for i in range(len(p))]
    result = []
    while 0 in marked:
        temp = []
        x, xi = marked.index(0), marked.index(0)
        marked[x] = 1
        temp.append(x+1)
        x = p[x]
        while x != xi+1:
            #print(temp)
            marked[x-1] = 1
            temp.append(x)
            x = p[x-1]
        result.append(temp)
    return result

ans = []

t = int(input())
for test in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    cycles = make(p)
    ans1 = []
    for i in range(len(p)):
        for j in range(len(cycles)):
            if i+1 in cycles[j]:
                ans1.append(len(cycles[j]))
                break
    ans.append(ans1)

for i in range(len(ans)):
    for j in range(len(ans[i])):
        if j == len(ans[i])-1:
            if i == len(ans)-1:
                print(ans[i][j], end='')
            else:
                print(ans[i][j])
        else:
            print(ans[i][j], end=' ')
