# data = []
# data.append(5)
# data.append(10)
# data.append(15)
# data.append(20)

# print(data)

# data.pop()
# data.pop()

# print(data)


# element = data.pop()

# print(element)
# print(data)

class Stack:
    def __init__(self):
        self._data = []

    def push(self, data):
        self._data.append(data)

    def pop(self):
        return self._data.pop()
    
    def peek(self):
        return self._data[len(self._data) - 1]

stack = Stack()
stack.push(10)
print(stack.peek())



