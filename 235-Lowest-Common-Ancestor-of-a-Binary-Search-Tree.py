from tkinter.tix import Tree


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

a = TreeNode(9, TreeNode(3, TreeNode(8), TreeNode(9), TreeNode(3)))

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr
    
Solution.lowestCommonAncestor(a)