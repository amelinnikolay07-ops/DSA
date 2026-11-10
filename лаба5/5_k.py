
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Добавление элемента
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

    # Поиск минимального элемента >= key
    def next(self, key):
        node = self.root
        answer = -1

        while node is not None:
            if node.data >= key:
                answer = node.data
                node = node.left
            else:
                node = node.right

        return answer


tree = BinarySearchTree()

n = int(input())

last_answer = 0
last_was_query = False

for _ in range(n):
    command, x = input().split()
    x = int(x)

    if command == "+":
        if last_was_query:
            x = (x + last_answer) % 10**9

        tree.insert(x)
        last_was_query = False

    else:
        last_answer = tree.next(x)
        print(last_answer)
        last_was_query = True
