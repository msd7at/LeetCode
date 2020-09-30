class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d={}                                       #it will store element row-wise
        j=0                                        #column
        u=0                                        #index count for string s
        while u<len(s): 
            for i in range(numRows):               #it will store in column wise manner
                if i in d:
                    d[i]+=s[u]
                else:
                    d[i]=s[u]
                u+=1
                if u==len(s):
                    break
            if u==len(s):
                break
            j+=1
            for i in range(numRows-2,0,-1):        #it will store diagonal element bw 2                                                          #columns(except first and last row)
                if i in d:
                    d[i]+=s[u]
                else:
                    d[i]=s[u]
                u+=1
                j+=1
                if u==len(s):
                    break
        
        an=""                                      #resultant string
        for i in d:                                #add the row-wise string to resultant string
            an+=d[i]
        return an
            
                
