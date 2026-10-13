class Deque:
    def __init__(self):
        self.data = []

    def push_front(self, n):
        self.data.insert(0, n)
        return 'ok'

    def push_back(self, n):
        self.data.append(n)
        return 'ok'

    def pop_front(self):
        if not self.data:
            return 'error'
        return self.data.pop(0)

    def pop_back(self):
        if not self.data:
            return 'error'
        return self.data.pop()

    def front(self):
        if not self.data:
            return 'error'
        return self.data[0]

    def back(self):
        if not self.data:
            return 'error'
        return self.data[-1]

    def size(self):
        return len(self.data)

    def clear(self):
        self.data.clear()
        return 'ok'


deq = Deque()

while True:
    command = input().split()

    if command[0] == 'push_front':
        print(deq.push_front(int(command[1])))

    elif command[0] == 'push_back':
        print(deq.push_back(int(command[1])))

    elif command[0] == 'pop_front':
        print(deq.pop_front())

    elif command[0] == 'pop_back':
        print(deq.pop_back())

    elif command[0] == 'front':
        print(deq.front())

    elif command[0] == 'back':
        print(deq.back())

    elif command[0] == 'size':
        print(deq.size())

    elif command[0] == 'clear':
        print(deq.clear())

    elif command[0] == 'exit':
        print('bye')
        break
