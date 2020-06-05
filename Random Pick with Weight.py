class Solution:

    def __init__(self, w: List[int]):
        s = sum(w)
        self.weight = [w[0]/s]
        for i in range(1, len(w)):            
            self.weight.append(self.weight[-1]+w[i]/s)

    def pickIndex(self) -> int:
        l, r, seed = 0, len(self.weight)-1, random.random()
        while l < r:
            m = (l+r)//2
            if self.weight[m] <= seed: l = m+1
            else: r = m
        return l
        
    """
    Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input: 
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments. Solution's constructor has one argument, the array w. pickIndex has no arguments. Arguments are always wrapped with a list, even if there aren't any."""
