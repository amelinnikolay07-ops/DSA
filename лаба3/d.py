class Queue:
    def __init__(self):
        self.queue = []

    def push(self, n):
        self.queue.append(n)
        return 'ok'

    def pop(self):
        if not self.queue:
            return 'error'
        return self.queue.pop(0)

    def front(self):
        if not self.queue:
            return 'error'
        return self.queue[0]

    def size(self):
        return len(self.queue)

    def clear(self):
        self.queue.clear()
        return 'ok'


queue = Queue()

while True:
    command = input().split()

    if command[0] == 'push':
        print(queue.push(int(command[1])))

    elif command[0] == 'pop':
        print(queue.pop())

    elif command[0] == 'front':
        print(queue.front())

    elif command[0] == 'size':
        print(queue.size())

    elif command[0] == 'clear':
        print(queue.clear())

    elif command[0] == 'exit':
        print('bye')
        break
