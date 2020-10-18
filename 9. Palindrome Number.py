class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            y=10
            rev=0
            ori=x
            while x:
                rev=rev*10
                t=x%10
                rev=rev+t
                x=x//10
                
            if rev==ori:
                return True
            return False
