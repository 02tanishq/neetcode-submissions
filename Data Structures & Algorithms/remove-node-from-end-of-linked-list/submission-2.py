# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        if head.next == None :
            return None


        prev = None
        curr = head
        k = 0
        length = 1
        slow = head
        fast = head.next

        while fast and fast.next :
            slow = slow.next
            fast= fast.next.next
            length += 1
        if fast == None :
            total_len = length * 2 - 1
        else:
            total_len = length * 2            

        left_distance = total_len - n 

        if total_len  == n :
            nxt = curr.next
            curr.next = None
            return nxt

        
        while curr:
            nxt = curr.next
            
            if k == left_distance :
                prev.next = nxt
                curr.next = None 
                return head
            
            prev = curr
            curr = nxt
            k += 1
            
