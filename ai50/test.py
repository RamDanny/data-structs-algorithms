class gg():
    def __init__(self, x):
        self.x = x

def main():
    d = dict()
    name = input("Enter name: ")
    id = input("Enter id: ")
    d[name] = {id}
    print(d)
    g = gg(id)
    print(g.x)
    x = [[],[],[]]
    print(x == [[],[],[]])

if __name__ == "__main__":
    main()
