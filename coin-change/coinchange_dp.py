INF = 999999 # or some relevantly large value

def coinchange(amt, denoms):
    # Initialize DP array
    arr = [INF for i in range(amt + 1)]
    arr[0] = 0
    # Fill the array
    for denom in denoms:
        for i in range(denom, amt+1):
            arr[i] = min(arr[i], arr[i-denom] + 1)
    # Return final coin total
    if arr[amt] == INF:
        return -1
    return arr[amt]

def main():
    denoms = [1, 6, 10]
    amt = 12
    print(coinchange(amt, denoms))

if __name__ == '__main__':
    main()