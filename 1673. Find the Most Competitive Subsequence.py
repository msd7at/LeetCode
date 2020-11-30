class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        st=[]
        idx=0
        for i in nums:
            if st==[]:
                st.append(i)
            else:
                while st and st[-1]>i and (len(st)-1 + len(nums)-idx >= k):
                    st.pop()
                if len(st)<k:
                    st.append(i)
            idx+=1
        return st
