class Solution {
	public int minimumDifference(int[] nums, int k) {
        Arrays.sort(nums);
        if (nums.length <2 ){
            return 0;
        }
        k=k-1;
        System.out.println(Arrays.toString(nums));
        int min=100000;
        for(int i=0; i+k <nums.length;i++){
            if (nums[i+k] - nums[i] < min && nums[i+k] - nums[i]>-1  ) {
            	min= nums[i+k] - nums[i];
            }
            // System.out.println((i+k)+" "+i);
         
        }
        return min;
    }
}
