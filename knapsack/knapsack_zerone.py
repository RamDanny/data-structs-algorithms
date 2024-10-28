import copy

def knapsack_zerone(weight, items):
    table = [[0 for j in range(weight+1)] for i in range(len(items)+1)]
    for i in range(1, len(items)+1):
        for w in range(1, weight+1):
            if w < items[i-1][0]:
                table[i][w] = table[i-1][w]
            else:
                new = table[i-1][w-items[i-1][0]] + items[i-1][1]
                if new >= table[i-1][w]:
                    table[i][w] = new
                else:
                    table[i][w] = table[i-1][w]
    return (table[-1][weight])

def main():
    items = [[10, 5], [5, 2], [9, 4], [6, 3]]
    print(knapsack_zerone(int(input()), items))

if __name__ == '__main__':
    main()