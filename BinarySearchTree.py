class BinarySearchTree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    def insert_left(self, new_data):
        if self.left == None:
            self.left = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, left=self.left)
            self.left = tree
    def insert_right(self, new_data):
        if self.right == None:
            self.right = BinarySearchTree(new_data)
        else:
            tree = BinarySearchTree(new_data, right=self.right)
            self.right = tree
    def get_left(self):
        return self.left
    def get_right(self):
        return self.right
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def insert(self, new_data):
        if new_data == self.data:
            return
        elif new_data < self.data:
            if self.left == None:
                self.left = BinarySearchTree(new_data)
            else:
                self.left.insert(new_data)
        else:
            if self.right == None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(new_data)
    def search(self, find_data):
        if self.data == find_data:
            return True
        elif find_data < self.data and self.left != None:
            return self.left.search(find_data)
        elif find_data > self.data and self.right != None:
            return self.right.search(find_data)
        else:
            return False
