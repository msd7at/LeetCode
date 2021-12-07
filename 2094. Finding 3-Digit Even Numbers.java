class Solution {
	public int[] findEvenNumbers(int[] digits) {
		Set<Integer> set = new HashSet<Integer>();
		int len = digits.length;
		for (int i = 0; i < len; i++) {
			if (digits[i] == 0)
				continue;
			for (int j = 0; j < len; j++) {
				for (int k = 0; k < len; k++) {
					if (digits[k] % 2 != 0)
						continue;
					if (i != j && j != k && k != i) {
						set.add(digits[i] * 100 + digits[j] * 10 + digits[k]);

					}
				}
			}
		}
		int[] ans = new int[set.size()];
		int c = 0;
		for (int i : set) {
			ans[c] = i;
			c++;
		}
		Arrays.sort(ans);
		return (ans);
	}
}
