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

    def find_max(self):
        if self.root is None:
            return f'{str(None)}'
        return self._max_node(self.root).data

    def _max_node(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.data:
            node.left = self._delete(node.left, key)
        elif key > node.data:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            max_node = self._max_node(node.left)
            node.data = max_node.data

            node.left = self._delete(node.left, max_node.data)
        return node


if __name__ == '__main__':
    bst = BinarySearchTree()
    numbers = list(map(int, input().split()))
    for num in numbers:
        if num == 0:
            break
        bst.insert(num)
    mx1 = bst.find_max()
    bst.delete(mx1)
    mx2 = bst.find_max()
    print(mx2)
