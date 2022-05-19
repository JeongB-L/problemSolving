public class ReplaceDigitsWithCharacter {
    public static char shift(char letter, int indexPlus) {
        char returning = (char) (letter + (char) indexPlus);
        return returning;
    }
    public static String replaceDigits(String s) {
        int l = s.length();
        char[] array = new char[l];
        for (int i = 0; i < l; i++) {
            if (Character.isDigit(s.charAt(i))) {
                array[i] = shift(s.charAt(i - 1), s.charAt(i) - '0');
            } else {
                array[i] = s.charAt(i);
            }
        }
        String finale = new String(array);
        return finale;
    }
    public static void main(String[]args) {
        replaceDigits("a1");
    }
}
