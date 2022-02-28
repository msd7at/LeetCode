class Solution {
	public List<String> summaryRanges(int[] nums) {
		List<String> ans = new ArrayList<String>();
		if (nums.length == 0) {
			return ans;
		}
		int fir = nums[0];
		int prev = nums[0];

		for (int i = 1; i < nums.length; i++) {
			if (prev + 1 != nums[i] || Math.abs(Math.abs(nums[i]) - Math.abs(prev)) > 1) {
				if (prev == fir) {
					ans.add("" + fir);
				} else {
					ans.add(fir + "->" + prev);
				}
				fir = nums[i];

			}

			prev = nums[i];
		}
		if (prev == fir) {
			ans.add("" + fir);
		}

		else {
			ans.add(fir + "->" + prev);
		}
		return ans;
	}
}
