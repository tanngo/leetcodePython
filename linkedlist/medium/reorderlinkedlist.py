# https://leetcode.com/problems/reorder-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        The logic is as below:
        Find the second middle element and then sort the second half
        """
        if not head:
            return
        # find the middle element
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        # reverse the second half
        prev = None
        cur = slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        # rearrange head : 1->2->3 ,prev: 6->5->4
        first,second = head,prev
        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
        



        
        