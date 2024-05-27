# Python code to demonstrate Implementing
# Queue using list and deque

from collections import deque

queue = ["A", "B", "C"]
queue.append("D")
queue.append("E")
print(queue)

# Removes the first item
print(queue.pop(0))
print(queue)


#To implement a queue, use collections.deque which was designed
# to have fast appends and pops from both ends.

queue = deque(["Sachin", "Saurav", "Rahul"])
print("Original queue:",queue)
queue.append("VVS")          # VVS arrives
queue.append("Anil")          # Anil arrives
print("After append the queue:",queue)
print("first pop : ",queue.popleft())
# The first to arrive now leaves
print("second pop : ",queue.popleft())
# The second to arrive now leaves

