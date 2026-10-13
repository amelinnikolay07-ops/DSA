class Stack:
    def __init__(self):
        self.stack = []

    def push(self, n):
        self.stack.append(n)
        return 'ok'

    def pop(self):
        if not self.stack:
            return 'error'
        return self.stack.pop()

    def back(self):
        if not self.stack:
            return 'error'
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def clear(self):
        self.stack.clear()
        return 'ok'


stack = Stack()

while True:
    command = input().split()

    if command[0] == 'push':
        print(stack.push(int(command[1])))

    elif command[0] == 'pop':
        print(stack.pop())

    elif command[0] == 'back':
        print(stack.back())

    elif command[0] == 'size':
        print(stack.size())

    elif command[0] == 'clear':
        print(stack.clear())

    elif command[0] == 'exit':
        print('bye')
        break
