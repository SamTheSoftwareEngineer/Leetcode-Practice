# Nodes
# 1 - Value - anything, strings, ints, objects
# 2. The next node

class linkedlistNode:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode




 # 3 --> 7 --> 10
        
# node1 = linkedlistNode("3")
# node2 = linkedlistNode("7")
# node3 = linkedlistNode("10")

# node1.nextNode = node2 # node 1 --> node 2 "3" --> "7"
# node2.nextNode = node3

# currentNode = node1
# while True:
#     print (currentNode.value, "->"),
#     if currentNode.nextNode is None:
#         print("None")
#         break
#     currentNode = currentNode.nextNode


