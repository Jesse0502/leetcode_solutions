class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

a = ListNode(-1, ListNode(2, ListNode(8)))
b = ListNode(-3, ListNode(4, ListNode(7)))

from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list2.val > list1.val:
                tail.next = list1
                list1 = list1.next
                tail = tail.next
            else:
                tail.next = list2
                list2 = list2.next
                tail = tail.next
                
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next
                