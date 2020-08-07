class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label==1:
            return [1]
        x=int(log(label,2))+1
        print(x)
        ans=[label]
        x-=1
        while x>0:
            label=2**(x-1) + ((2**(x+1) - 1 - label)//2)
            ans.append(label)
            x-=1
        return ans[::-1]
