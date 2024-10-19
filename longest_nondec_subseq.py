table = []

def li(string, i, n):
    global table
    if i == 0:
        temp = [string[i]]
        table[i] = temp
        #return temp
    else:
        index = -1
        li1 = table[i-1]
        for j in range(len(li1)-1, -1, -1):
            if li1[j] <= string[i]:
                index = j
                break
        if index > -1:
            temp = li1[:index+1]
            temp.append(string[i])
            table[i] = temp
            #return temp
        else:
            temp = [string[i]]
            table[i] = temp
            #return temp

def lndss(string):
    global table
    for i in range(len(string)):
        li(string, i, len(string))
    m = []
    for row in table:
        if len(row) > len(m):
            m = row
    return m

def main():
    global table
    string = list(map(int, input().split(' ')))
    table = [list() for i in range(len(string))]
    print(lndss(string))

if __name__ == '__main__':
    main()
