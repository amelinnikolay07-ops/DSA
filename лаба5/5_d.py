
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

    def second_max(self):
        node = self.root
        parent = None

        # Ищем максимальный элемент
        while node.right is not None:
            parent = node
            node = node.right

        # Если у максимума есть левое поддерево,
        # ищем в нём самый правый элемент
        if node.left is not None:
            node = node.left

            while node.right is not None:
                node = node.right

            return node.data

        # Иначе второй максимум — родитель максимума
        return parent.data


tree = BinarySearchTree()

numbers = list(map(int, input().split()))

for x in numbers:
    if x == 0:
        break
    tree.insert(x)

print(tree.second_max())
