class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        if key < node.data:
            node.left = self._insert(node.left, key)
        elif key > node.data:
            node.right = self._insert(node.right, key)
        return node

    def order_up(self):
        return self._order_up(self.root)

    def _order_up(self, node):
        if node is None:
            return []
        return self._order_up(node.left) + [node.data] + self._order_up(node.right)



if __name__ == '__main__':
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num == 0:
            break
        bst.insert(num)

    res = bst.order_up()
    print(*res, sep='\n')
