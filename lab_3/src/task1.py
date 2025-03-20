class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

def find_successor(node: BinaryTree) -> BinaryTree:
    if node.right:
        return find_min_in_right(node.right)
    else:
        if node.parent is not None:
            return find_left_parent(node.parent)
        else:
            return None

def find_min_in_right(node: BinaryTree) -> BinaryTree:
    if node.left is None:
        return node
    return find_min_in_right(node.left)

def find_left_parent(node: BinaryTree) -> BinaryTree:
    if node.parent is None:
        return None
    if node.parent.left == node:
        return node.parent
    return find_left_parent(node.parent)

root = BinaryTree(10)
root.left = BinaryTree(5, parent=root)
root.right = BinaryTree(15, parent=root)
root.left.left = BinaryTree(3, parent=root.left)
root.left.right = BinaryTree(7, parent=root.left)
root.right.right = BinaryTree(20, parent=root.right)
root.right.right.left = BinaryTree(12, parent=root.right.right)

node = root.left.right
successor = find_successor(node)
print(successor.value)
        