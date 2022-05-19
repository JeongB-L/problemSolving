import java.util.*;


public class ShuffleString {
   /* public String restoreString(String s, int[] indices) {
    //use stringbuilder and put them together.
        //sort using integer conversion of charAt.
        //then return
        String[] stringArray = new String[s.length()];
        for (int i = 0; i < s.length(); i++) {
            StringBuilder sb = new StringBuilder();
            sb.append(Character.toString(s.charAt(i)));
            sb.append(indices[i]);
            stringArray[i] = sb.toString();
        }
        int k = 0;
        for (int i = 0; i < s.length(); i++) {
            for (int j = s.length() - 1; j >= i; j--) {
                if (Integer.parseInt(String.valueOf(stringArray[j - 1].charAt(1)))
                        > Integer.parseInt(String.valueOf(stringArray[j].charAt(1)))) {
                    k = Integer.parseInt(String.valueOf(stringArray[j - 1]));

                }
            }
        }
    }

    */
   public String restoreString(String s, int[] indices) {
       //create a character array
       // store each char of string in there with the respected indices.
       //return it
       Character[] charArray = new Character[s.length()];
       for (int i = 0; i < indices.length; i++) {
           char temp = s.charAt(i);
           charArray[indices[i]] = temp;
       }
       StringBuilder sb = new StringBuilder();
       for (int i = 0; i < indices.length; i++) {
           sb.append(charArray[i]);
       }
       return sb.toString();
   }
}
