from collections import deque


queue = deque()

queue.append(5)
queue.append(6)
queue.append(7)
print(queue)
queue.popleft()
print(queue)
