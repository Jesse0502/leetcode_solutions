class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(4, TreeNode(3, TreeNode(2)))
b = TreeNode(3, TreeNode(2))

from typing import Optional

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        def isSameTree(root1, root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            else:
                return root1.val == root2.val and isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)
        
        def searchForSubTree(head, sub):
            if head is None:
                return False
            if isSameTree(head, sub):
                return True
            return searchForSubTree(head.left, sub) or searchForSubTree(head.right, sub)
        
        return searchForSubTree(root, subRoot)

Solution.isSubtree(Solution, a, b)