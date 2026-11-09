
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

    def inorder(self):
        stack = []
        node = self.root

        while stack or node is not None:
            while node is not None:
                stack.append(node)
                node = node.left

            node = stack.pop()
            print(node.data)

            node = node.right


tree = BinarySearchTree()

numbers = list(map(int, input().split()))

for x in numbers:
    if x == 0:
        break
    tree.insert(x)

tree.inorder()
