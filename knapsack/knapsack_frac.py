def knapsack_frac(weight, items):
    picked = []
    arr = [[items[i][1]/items[i][1], i] for i in range(len(items))]
    arr.sort(reverse=True, key=lambda x: x[0])
    w, value = weight, 0
    for item in arr:
        if w <= 0:
            break
        if w >= items[item[1]][0]:
            value += items[item[1]][1]
            w -= items[item[1]][0]
            picked.append(item[1])
        else:
            value += w * items[item[1]][1] / items[item[1]][0]
            w = 0
            picked.append(item[1])
    return (picked, value)

def main():
    items = [[10, 5], [5, 2], [9, 4], [6, 3]]
    print(knapsack_frac(int(input()), items))

if __name__ == '__main__':
    main()
