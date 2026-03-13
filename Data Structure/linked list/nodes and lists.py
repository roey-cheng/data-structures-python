class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class Linked_List():
    def __init__(self):
        self.head == None

    def is_empty(self):
        return self.head == None
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.get_next()
        return count

    def add(self, item):
        new_node = Node(item)
        new_node.set_next = self.head
        self.head = new_node

    def search(self, item):
        curr = self.head
        while curr is not None:
            if item == curr.get_data():
                return True
            else:
                curr = curr.get_next()
        return False

# traversal of nodes
current = head
while current:
    if condition:
        insert/delete after current
    current = current.next

"""Handling Edge Cases
Empty Chain: Always check whether the starting node is None before beginning any operation. This prevents errors and ensures robustness.
Last Node: The last node in the chain has its next attribute set to None. Make sure to handle this so you don’t accidentally try to access an attribute of a None object."""

"""Summary

Always start by checking for None (empty list or end of list).
Use loops or recursion to traverse nodes.
Use node attributes directly to read or modify data.
Choose the right return type for your function.
Try writing both iterative and recursive versions of your functions to deepen your understanding."""