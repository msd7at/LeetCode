class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rev(i,j,nums):
            while i < j :
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        n=len(nums)
        i=n-2
        while i>=0 :
            if nums[i]<nums[i+1]:
                x=nums[i]
                idd=i
                break
            i-=1
        if i==-1:
            rev(0,n-1,nums)
        else:
            i=n-1
            while i >=0 and nums[i]<=x:
                i-=1

            nums[i],nums[idd]=nums[idd],nums[i]
            rev(idd+1,len(nums)-1,nums)
