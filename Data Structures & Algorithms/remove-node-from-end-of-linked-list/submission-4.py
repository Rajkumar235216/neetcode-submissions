# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        slow = head
        fast = head
        if not slow.next:
            return None
        
        for i in range(n):
            print("fast.val", fast.val)
            fast = fast.next

        if not fast:
            print("if slow.val", slow.val)
            prev = None
            prev = slow.next
            slow.next = None
            slow = prev
            head = slow

        while fast and fast.next:
            print(fast.val)
            print(slow.val)
            slow = slow.next
            fast = fast.next
        
        # if fast:
        #     slow = slow.next
        # when fast is at null, means slow is at one step before n
        print("slow.val", slow.val)
        if fast and slow.next:
            slow.next = slow.next.next
        return head



