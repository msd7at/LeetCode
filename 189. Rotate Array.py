class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=k%l
        def rev(i,j):
            while i<j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        rev(0,l-1)
        rev(0,k-1)
        rev(k,l-1)
