class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        l=len(nums)
        for i in range(l):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        for i in d:
            if target-i in d :
                if i==target-i and len(d[i])>1:
                    return [d[i][0],d[i][1]]
                elif i==target-i and len(d[i])==1:
                    pass
                else:
                    return [d[i][0],d[target-i][0]]
 """
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
