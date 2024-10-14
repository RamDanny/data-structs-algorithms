import sys

#sys.stdin = open('in.txt', 'r')

def main():
    l = 0
    n, string = 0, ''
    ct, ca = 0, 0
    fin = False
    for line in sys.stdin:
        if l == 0:
            n = int(line)
        elif l == 1:
            string = line
        l += 1
    for c in string:
        if c == 'T':
            ct += 1
        elif c == 'A':
            ca += 1
        if ct >= n//2 or ca >= n//2:
            break
    print('T') if ct > ca else print('A')

if __name__ == '__main__':
    main()
