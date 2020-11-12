class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
    
        def reve(a,b,nums):
            while a<b:
                nums[a],nums[b]=nums[b],nums[a]
                a+=1
                b-=1
        i=len(nums)-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i<0:
            reve(i+1,len(nums)-1,nums)
        else:
            k=len(nums)-1
            while k >=0 and nums[k]<=nums[i]:
                k-=1
            nums[k],nums[i]=nums[i],nums[k]
            reve(i+1,len(nums)-1,nums)
            
            
