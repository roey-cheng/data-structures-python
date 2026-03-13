class BinaryTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, left=self.left)
            self.left = t

    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinaryTree(new_data)
        else:
            t = BinaryTree(new_data, right=self.right)
            self.right = t

    def get_left(self):
        return self.left

    def get_right(self):
        return self.right

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right

def create_tree_from_nested_list(node_list):
    if node_list:
        result = BinaryTree(node_list[0])
        left = create_tree_from_nested_list(node_list[1])
        right = create_tree_from_nested_list(node_list[2])
        if left != None:
            result.set_left(left)
        if right != None:
            result.set_right(right)
        return result       

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        print("New node on stack")
        self.items.append(item)
    def pop(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items.pop()
    def peek(self):
        if self.is_empty():
            raise IndexError('ERROR: The stack is empty!')
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)[:-1] + ' <-'	
        


tree1 = create_tree_from_nested_list([5, None, None])
tree2 = create_tree_from_nested_list([4, [2, None, [3, None, None]], [7, None, None]])
tree3 = create_tree_from_nested_list([4, None, [7, None, [10, None, [12, None, None]]]])
tree4 = create_tree_from_nested_list([4, [2, [1, [0, None, None], None], None], None])
tree5 = create_tree_from_nested_list([5, [2, [1, None, None], None], [7, None, None]])
tree6 = create_tree_from_nested_list([5, [2, None, [3, None, None]], [7, None, None]])
tree7 = create_tree_from_nested_list([8, [3, None, [4, None, None]], [10, None, [11, None, None]]])
tree8 = create_tree_from_nested_list([7, [3, [1, None, None], [4, None, None]], [10, None, [11, None, None]]])
tree9 = create_tree_from_nested_list([7, [3, [1, [0, None, None], [2, None, None]], [4, None, None]], [9, [8, None, None], [11, None, None]]])

