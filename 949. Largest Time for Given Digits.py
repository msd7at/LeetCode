class Solution:
    def largestTimeFromDigits(self, nums: List[int]) -> str:
        res=[]
        def per(depth):
            if depth==len(nums)-1:
                res.append(nums[:])
            for i in range(depth,len(nums)):
                nums[i],nums[depth]=nums[depth],nums[i]
                per(depth+1)
                nums[i],nums[depth]=nums[depth],nums[i]
        per(0)
        
        re=""
        for i in res:
            if i[0]*10 +i[1]<24 and i[2]*10+i[3]<60:
                re=max(re,str(i[0])+str(i[1])+':'+str(i[2])+str(i[3]))
        return re
