from random import randint
import queue

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

    def balanced(self):
        return self._balanced(self.root)

    def _balanced(self, node):
        if node is None:
            return True
        left_h = self._height(node.left)
        right_h = self._height(node.right)
        if ((abs(left_h - right_h) <= 1) and
            self._balanced(node.left) and
            self._balanced(node.right)):
            return True
        return False

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))





if __name__ == '__main__':
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num == 0:
            break
        bst.insert(num)
    res = bst.balanced()
    if res:
        print('YES')
    else:
        print('NO')
