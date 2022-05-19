public class Pangram {
    public static boolean checkIfPangram(String sentence) {
        String[] alphabet = new String[]{"a", "b", "c", "d", "e", "f", "g",
                "h", "i", "j", "k", "l", "m", "n",
                "o", "a", "p", "q", "r", "s", "t",
               "u", "v", "w", "x", "y", "z"};
        boolean rss = true;
        for (int i = 0; i < alphabet.length; i++) {
            if (!sentence.contains(alphabet[i])) {
                rss = false;
            }
        }
        return rss;
    }
    public static void main(String[]args) {
        String sentence = "thequickbrownfoxjumpsoverthelazydog";
        checkIfPangram(sentence);
    }
}
