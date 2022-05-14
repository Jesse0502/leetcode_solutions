from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15, TreeNode(7))))
b = TreeNode(3, None, TreeNode(2))

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:        
        def findFullNode(root, l):
            if (root != None):
                l.append(root.val)
                findFullNode(root.left, l)
                findFullNode(root.right, l)
            else:
                l.append(None)
            return l
        return findFullNode(p, []) == findFullNode(q, [])

print(
    Solution.isSameTree(Solution, a, b)
)
