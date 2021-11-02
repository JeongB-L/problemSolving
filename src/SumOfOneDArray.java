public class SumOfOneDArray {
    //use for loop
    //keep the sum
    //add the previous some to the new value and then store it into the finale array.
    public static int[] runningSum(int[] nums) {
        int[] finale = new int[nums.length];
        finale[0] = nums[0];
        int sum = finale[0];
        for (int i = 1; i < nums.length; i++) {
            sum += nums[i];
            finale[i] = sum;
            //System.out.println(finale[i]);
        }
        return finale;
    }

    public static void main(String[]args) {
        int[] array = new int[4];
        array = new int[]{1, 2, 3, 4};
        runningSum(array);

    }
}
