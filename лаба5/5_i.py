class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        node = self.root

        while True:
            if key < node.data:
                if node.left is None:
                    node.left = Node(key)
                    return
                node = node.left

            elif key > node.data:
                if node.right is None:
                    node.right = Node(key)
                    return
                node = node.right

            else:
                return

    def check_balance(self, node):
        if node is None:
            return 0

        left = self.check_balance(node.left)

        if left == -1:
            return -1

        right = self.check_balance(node.right)

        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)


tree = BinarySearchTree()

numbers = list(map(int, input().split()))

for x in numbers:
    if x == 0:
        break
    tree.insert(x)

if tree.check_balance(tree.root) == -1:
    print("NO")
else:
    print("YES")
