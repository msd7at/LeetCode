class Solution:
    def distributeCandies(self, candies: int, nn: int) -> List[int]:
        a=[0]*nn
        k=0
        i=0
        s=0
        l=candies - s
        while s<candies:
            i=0
            while i<nn:
                l=candies - s
                k+=1
                if l>k:
                    a[i]+=k
                else:
                    a[i]+=l   
                i+=1
                s=s+k
                if s>=candies:
                    return a
        return a
            
            
