class Solution {
    
    public class pair{
        char ch;
        int freq;
        public pair(char ch , int freq){
           this.ch =ch;
            this.freq=freq;
        }
    }
    
    public String reorganizeString(String s) {
        int[] map = new int[26];
        
        for (int i=0;i<s.length();i++){
            map[s.charAt(i)-'a']++;
        }
        
        PriorityQueue<pair> pq = new PriorityQueue<>((a,b)->(b.freq-a.freq));
        for(int i=0; i<26;i++){
            if (map[i] > 0){
                pq.add(new pair((char)('a'+i),map[i]));
            }
        }
        
        StringBuilder sb = new StringBuilder();
        
        pair block = pq.poll();
        sb.append(block.ch);
        block.freq--;
        
        while (pq.size()>0){
            
            pair temp = pq.poll();
            temp.freq--;
            sb.append(temp.ch);
            if (block.freq>0){
                pq.add(block);
            }
            block=temp;
        }
        
        if (block.freq>0){
            return "";
        }
        return sb.toString();
        
    }
}
