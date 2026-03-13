from collections import deque
linkedlist = deque()
linkedlist.append(1)
linkedlist.append(2)
linkedlist.append(3)
print(linkedlist)
linkedlist.insert(2,99)
print(linkedlist)
element = linkedlist[2]
print(element)
index = linkedlist.index(99)
print(index)
linkedlist[2] = 88
print(linkedlist)
linkedlist.remove(88)
print(linkedlist)
length = len(linkedlist)
print(length)