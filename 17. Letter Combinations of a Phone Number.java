class Solution {
	static String[] arr = { ".;","", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz" };
	
	public List<String> letterCombinations(String digits) {
		
		if (digits.length() == 0) {
			return new ArrayList<String>();
		}
		
		return helper(digits);
	}

	public List<String> helper(String digits) {
		if (digits.length() == 0) {
			List<String> temp = new ArrayList<>();
			temp.add("");
			return temp;
		}

		char ch = digits.charAt(0);
		String ros = digits.substring(1);
		List<String> res = helper(ros);
		List<String> ans = new ArrayList<>();

		String chcode = arr[ch - '0'];

		for (int i = 0; i < chcode.length(); i++) {
			char chc = chcode.charAt(i);
			for (String st : res)
			{
				ans.add(chc + st);
			}
			}
		return ans;
	}

}
