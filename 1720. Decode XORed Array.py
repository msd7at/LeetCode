class Solution:
    def decode(self,A: List[int], first: int) -> List[int]:
        res = [first]
        for a in A:
            res.append(res[-1] ^ a)
        return res
