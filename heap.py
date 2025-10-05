import heapq

hq = []

heapq.heappush(hq, 5)
heapq.heappush(hq, 6)
heapq.heappush(hq, 7)
print(hq)
print(heapq.heappop(hq))
print(hq)
print(heapq.heappop(hq))
print(hq)