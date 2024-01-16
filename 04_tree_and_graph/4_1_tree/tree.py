class TreeNode:
    def __init__(self, data):
        self.value = data
        self.children: list = []


class BinaryTreeNode:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None