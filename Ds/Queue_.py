import queue
from collections import deque as de

que=queue.Queue()
que.put(1)
que.put(2)
que.put(3)
que.put(4)
que.put(5)
for i in range(que.qsize()):
    print(que.get())

d=de()
d.append(1)
d.append(2)
d.append(3)
print(d)
print(d.popleft())
print(d.pop())
print(d)