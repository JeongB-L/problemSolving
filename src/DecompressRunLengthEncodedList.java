import java.util.ArrayList;

public class DecompressRunLengthEncodedList {
    public int[] decompressRLElist(int[] nums) {
        /*
        for (int i = 0; i < nums.length; i = i + 2) {
            int[] temp = new int[nums[i]];
            //size of new array; frequency
            for (int j = 0; j < temp.length; j++) {
                temp[j] =  nums[i + 1];
                //filling in the new array; value
            }

        }

         */
        ArrayList<Integer> finale = new ArrayList<Integer>();
        for (int i = 0; i < nums.length; i = i + 2) {
            for (int j = 0; j < nums[i]; j++) {
                finale.add(nums[i + 1]);
            }
        }
        int[] returning = new int[finale.size()];
        int size = 0;
        for (int temp : finale) {
            returning[size++] = temp;
        }
        return returning;
    }
}
