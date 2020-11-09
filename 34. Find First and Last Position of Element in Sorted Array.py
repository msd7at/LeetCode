class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        s=0
        l=0
        ff=0
        for i in nums:
            
            if i<target:
                s+=1
            elif i>target:
                l+=1
            else:
                ff=1
        if ff:
            return [s,len(nums)-l-1]
        else:
            return [-1,-1]
