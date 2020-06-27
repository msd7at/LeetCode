# link:-https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
# explanation :- https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/discuss/708731/Python-3-Faster-than-100-Explanation
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=len(nums)
        ar=[]
		
        c=0 # it will count 1's
        su=sum(nums)
		# if all element are 1
        if su==l:
            return l-1
		#if all element are 0
        if su==0:
            return su
			
        for i in nums:
			# if 1 increment c
            if i==1:
                c+=1
            else:
                if c==0:
					# if list is empty or previous element is not 0
					# if two or more consecutive avoid that condition by pass
                    if ar==[] or ar[-1]==0:
                        pass
					# else append c to ar
                    else:
                        ar.append(c)
                else:
                    ar.append(c)
                    c=0
		# if last element of nums is 1 then append c to ar as  in the above for loop we can not append 
		#c to ar when i==1 and we have to add the last value of c in ar to get ans 
        if nums[-1]==1:
            ar.append(c)         
        m=ar[0]
        la=len(ar)
        for i in range(la-1):
            m=max(m,ar[i]+ar[i+1])
        return m
