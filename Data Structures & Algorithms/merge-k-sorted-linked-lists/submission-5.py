# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode):
    res = cur = ListNode(0)
    while l1 and l2:
        # print("a")
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        else:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        # break
    cur.next = l1 or l2
    return res.next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            merged_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                merged_list.append(mergeTwoLists(l1, l2))

            lists = merged_list

        return lists[0]

        # mid = len(lists) // 2
        # end = len(lists) - 1 # second last element
        # start = 0 # 2nd element of beginning
        # start_list = [lists[start]]
        # end_list = [lists[end]]
        # # print("mid before loop-- ", mid)
        
        # if len(lists) >= 3:
        #     while start < mid:
        #         # print("start - ", start, " mid -- ", mid, " end -- ", end)
        #         # print("start")
        #         start_list[0] = mergeTwoLists(start_list[0], lists[start + 1])
        #         if mid < end - 1:
        #             # print("end")
        #             end_list[0] = mergeTwoLists(end_list[0], lists[end - 1])
        #             end -= 1
        #         # print("break")
        #         # break
        #         start += 1
                
        # # for i in range(len(lists) - 1):
        # #     # print("here")
        # start_list[0] = mergeTwoLists(start_list[0], end_list[0])
        # return start_list[0] or None
        # print("length of lists -- ", len(lists))
        # return  lists[0] or None




        

        