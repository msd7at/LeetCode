class Solution {
   	 public int countElements(int[] nums) {
		 int c=0;
		 int min =Arrays.stream(nums).min().getAsInt();
		 int max = Arrays.stream(nums).max().getAsInt();
	     
		 for (int i : nums) {
			 if (i> min && i < max) {
				 c++;
			 }
		 }	 
	        return c;
	    }
}
