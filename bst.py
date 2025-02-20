class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def insert_node(root, value):
    if value == root.value:
        return
    elif value < root.value:
        if root.left is not None:
            insert_node(root.left, value)
        else:
            new_node = Node(value)
            root.left = new_node
    else:
        if root.right is not None:
            insert_node(root.right, value)
        else:
            new_node = Node(value)
            root.right = new_node

def inorder(root):
    if root.left is not None:
        inorder(root.left)
    print(root.value, end=' ')
    if root.right is not None:
        inorder(root.right)

def levelorder(root):
    queue = []
    if root:
        queue.append(root)
    while len(queue) > 0:
        curr = queue.pop(0)
        print(curr.value, end=' ')
        if curr.left is not None:
            queue.append(curr.left)
        if curr.right is not None:
            queue.append(curr.right)
        

def main():
    root = Node(6)
    insert_node(root, 3)
    insert_node(root, 9)
    insert_node(root, 11)
    insert_node(root, 1)
    insert_node(root, 10)
    insert_node(root, 2)
    insert_node(root, 4)
    insert_node(root, 8)
    insert_node(root, 7)
    insert_node(root, 5)
    inorder(root)
    print()
    levelorder(root)

if __name__ == '__main__':
    main()