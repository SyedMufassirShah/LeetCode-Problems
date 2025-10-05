# We will be shown all the properties of list by our IDE but we have to make sure we have to only use the properties of Stack not the list because the stack is a list by nature and we have to treat it as a Stack and will only LIFO order and our stack will support only 3 operations
# Order --> LIFO
# Operations supported by stack 
                #  append()
                #  pop()
                #  peek() --> Help us to see whats on the top in the stack

stack = []
stack.append("Hello")
print(stack)
stack.append(55)
print(stack)
print(stack[-1]) #  peek method to see whats on the top of the stack
stack.append("World")
print(stack[0])
print(stack[1])
print(stack[2])
print(stack)
stack.pop(-1)
print(stack)
stack.pop(0)
print(stack)