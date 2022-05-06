from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))


def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    diameter = 0

    def dfs(root):
        nonlocal diameter
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)

        diameter = max(left + right, diameter)

        return max(left, right) + 1
    dfs(root)
    return diameter


print(
    diameterOfBinaryTree(0, a)
)
