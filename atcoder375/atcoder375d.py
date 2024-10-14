import sys

#sys.stdin = open('in.txt', 'r')

def select(arr):
    ans, row = [], []
    for i in range(2**(len(arr))):
        bits = i
        for j in range(len(arr)):
            if (bits & 1) == 1:
                row.append(arr[j])
            bits = bits >> 1
        ans.append(row)
        row = []
    return ans

def main():
    l = 0
    string, n = '', 0
    for line in sys.stdin:
        if l == 0:
            string = line.split('\n')[0]
        elif l == 1:
            n = int(line.split('\n')[0])
        l += 1
    total = 0
    powers, sums = [], []
    for i in range(len(string)):
        if string[i] == '?':
            powers.append(len(string)-1-i)
        else:
            total += int(string[i]) * 2**(len(string)-1-i)
    #print(total, powers)
    if total > n:
        print(-1)
    else:
        sel = select(powers)
        for l in sel:
            if len(l) == 0:
                sums.append(total)
            else:
                temp = total
                for num in l:
                    temp += 2**num
                sums.append(temp)
        max_num = -1
        for number in sums:
            if number <= n and number > max_num:
                max_num = number
        print(max_num)

if __name__ == '__main__':
    main()
