import java.util.HashMap;

public class LC01_03 {
    public static void main(String[] args) {
        int n =5;
        int arr[] = {2,5,6,8,11};
        int target = 14;

        String ans = twoSum(n,arr,target);
        System.out.println("Solution --> "+ans);
    }

    public static String twoSum(int n,int arr[],int target){
        HashMap<Integer,Integer> mpp = new HashMap<>();
        for (int i = 0; i<n;i++){

        int num = arr[i];
        int moreNeeded = target - num;
        if(mpp.containsKey(moreNeeded)){
            return "Yes";
        }
        mpp.put(arr[i], i);
        }
        return "No";
    }

}
