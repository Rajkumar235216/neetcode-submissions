# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # using fast pointer and slow pointers, divide linked list in half
        # sort the 2nd half list by reversing the links so that head points to last element
        # run loop, where pick element from each linked list alternatively
        slow, fast = head, head.next

        # run the loop until fast reaches null
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # as fast is null, means slow is at middle
        # make slow.next head as null, so that linked 
        # list get divided
        head2 = slow.next
        slow.next = None

        # now 2 linked list, one started with head, 
        # another with head2
        # sort the 2nd list
        prev = None
        while head2:
            temp_node = head2.next
            head2.next = prev
            prev = head2
            head2 = temp_node
        # now 2nd linked list starts with prev as head as it is sorted
        # now iterate through both list and pick alternate
        res = fs = ListNode()
        while prev:
            # pick 1st element
            print("head -- ", head.val)
            res.next = head
            res = res.next
            head = head.next

            # pick 2nd element
            print("prev -- ", prev.val)
            res.next = prev
            res = res.next
            prev = prev.next
        
        if head:
            res.next = head
            res = res.next

        # return res