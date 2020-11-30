class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2==1:
            m=nums[len(nums)//2]
            ans=0
            for i in nums:
                ans+=abs(m-i)
            return ans
        else:
            m1=nums[len(nums)//2]
            m2=nums[(len(nums)//2)-1]
            ans1=0
            ans2=0
            for i in nums:
                ans1+=abs(m1-i)
                ans2+=abs(m2-i)
            return min(ans1,ans2)
                
