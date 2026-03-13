class BinaryTree:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
    
    def insert_left(self, new_data):
        if self.left is None:
            self.left = BinaryTree(new_data)
        else:
            subtree = BinaryTree(new_data, self.left)
            self.left = subtree

    def insert_right(self, new_data):
        if self.right is None:
            self.right = BinaryTree(new_data)
        else:
            subtree = BinaryTree(new_data, self.right)
            self.right = subtree

    def get_left(self):
        return self.left
    
    def get_right(self):
        return self.right
    
    def set_data(self, data):
        self.data = data
    
    def get_data(self):
        return self.data
    
