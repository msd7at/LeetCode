class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        l=len(nums)
        m=l//2
        i=0
        j=m+1
        ans=[]
        while i <=m and j<l:
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        while i<= m:
            ans.append(nums[i])
            i+=1
        while j<l:
            ans.append(nums[j])
            j+=1
        return ans
