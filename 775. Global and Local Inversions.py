#link  :-   https://leetcode.com/problems/global-and-local-inversions/
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        if not A:
            return False
        for i,c in enumerate(A):
            if abs(c-i)>1:
                return False
        return True
                
                
        
