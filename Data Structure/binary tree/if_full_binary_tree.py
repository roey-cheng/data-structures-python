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
            
    def is_full_node(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is not None and self.right is not None:
            return True
        return False

def is_full_tree(root):
    if not root.is_full_node():
        return False
    if root.is_full_node():
        left = root.left.is_full_node()
        right = root.right.is_full_node()
        return left and right


tree1 = BinaryTree(7, BinaryTree(2, BinaryTree(1), BinaryTree(5)), BinaryTree(9, None, BinaryTree(14)))
print(is_full_tree(tree1))