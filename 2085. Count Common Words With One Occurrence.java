class Solution {
	public int countWords(String[] words1, String[] words2) {

		HashMap<String, Integer> dict1 = new HashMap<>();
		HashMap<String, Integer> dict2 = new HashMap<>();
		for (int i = 0; i < words1.length; i++) {
			if (!dict1.containsKey(words1[i])) {
				dict1.put(words1[i], 0);
			}
			dict1.put(words1[i], dict1.get(words1[i]) + 1);
		}
		for (int i = 0; i < words2.length; i++) {
			if (!dict2.containsKey(words2[i])) {
				dict2.put(words2[i], 0);
			}
			dict2.put(words2[i], dict2.get(words2[i]) + 1);
		}
		int ans=0;
		for( String i : words1) {
			if (dict2.containsKey(i)) {
				if (dict2.get(i)==1 && dict1.get(i)==1) {
					ans++;
				}
			}
		}
		return ans;
	}
}
