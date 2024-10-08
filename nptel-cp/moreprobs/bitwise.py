import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

def zeroes(x):
    zero = 0
    for i in range(len(bin(x))):
        if bin(x)[i] == '0':
            zero += 1
    return zero

n = int(input())
a = list(map(int, input().split()))
b = ''
for i in a:
    b += 
q = int(input())
for i in range(q):
    x, y = list(map(int, input().split()))
