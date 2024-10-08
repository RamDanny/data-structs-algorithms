def lcs(string1, string2):
    #print(f'-{string1} {string2}-')
    if string1 == '' or string2 == '':
        return ''
    elif string1[-1] == string2[-1]:
        return lcs(string1[:-1], string2[:-1]) + string1[-1]
    else:
        a = lcs(string1[:-1], string2)
        b = lcs(string1, string2[:-1])
        return a if len(a) > len(b) else b

def main():
    string1, string2 = tuple(input('Enter strings: ').split(' '))
    print(lcs(string1, string2))

if __name__ == '__main__':
    main()
