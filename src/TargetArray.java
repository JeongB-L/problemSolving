import java.util.ArrayList;

public class TargetArray {
    public int[] createTargetArray(int[] nums, int[] index) {
        ArrayList<Integer> temp = new ArrayList<Integer>();
        int alpha = nums.length;
        for (int i = 0; i < alpha; i++) {
            temp.add(index[i], nums[i]);
        }
        int[] finale = new int[alpha];
        for (int i= 0 ; i < alpha; i++) {
            finale[i] = temp.get(i);
        }
        return finale;
    }
    public static void main(String[]args) {
        ArrayList<Integer> temp = new ArrayList<Integer>();

    }
}
