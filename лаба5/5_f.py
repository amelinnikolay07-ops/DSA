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

    def leaves(self):
        res = []
        self._leaves(self.root, res)
        return res

    def _leaves(self, node, result):
        if node is None:
            return
        self._leaves(node.left, result)
        if node.left is None and node.right is None:
            result.append(node.data)
        self._leaves(node.right, result)
        return result


if __name__ == '__main__':
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num == 0:
            break
        bst.insert(num)

    res = bst.leaves()
    print(*res, sep='\n')
