class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        st=set()
        for a in A:
            res= "".join(sorted(a[1::2])+sorted(a[::2]))
            st.add(res)
        return len(st)
