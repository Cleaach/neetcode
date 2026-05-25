# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        if not head.next:
            return head

        prev = head
        curr = head.next
        nxt = head.next.next

        prev.next = None

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            nxt = None if not nxt else nxt.next

        return prev