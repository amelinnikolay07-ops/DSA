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

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.data == key:
            return True
        if key < node.data:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def order_down(self):
        return self._order_down(self.root)

    def _order_down(self, node):
        if node is None:
            return []
        return self._order_down(node.right) + [node.data] + self._order_down(node.left)

    def next(self, key):
        return self._next(self.root, key)

    def _next(self, node, key):
        candidate = None
        while node is not None:
            if node.data >= key:
                candidate = node.data
                node = node.left
            else:
                node = node.right
        if candidate is None:
            return -1
        return candidate



if __name__ == '__main__':
    bst = BinarySearchTree()
    n = int(input())
    prev_op = None
    prev_res = None
    for _ in range(n):
        op = input().split()

        if op[0] == '?':
            prev_res = bst.next(int(op[1]))
            print(prev_res)
        else:
            if prev_op is None or (prev_op == '+'):
                bst.insert(int(op[1]))
            else:
                bst.insert((int(op[1]) + prev_res)%(10**9))


        prev_op = op[0]

