class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=len(nums)
        ans=[0]*l
        ans[0]=1
        for i in range(1,l):
            ans[i]=ans[i-1]*nums[i-1]
        r=1
        for i in range(l-1,-1,-1):
            ans[i]=r*ans[i]
            r=r*nums[i]
        return ans
