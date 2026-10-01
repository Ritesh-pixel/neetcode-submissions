class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>(); 
        for(int ele:nums) set.add(ele);

        
        int maxCons = 0;

        for(int i =0; i<nums.length; i++){
            int cons = 1;
            if(!set.contains(nums[i]-1)){
                int num = nums[i];
                while(set.contains(num+1)){
                     cons++;
                     num++;
                }
                maxCons = Math.max(cons,maxCons);
            }
        }
        return maxCons;
    }
}
