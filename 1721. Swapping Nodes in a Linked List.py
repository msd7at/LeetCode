class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l=head
        r=head
        for i in range(k-1):
            l= l.next
        
        tail=l
        
        while tail.next:
            tail=tail.next
            r=r.next
        
        l.val,r.val=r.val,l.val
        
        return head
