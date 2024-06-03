class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_minimum(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.left.left = TreeNode(5)

print(find_minimum(root))  # Виведе 5
