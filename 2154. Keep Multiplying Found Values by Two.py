class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        
        # def srch(nums,key):
        #     for i in nums:
        #         if i == key:
        #             return i
        #     return -1
        nums.sort()
        def srch (nums,key):
            
            l=0
            mid=0
            r=len(nums)-1
            while l <= r:
                mid= (l+r)//2
                if nums[mid] < key:
                    l = mid +1
                elif nums[mid] > key :
                    r = mid -1
                
                else:
                    return mid
            return -1
                
                
        
        while True:
            ans = srch(nums,original)
            # print(ans)
            if ans == -1:
                return original
            original = 2 * original
            # print(original)
        
