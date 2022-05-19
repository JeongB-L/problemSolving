public class DecodedXORarray {
    public static int[] decode(int[] encoded, int first) {
        int[] temp = new int[encoded.length + 1];
        temp[0] = first;
        for (int i = 0; i < encoded.length; i++) {
            temp[i + 1] = encoded[i] ^ temp[i];
        }
        return temp;
    }
    public static void main(String[]args) {
        int[] array = new int[]{1, 2, 3};
        decode(array, 1);
    }
}
