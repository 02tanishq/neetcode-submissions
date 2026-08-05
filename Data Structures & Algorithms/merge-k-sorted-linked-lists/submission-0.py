# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    

    def merge_two(seelf , l1: List[Optional[ListNode]] , l2 : List[Optional[ListNode]] ) -> Optional[ListNode]:
            dummy = ListNode(0)
            tail  = dummy
            temp1  = l1
            temp2 = l2 
            while temp1 and temp2:
                if temp1.val <= temp2.val :
                    tail.next = temp1
                    temp1 = temp1.next
                else :
                    tail.next = temp2
                    temp2 = temp2.next
                tail = tail.next
            if temp1:
                tail.next = temp1
            if temp2 :
                tail.next = temp2
            return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode] :

        if len(lists) == 0:
            return None

        finalhead = lists[0]

        for i in range(1,len(lists)):
            curhead = lists[i]
            finalhead = self.merge_two(finalhead , curhead)
        return finalhead
        


 