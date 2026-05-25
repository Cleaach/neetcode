# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        one = l1
        two = l2
        dummy = ListNode()
        curr = dummy
        carry = 0
        
        while one or two:
            if one:
                first = one.val
            else:
                first = 0
            
            if two:
                second = two.val
            else:
                second = 0

            result = (first + second + carry) % 10
            carry = 1 if first + second + carry > 9 else 0
            
            curr.next = ListNode(val=result, next=None)
            curr = curr.next

            if one:
                one = one.next
            if two:
                two = two.next

        if carry != 0:
            curr.next = ListNode(val=1,next=None)
        
        return dummy.next