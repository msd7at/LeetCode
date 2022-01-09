class Solution {
    public boolean checkValid(int[][] matrix) {
 		int n = matrix.length;

		for (int i = 0; i < n; i++) {
			HashSet<Integer> r = new HashSet<>();
			HashSet<Integer> c = new HashSet<>();
			for (int j = 0; j < n; j++) {
				if (i >= 0 && j < n) {
					r.add(matrix[i][j]);
					c.add(matrix[j][i]);
				}

			}
			if (r.size() != n || c.size()!=n  ) {
				return false;
			}
		}
		return true;
       
    }
}
