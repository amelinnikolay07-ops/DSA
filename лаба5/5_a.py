import sys

sys.setrecursionlimit(10000)


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Вставка элемента
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

    # Поиск элемента
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

    # Поиск максимального элемента
    def _max_node(self, node):
        while node.right is not None:
            node = node.right

        return node

    # Удаление элемента
    def delete(self, key):
        if not self.search(key):
            return False

        self.root = self._delete(self.root, key)
        return True

    def _delete(self, node, key):
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

    # Вывод дерева
    def print_tree(self):
        result = []
        self._print_tree(self.root, 0, result)
        return result

    def _print_tree(self, node, level, result):
        if node is None:
            return

        self._print_tree(node.left, level + 1, result)

        result.append("." * level + str(node.data))

        self._print_tree(node.right, level + 1, result)


if __name__ == "__main__":
    tree = BinarySearchTree()

    for line in sys.stdin:
        command = line.split()

        if not command:
            continue

        operation = command[0]

        if operation == "ADD":
            key = int(command[1])

            if tree.search(key):
                print("ALREADY")
            else:
                tree.insert(key)
                print("DONE")

        elif operation == "DELETE":
            key = int(command[1])

            if tree.delete(key):
                print("DONE")
            else:
                print("CANNOT")

        elif operation == "SEARCH":
            key = int(command[1])

            if tree.search(key):
                print("YES")
            else:
                print("NO")

        elif operation == "PRINTTREE":
            for element in tree.print_tree():
                print(element)
