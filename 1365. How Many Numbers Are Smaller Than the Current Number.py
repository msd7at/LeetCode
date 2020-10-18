class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=[0]*101
        for i in nums:
            l[i]+=1
        ans=[]
        for i in nums:
            j=0
            c=0
            while j < i:
                if l[j] !=0:
                    c=c+l[j]
                j+=1
            ans.append(c)
        return ans
            
