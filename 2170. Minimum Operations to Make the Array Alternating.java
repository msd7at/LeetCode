class Solution {
    
    public static void greater(int[] even,int c,int i){
        if (even[0] < c){
                even[2] = even[0];
                even[3] = even[1];
                
                even[0] = c;
                even[1] = i;
                
            }
            
            else if (even[2] < c){
                even[2] = c;
                even[3] = i;
            }
        
    }
    
    public int minimumOperations(int[] nums) {
        int[] count1 =  new int[100001];
        int[] count2 =  new int[100001];
        
        int numsLen= nums.length;
        for(int i=0 ;i < numsLen ; i++){
            if ((i & 1) ==0){
                count1[nums[i]]++;
            }
            else{
                count2[nums[i]]++;
            }
        }
        
        int[] odd = new int[4];
        int[] even = new int[4];
        
        for (int i =0 ; i <100001;i++){
            
            greater(even,count1[i],i);
            greater(odd,count2[i],i);
            
        }
        
        
        if (odd[1] != even[1]){
            return numsLen - odd[0] - even[0];
        }
        
        return Math.min(numsLen - odd[0] - even[2], numsLen - odd[2] - even[0]);
        
        
    }
    

}
// public int minimumOperations(int[] nums) {
//         // make count for even & odd indices elements
//         int[] count1 = new int[100001];
//         int[] count2 = new int[100001];
        
//         int n = nums.length;
//         for (int i = 0; i < n; i += 2) {
//             ++count1[nums[i]];
//             if (i + 1 < n) {
//                 ++count2[nums[i + 1]];
//             }
//         }
        
//         // find max & second max for both odd & even , store along with candidate element
//         int[] even = new int[4];
//         int[] odd = new int[4];
//         for (int i = 1; i < 100001; ++i) {
//             int c = count1[i];
//             if (even[0] < c) {
//                 even[2] = even[0];
//                 even[3] = even[1];
                
//                 even[0] = c;
//                 even[1] = i;
//             } else if (even[2] < c) {
//                 even[2] = c;
//                 even[3] = i;
//             }
            
//             c = count2[i];
//             if (odd[0] < c) {
//                 odd[2] = odd[0];
//                 odd[3] = odd[1];

//                 odd[0] = c;
//                 odd[1] = i;
//             } else if (odd[2] < c) {
//                 odd[2] = c;
//                 odd[3] = i;
//             }
//         }
        
//         // if max candidate for odd & even is different, can use them.
//         if (odd[1] != even[1]) {
//             return n - odd[0] - even[0];
//         }
//         // else take either of second max for odd or even.
//         return Math.min(n - odd[0] - even[2], n - odd[2] - even[0]);
//     }
