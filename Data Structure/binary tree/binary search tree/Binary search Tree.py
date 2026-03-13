class BinarySearchTree:
    def __init__(self, data, left = None, right = None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def insert(self, new_data):
        if new_data == self.data:
            return
        elif new_data < self.data:
            if self.left is None:
                self.left = BinarySearchTree(new_data)
            else:
                self.left.insert(self.left, new_data)
        else:
            if self.right is None:
                self.right = BinarySearchTree(new_data)
            else:
                self.right.insert(self.right, new_data)

    def search(self, find_data):
        if self.data == find_data:
            return True
        elif self.data > find_data and self.left is not None:
            return self.left.search(find_data)
        elif self.data < find_data and self.right is not None:
            return self.right.search(find_data)
        else:
            return False
        

def reconstruct_tree(inorder_sequence, preorder_sequence):
    if inorder_sequence == []:
        return None
    else:
        root = preorder_sequence[0]
        inorder_i = inorder_sequence.index(root)
        inorder_left = inorder_sequence[:inorder_i]
        inorder_right = inorder_sequence[inorder_i + 1:]
        preorder_left = preorder_sequence[1:len(inorder_left) + 1]
        preorder_right = preorder_sequence[len(inorder_left) + 1:]
        return [root] + [reconstruct_tree(inorder_left, preorder_left)] + [reconstruct_tree(inorder_right, preorder_right)]