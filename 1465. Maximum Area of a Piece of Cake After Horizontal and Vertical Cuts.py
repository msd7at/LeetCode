class Solution:
    def maxArea(self, h: int, w: int, hc: List[int], vc: List[int]) -> int:
        lhc=len(hc)
        vhc=len(vc)
        if lhc==1:
            lhei=max(hc[0]-0,h-hc[lhc-1])
        else:
            hc.sort()
            mhc=0
            for i in range(lhc-1):
                mhc=max(mhc,(hc[i+1]-hc[i]))
            k=hc[0]-0
            kl=h-hc[lhc-1]
            lhei=max(mhc,k,kl)
        if vhc==1:
            lwei=max(vc[0]-0,w-vc[vhc-1])
        else:
            vc.sort()
            mvc=0
            for i in range(vhc-1):
                mvc=max(mvc,(vc[i+1]-vc[i]))
            kv=vc[0]-0
            kh=w-vc[vhc-1]
            lwei=max(mvc,kv,kh)
        return ((lhei*lwei)%((10**9)+7))
        
        
  """
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.

 

Example 1:



Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:



Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9
 

Constraints:

2 <= h, w <= 10^9
1 <= horizontalCuts.length < min(h, 10^5)
1 <= verticalCuts.length < min(w, 10^5)
1 <= horizontalCuts[i] < h
1 <= verticalCuts[i] < w
It is guaranteed that all elements in horizontalCuts are distinct.
It is guaranteed that all elements in verticalCuts are distinct."""
