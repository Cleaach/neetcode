# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        
        if not list1:
            return list2

        new = ListNode(val=min(list1.val,list2.val),next=None)
        curr = new

        one = list1.next if list1.val < list2.val else list1
        two = list2 if list1.val < list2.val else list2.next
            
        while True:
            if not one:
                curr.next = two
                break
            if not two:
                curr.next = one
                break

            if one.val < two.val:
                curr.next = ListNode(val=one.val, next=None)
                one = one.next
            else:
                curr.next = ListNode(val=two.val, next=None)
                two = two.next
            
            curr = curr.next
        
        return new