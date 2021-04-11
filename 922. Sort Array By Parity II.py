class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        e=0
        o=1
        l=len(nums)
        while e<l and o<l:
            while e<l and o<l and nums[e]%2==0 :
                e+=2
            while e<l and o<l and nums[o]%2==1:
                o+=2
            if nums[o]%2==0 and nums[e]%2==1:
                nums[o],nums[e]=nums[e],nums[o]
            o+=2
            e+=2
        return nums
            
