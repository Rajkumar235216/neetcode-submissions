# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur1 = head
        cur2 = head
        while cur1 and cur2:
            cur1 = cur1.next
            if cur2.next is None:
                return False
            cur2 = cur2.next.next
            if cur1 == cur2:
                return True
            if cur1 is None or cur2 is None:
                return False
        return False