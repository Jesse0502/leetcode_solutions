from tkinter.tix import Tree
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(1, TreeNode(2, TreeNode(6), TreeNode(8)), TreeNode(9, TreeNode(7, TreeNode(0))))


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None: return False
            left = dfs(root.left)
            right = dfs(root.right)

            if not left and not right:
                return True
            elif left and right:
                return True
            else:
                return False
        return dfs(root)


print(
    Solution.isBalanced(0, a)
)
