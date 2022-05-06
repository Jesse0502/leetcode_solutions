from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None: return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root