public class ShuffleTheArray {
    /*
    public static int[] shuffle(int[] nums, int n) {
        int[] temp1 = new int[n];
        int[] temp2 = new int[n];
        int[] finale = new int[2 * n];
        for (int i = 0; i < n; i++) {
            temp1[i] = nums[i];
        }
        int j = 0;
        for (int i = n; i < 2 * n; i++) {
            temp2[j] = nums[i];
            j++;
        }
        boolean isTemp1 = true;
        int k = 0;
        int z = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (isTemp1) {
                finale[i] = temp1[k];
                k++;
                isTemp1 = false;
                //
                System.out.println(finale[i]);
            } else {
                finale[i] = temp2[z];
                z++;
                isTemp1 = true;
                //
                System.out.println(finale[i]);
            }
        }
        return finale;
    }

     */
    //another solution
    //even number and odd number
    public static int[] shuffle(int[] nums, int n) {
        int[] array = new int[n * 2];
        for (int i = 0; i < n; i++) {
            array[2 * i + 1] = nums[n + 1];
            array[2 * i] = nums[i];
        }
        return array;
    }
    public static void main(String[]args) {
        int[] haha = new int[6];
        haha = new int[]{2, 5, 1, 3, 4, 7};
        shuffle(haha, 3);
    }
}
