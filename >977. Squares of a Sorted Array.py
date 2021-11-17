class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i=0
        j=0
        l=len(nums)-1
        while nums[i]<0 and i<l  :
            i+=1
        j=i
        i=i-1
        # print(i,j)
        ans=[]
        while j<=l and i>=0:
            if nums[j]==0:
                ans.append(0)
                j+=1
            elif abs(nums[i]) <= nums[j]:
                ans.append(nums[i]**2)
                i-=1
            else:
                ans.append(nums[j]**2)
                j+=1
        while i>=0:
            ans.append(nums[i]**2)
            i-=1
        while j<=l:
            ans.append(nums[j]**2)
            j+=1
        return ans
