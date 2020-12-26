class Solution:
    def countStudents(self, st: List[int], sw: List[int]) -> int:
        l=len(st)
        zst=st.count(0)
        ost=l-zst
        lsw=len(sw)
        for i in sw:
            if i==1:
                if ost>0:
                    ost-=1
                    l-=1

                else:
                    return l
            else:
                if zst>0:
                    zst-=1
                    l-=1

                else:
                    return l
        return l
