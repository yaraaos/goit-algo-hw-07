class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_maximum(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.val

# Приклад використання
root = TreeNode(20)
root.left = TreeNode(10)
root.right = TreeNode(30)
root.right.right = TreeNode(40)

print(find_maximum(root))  # Виведе 40
