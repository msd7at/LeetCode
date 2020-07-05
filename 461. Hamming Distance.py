# Link : -  https://leetcode.com/problems/hamming-distance/
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = '{0:032b}'.format(x)
        b = '{0:032b}'.format(y)
        count = 0
        i = 0
        while i < len(a):
            if a[i] != b[i]:
                count += 1
            i += 1
        return count
        
