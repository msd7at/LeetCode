class Solution:
    def reverseBits(self, n):
        oribin='{0:032b}'.format(n)
        print(oribin)
        reversebin=oribin[::-1]
        return int(reversebin,2)
