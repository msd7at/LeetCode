class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return
        
        # Step 1: Find middle element
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow, fast = slow.next, fast.next.next
        # separating both the lists
        prev.next = None
        
        # Step 2: Reverse second half
        prev, curr = None, slow
        while curr:
            temp, curr.next = curr.next, prev
            prev, curr = curr, temp
        
        # Step 3: Merge both lists
        h1, h2 = head, prev
        # As size of second half >= size of first half
        while h2:
            temp, h1.next = h1.next, h2
            h1, h2 = h2, temp
