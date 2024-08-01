public class LC01_Better {
    public static void main(String[] args) {
        int n =5;
        int arr[]={2,6,5,8,11};
        int target =11;
        int ans[]= twoSum(n,arr,target);
        System.out.println("Solution--> "+ans[0]+" "+ans[1]);
    }

    public static int[] twoSum(int n, int arr[], int target){
        int ans[] = new int[2];
        ans[0]=ans[1]=-1;
        for(int i = 0; i < n; i++){
            for (int j = i+1; j<n;j++){
                if(arr[i]+arr[j]==target){
                    ans[0]=i;
                    ans[1]=j;
                    return ans;
                }
            }
        }
        return ans;
    }  
}
