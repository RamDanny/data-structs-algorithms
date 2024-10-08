n = int(input())
#a = [0 for i in range(100001)]
a = [0 for i in range(15)]
l = map(int,input().split())
for i in l:
    a[i] += i
x, y = 0, 0
for i in a:
    #x, y = max(x, i+y), x
    y1 = x
    x = max(x, i+y)
    y = y1
    print(f'({x}, {y})')
print(x)#, end='')