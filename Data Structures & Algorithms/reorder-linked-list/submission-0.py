# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ans = head
        slow = head
        fast = head.next
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
        right_head = slow.next
        prev = None
        slow.next = None
        while right_head:
            nxt = right_head.next
            right_head.next = prev
            prev = right_head
            right_head = nxt
        right_head = prev
        while right_head and head :
            nxt = head.next
            head.next = right_head
            nxt_right = right_head.next
            right_head.next = nxt
            head = nxt
            right_head = nxt_right

