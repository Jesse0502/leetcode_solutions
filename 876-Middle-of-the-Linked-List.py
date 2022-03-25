
class Solution:
    def middleNode(self, head):
        t = head
        h = head
        
        while h != None and h.next:
            
            h = h.next.next
            t = t.next
        print(f'{t.val}, {t.next.val}...')
        return t

class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

a = ListNode(1,ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))

Solution.middleNode("",a)