class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]= nums[i]+(len(nums)*(nums[nums[i]]%len(nums)))
        for i in range(len(nums)):
            nums[i]=nums[i]//len(nums)
        return nums
    
    """https://leetcode.com/problems/build-array-from-permutation/discuss/1315705/Python-C%2B%2B-and-Java-Solution-for-both-O(n)-and-O(1)-space-complexity."""
