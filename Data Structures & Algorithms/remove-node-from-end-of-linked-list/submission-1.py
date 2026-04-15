# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        
        curr, tail = dummy, head
        i = 1
        while i < n:
            tail = tail.next
            i += 1
         
        while tail.next:
            tail = tail.next
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next