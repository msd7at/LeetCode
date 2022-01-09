class Solution {
    public int minSwaps(int[] nums) {
		int ones = Arrays.stream(nums).sum();
		
		int ans= nums.length;
		int holes = 0;
		for (int i=0;i<ones;i++) {
			if (nums[i]==0) {
				holes+=1;
			}
		}
		
		ans = Math.min(ans, holes);
		
		
//		int left = 0 ;
		int right=ones%nums.length;
		
		for (int left=0 ;left<nums.length;left++) {
			
			ans=Math.min(ans, holes);
			
			if (nums[left] != nums[right]) {
				if (nums[right] == 1) {
					holes--;

				} else {
					holes++;
				}
				
				
			}
			right=  (right+1)%nums.length;
		}
		
		
		
		//return ans
		return ans;
    }
}
