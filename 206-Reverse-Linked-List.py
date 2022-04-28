class Solution:
    def reverseList(self, head):
        if head is None: return head
        
        prev = None
        curr = head
        
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            
        return prev
        