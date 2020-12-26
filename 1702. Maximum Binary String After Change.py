class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        c=0
        st=0
        for i in range(len(binary)) :
            if binary[i]=="0":
                if c==0:
                    st=i
                c+=1
        c=c+st
        res=""
        for i in range(len(binary)):
            if i==c-1:
                res+="0"
            else:
                res+="1"
        return res
