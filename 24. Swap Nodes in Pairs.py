# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(0,head)
        d=dum
        
        while d.next and d.next.next:
            
            cu = d.next
            sec = cu.next
            
            d.next = sec
            
            cu.next = sec.next
            
            sec.next = cu 
            
            d= cu
        
        return dum.next
            
        
        
