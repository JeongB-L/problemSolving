public class SmallerThanTheCurrentNumber {
    public static int[] smallerNumbersThanCurrent(int[] nums) {
        int[] array = new int[nums.length];
        int counter = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < nums.length; j++) {
                if (nums[i] != nums[j] && nums[i] > nums[j]) {
                    counter++;
                }
            }
            array[i] = counter;
            counter = 0;
            System.out.println(array[i] + ", ");
        }
        return array;
    }
    public static void main(String[]args) {
        int[] array = new int[]{8, 1, 2, 2, 3};
        smallerNumbersThanCurrent(array);
    }
}
