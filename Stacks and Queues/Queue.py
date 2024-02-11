from collections import deque

data = deque()

data.append("Caleb")
element = data.popleft()
print(element)
print(data)
