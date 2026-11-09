
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

    def count(self):
        if self.root is None:
            return 0

        stack = [self.root]
        result = 0

        while stack:
            node = stack.pop()
            result += 1

            if node.left is not None:
                stack.append(node.left)

            if node.right is not None:
                stack.append(node.right)

        return result


tree = BinarySearchTree()

numbers = list(map(int, input().split()))

for x in numbers:
    if x == 0:
        break
    tree.insert(x)

print(tree.count())
