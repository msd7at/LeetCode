class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        ex=0
        oc=0

        for i in position:
            if i%2:
                oc+=1
            else:
                ex+=1
        return min(ex,oc)
