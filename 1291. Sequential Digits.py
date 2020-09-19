class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        l=int(log(low,10)) # no of digits -1
        a="123456789"
        i=0
        dig=int(a[0:l])
        while  dig<low and l<10:
            if i+l>=10:
                i=0
                l+=1
            dig=int(a[i:i+l])
            i+=1
        if dig<low:
            return []
        li=[]
        while dig < high and l<10:
            li.append(dig)
            if i+l>=10:
                i=0
                l+=1
            dig=int(a[i:i+l])
            i+=1
        return li
