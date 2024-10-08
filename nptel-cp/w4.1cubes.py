import sys

sys.stdin = open('in.txt', 'r')
sys.stdout = open('out.txt', 'w')

q = int(input())
state = []
sets = dict()

for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        state.append(query[1]) # add cube to items
        # add cube under the corr colour
        if query[1] not in sets:
            sets[query[1]] = [len(state)-1]
        else:
            sets[query[1]].append(len(state)-1)
    elif query[0] == 2:
        # convert cube from col1 to col2
        if query[1] not in sets:
            continue
        elif not sets[query[1]]:
            continue
        else:
            for cube in sets[query[1]]:
                state[cube] = query[2] # converting ith cube
            if query[2] not in sets:
                sets[query[2]] = []
                sets[query[2]].extend(sets[query[1]])
            else:
                sets[query[2]].extend(sets[query[1]]) # updating colours
            sets[query[1]] = []
    # print(query, state, sets)

for i in range(len(state)):
    if i == len(state)-1:
        print(state[i], end='')
    else:
        print(state[i], end=' ')
