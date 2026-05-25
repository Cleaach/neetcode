# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # edge case
        if not head:
            return None
        
        # count length
        length = 0
        counter = head
        while counter:
            counter = counter.next
            length += 1
        
        # edge case
        if length == n:
            return head.next
        
        # 0-indexed node to remove
        order = length - n 

        prev = head
        curr = head.next
        nxt = head.next.next

        # navigate to node
        for _ in range(order - 1):
            prev = curr
            curr = nxt
            nxt = nxt.next
        
        # remove
        prev.next = nxt

        return head