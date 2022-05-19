public class ConsistentStrings {
    public static int countConsistentStrings(String allowed, String[] words) {
        String alphabet = "abcdefghijklmnopqrstuvwxyz";
        String notAllowed;
        int counter = words.length;
        for (int i = 0; i < allowed.length(); i++) {
            String temp = Character.toString(allowed.charAt(i));
            alphabet = alphabet.replaceAll(temp, "");
        }
        notAllowed = alphabet;
        for (int i = 0; i < words.length; i++) {
            for (int j = 0; j < notAllowed.length(); j++) {
                if (words[i].contains(Character.toString(notAllowed.charAt(j)))) {
                    counter--;
                    break;
                }
            }
        }
        return counter;
    }
    public static void main(String[]args) {
        String allowed = "ab";
        String[] words = new String[]{"ad","bd","aaab","baa","badab"};
        countConsistentStrings(allowed, words);
    }
}
