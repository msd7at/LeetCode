class Solution {
	public List<Integer> targetIndices(int[] nums, int target) {
		List<Integer> sol = new ArrayList<>();
		int l = 0;
		int id = -2;
		int r = nums.length;
		Arrays.sort(nums);
		while (l < r) {
			int mid = (l + r) / 2;
			if (nums[mid] == target) {
				id = mid;
                break;
			} else if (nums[mid] > target) {
				r = mid;
			} else {
				l = mid + 1;
			}
		}
		if (id ==-2) {
			return(sol);
		}
		int low=id,high=id;
		while (low>=0 && target== nums[low]) {
			low--;	
		}
		while(high<nums.length && target==nums[high]) {
			high++;
		}
		for(int g=low+1;g<high;g++) {
			sol.add(g);
		}
		return (sol);
	}
}
