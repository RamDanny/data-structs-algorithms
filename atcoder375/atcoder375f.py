import sys
import itertools

#sys.stdin = open('in.txt', 'r')

def mapitoc(i):
    if i >=0 and i <=25:
        return chr(65+i)
    elif i >= 26 and i <= 51:
        return chr(71+i)
    else:
        return None

def addcarry(arr, i, carry):
    if i < len(arr):
        if arr[i] + carry >= 52:
            arr[i] = (arr[i]+carry) % 52
            addcarry(arr, i+1, carry)
        else:
            arr[i] += carry

def addone(arr):
    if arr[0]+1 >= 52:
        arr[0] = (arr[0]+1) % 52
        addcarry(arr, 1, 1)
    else:
        arr[0] += 1

def combos(arr):
    n = len(arr)
    buf = ['A' for i in range(n)]
    ans = [0 for i in range(n)]
    ret = []
    ret.append(''.join(buf))
    for i in range((52**n)-1):
        addone(ans)
        for j in range(n):
            buf[j] = mapitoc(ans[j])
        ret.append(''.join(buf))
        #print(f'-{buf}-', end=' ')
    return ret

def isddos(string):
    if len(string) == 4 and string[0] == string[1] and (ord(string[0]) >= 65 and ord(string[0]) <= 90) and (ord(string[2]) >= 97 and ord(string[2]) <= 122):
        return True
    else:
        return False

def subs(string):
    lst = [c for c in string]
    combs = []
    for i in range(1, len(lst)+1):
        els = [list(x) for x in itertools.combinations(lst, i)]
        combs.extend(els)
    return combs

def possible(string):
    total = 0
    ps = []
    indexs = []
    for i in range(len(string)):
        if string[i] == '?':
            indexs.append(i)
        ps.append(string[i])
    #print(f'-{indexs}-')
    combs = combos(indexs)
    for i in range(len(combs)):
        si, sii = combs[i], 0
        for j in range(len(indexs)):
            ps[indexs[j]] = si[sii]
            sii += 1
        #print(''.join(ps), end=' ')
        doinc = False
        for sub in subs(ps):
            if isddos(''.join(sub)):
                doinc = True
                break
        if not doinc:
            total += 1
    print(total)


def main():
    l = 0
    string, n = '', 0
    for line in sys.stdin:
        string = line.split('\n')[0]
    possible(string)

if __name__ == '__main__':
    main()
