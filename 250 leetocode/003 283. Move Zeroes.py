class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z = 0
        i = 0
        l = len(nums)
        while i < l and z < l:
            if nums[i] !=0:
                nums[z],nums[i] = nums[i],nums[z]
                z+=1
            i+=1
                
