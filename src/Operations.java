public class Operations {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for (int i = 0; i < operations.length; i++) {
            if (operations[i].equals("X++") || operations[i].equals("++X")) {
                x++;
            } else if (operations[i].equals("X--") || operations[i].equals("--X")) {
                x--;
            }
        }
        /*int X = 0;
        for (String operation : operations) {
            if (operation.contains("++")) X++;
            if (operation.contains("--")) X--;
        }
        */
        return x;
    }
}
