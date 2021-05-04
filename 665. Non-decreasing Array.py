class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums)<=2:
            return True
        nc=(1 if nums[0]>nums[1] else 0)
        for i in range(1,len(nums)-1):
            if nums[i]>nums[i+1]:
                if nums[i-1]>nums[i+1]:
                    nums[i+1]=nums[i]
                if nc==1:
                    return False
                nc+=1
        return True
