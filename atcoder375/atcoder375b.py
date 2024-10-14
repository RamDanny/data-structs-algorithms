import sys

#sys.stdin = open('in.txt', 'r')

def main():
    l = 0
    n, string = 0, ''
    start, end = 0, 0
    fin = False
    for line in sys.stdin:
        if l == 0:
            n = int(line)
        elif l == 1:
            string = line.split(' ')
        l += 1
    ans = []
    for i in range(len(string)-1):
        start, end = int(string[i]), int(string[i+1])
        ans.append(start)
        diff = int(string[i]) - int(string[i+1])
        if diff < -1:
            for num in range(start+1, end):
                ans.append(str(num))
        elif diff > 1:
            start, end = end, start
            for num in range(end-1, start, -1):
                ans.append(str(num))
    ans.append(string[-1])
    print(' '.join(map(str, ans)))

if __name__ == '__main__':
    main()
