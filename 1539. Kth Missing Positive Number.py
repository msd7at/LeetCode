1 using Set

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s=set(arr)
        for i in range(100000000000):
            if i not in s:
                if 0==k:
                    return i
                k-=1
2 without using set

class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        id=0
        l=len(arr)
        c=0
        i=0
        while True:
            if id < l:
                if i==arr[id]:
                    id+=1
                else:
                    if c==k:
                        return i
                    c+=1
                i+=1
            else:
                if c==k:
                    return i
                i+=1
                c+=1
