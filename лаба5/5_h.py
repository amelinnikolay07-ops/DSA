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

    def branches(self):
        res = []
        self._branches(self.root, res)
        return res

    def _branches(self, node, result):
        if node is None:
            return
        self._branches(node.left, result)
        if (node.left and node.right is None) or (node.left is None and node.right):
            result.append(node.data)
        self._branches(node.right, result)



if __name__ == '__main__':
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num == 0:
            break
        bst.insert(num)
    res = bst.branches()
    print(*res, sep='\n')
