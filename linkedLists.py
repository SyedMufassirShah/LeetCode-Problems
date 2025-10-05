# _____________________________________________________
# _____________________________________________________

    # SINGLY LINKEDLIST

# _____________________________________________________
# _____________________________________________________
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
        
# Declaring Nodes 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


# Linking the Nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Traversing the LinkedList
print("Traversal Started")
currentNode = node1
while currentNode:
    print(currentNode.data)
    currentNode = currentNode.next
    
print(node1.data)
print("Traversal Ended")        






# ____________________________________________________
# ____________________________________________________

#       DOUBLY LINKEDLIST

# ____________________________________________________
# ____________________________________________________

class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
        
dnode1 = DoublyNode(10)
dnode2 = DoublyNode(20)
dnode3 = DoublyNode(30)
dnode4 = DoublyNode(40)
dnode5 = DoublyNode(50)


# Linking Nodes

dnode1.next = dnode2
dnode2.next = dnode3
dnode3.next = dnode4
dnode4.next = dnode5

dnode2.prev = dnode1
dnode3.prev = dnode2
dnode4.prev = dnode3
dnode5.prev = dnode4

# Forward Traversal
temp = node1
print("Forward Traversal")
while temp:
    print(temp.data, end=" --> ")
    temp = temp.next
    
temp2 = dnode5
print("\nBackward Travarsal")
while temp2:
    print(" <-- " + str(temp2.data))
    temp2 = temp2.prev
    
    
# ________________________________________________________________
# ________________________________________________________________

                        # CIRCULAR LINKEDLIST
# ________________________________________________________________
# ________________________________________________________________

class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        


cnode1 = CNode(100)
cnode2 = CNode(200)
cnode3 = CNode(300)
cnode4 = CNode(400)
cnode5 = CNode(500)

cnode1.next = cnode2
cnode2.next = cnode3
cnode3.next = cnode4
cnode4.next = cnode5
cnode5.next = cnode1


cnode1.prev = cnode5
cnode2.prev = cnode1
cnode3.prev = cnode2
cnode4.prev = cnode3
cnode5.prev = cnode4

# # Circular Forward Traversal
# ctemp = cnode1
# print("Circular Forward Travarsal")
# while ctemp:
#     print(ctemp.data, end=" --> ")
#     ctemp = ctemp.next


# Circular Backward Travarsal
# ctemp = cnode5
# print("Circular Backward Travarsal")
# while ctemp:
#     print(temp2.data, end=" <-- ")
#     print(ctemp.data,  end=" --> ")
#     ctemp = ctemp.prev


data = b"hello"
data2 = bytearray(5)
print(data)
print(data2)
print(memoryview(data))