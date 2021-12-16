class Solution {
    public List<Integer> luckyNumbers (int[][] matrix) {
        int m = matrix.length;
        int n = matrix[0].length;
        
        List<Integer> res = new ArrayList();
        int[] minrow = new int[m];
        
        for(int i=0;i<m;i++){
            int minn = Integer.MAX_VALUE;
            for(int j=0;j<n;j++) minn = Math.min(minn, matrix[i][j]);
            minrow[i] = minn;
        }
        
        for(int j=0;j<n;j++){
            int maxx = Integer.MIN_VALUE;
            int r = 0;
            for(int i=0;i<m;i++) {
                if(matrix[i][j] > maxx){
                    maxx = matrix[i][j];
                    r = i;
                }
            }
            if(maxx == minrow[r]) res.add(maxx);
        }
        
        return res;
    }
}
