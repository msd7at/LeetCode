class Solution:
    def minInsertions(self, s: str) -> int:
        st=[]
        n=len(s)
        res=0
        idx=0
        while idx< n:
            c=s[idx]
            if c=="(":
                st.append(c)
            else:
                if not st:
                    res+=1
                    st.append("(")
                if idx<n-1 and s[idx+1]==")":
                    idx+=1
                    st.pop()
                else:
                    res+=1
                    st.pop()
            idx+=1
        return res+(len(st)*2)
                    
                
            
