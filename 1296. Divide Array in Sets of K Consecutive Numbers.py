from collections import OrderedDict 

class Solution:
    def isPossibleDivide(self, hand: List[int], W: int) -> bool:
        

        hand.sort()
        d=OrderedDict()
        for i in hand:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        while True:
            for i in d:
                x=i
                d[x]=d[x]-1
                if d[x]==0:
                    del d[x]
                for j in range(W-1):
                    if x+1 not in d:
                        return False
                    else:
                        d[x+1]=d[x+1]-1
                        if d[x+1]==0:
                            del d[x+1]
                    x+=1            
                if d=={}:
                    return True
                break
        return True
