# link:   https://leetcode.com/problems/next-greater-element-i/
# explanation : https://leetcode.com/problems/next-greater-element-i/discuss/727678/Python-3-44ms-faster-than-92-using-stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=len(nums2)
        d={}
        for i in range(l):
            d[nums2[i]]=i
        stack=[0]
        ans=[-1]*l
        for i in range(1,l):
            if nums2[i]<=nums2[stack[-1]]:
                stack.append(i)
            else:
                while stack and nums2[i]> nums2[stack[-1]] :
                    x=stack.pop()
                    ans[x]=nums2[i]
                stack.append(i)
        ff=[]
        for i in nums1:
            ff.append(ans[d[i]])
        return ff
