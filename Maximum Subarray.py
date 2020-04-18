#also known as kadane algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        meh=0
        msf=min(nums)
        for i in nums:
            meh=meh+i
            if meh<i:
                meh=i
            if msf < meh:
                msf=meh
        return msf 
        """Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle."""
