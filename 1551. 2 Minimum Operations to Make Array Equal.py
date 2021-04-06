class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        def sap(a,n):

            return ((n)*((2*a)+(n-1)*2))//2
        
        if n%2==1:
            return sap(2,n//2)
        else:
            return sap(1,n//2)
            
        
