public class LC_01_01{
    public static void main(String args[]){

        int n =5;
        int arr[] = {2,6,5,8,11};
        int target = 15;
        String answer = twoSum(n,arr,target);
        System.out.println("Solution --> "+answer);

    }

    public static String twoSum(int n, int arr[], int target){
        for (int i =0; i<n; i++){
            for(int j =i+1; j<n;j++){

                if(arr[i]+arr[j]==target){
                    return "Yes";
                }
            }
        }
        return "No";
    } 
}