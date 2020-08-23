class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        f=rounds[0]
        l=rounds[-1]
        if f<=l:
            return [i for i in range(f,l+1)]
        else:
            rec = []
            for i in range(n):
                if i+1<=l or i+1>=f:
                    rec.append(i+1)
            return sorted(rec)
