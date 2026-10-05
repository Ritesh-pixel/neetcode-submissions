class Solution {
    public int[] productExceptSelf(int[] arr) {
        int pre = 1, post =1;
        
        int[] ans = new int[arr.length];
        for(int i =arr.length-1; i>=0; i--){
            ans[i] = post;
            post*= arr[i];
        }

        for(int i = 0; i<arr.length;i++){
            ans[i] *= pre;
            pre*=arr[i];
        }

        return ans;
        
    }
}  
