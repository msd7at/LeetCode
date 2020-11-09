class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        cls=float("inf")
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            s=nums[i]
            while j<k:
                if abs(target-(s+nums[j]+nums[k]))<abs(cls):
                    cls= target-(s+nums[j]+nums[k])
                if  s+nums[j]+nums[k] < target :
                    j+=1
                else:
                    k-=1
            if cls==0:
                break
               
        return target-cls
            
                
            
