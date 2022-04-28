class Solution:
    def isPalindrome(self, head) -> bool:
        if head.next == None:
            return True
        a = []
        node = head
        while not node == None:
            a.append(node.val)
            node = node.next
        if not a == list(reversed(a)):
            return False
        else:
            return True
        
        
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
a = ListNode(1,ListNode(0,ListNode(0, None)))

print(Solution.isPalindrome("",a))