# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        h=n
        result=n
        while l<h:
            mid=int((l+h)/2)
            if isBadVersion(mid):
                result=mid
                h=mid
            else:
                l=mid+1
        return result
