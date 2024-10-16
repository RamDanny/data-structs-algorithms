def coinchange(amt, denoms, denom=0):
    numcoins = amt // denoms[denom]
    print(f'{numcoins} x {denoms[denom]}', end=' ')
    if amt % denoms[denom] > 0:
        if denom < len(denoms)-1:
            coinchange(amt % denoms[denom], denoms, denom+1)

def main():
    denoms = [50, 25, 10, 5, 1]
    coinchange(int(input()), denoms)

if __name__ == '__main__':
    main()
