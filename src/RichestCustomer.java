public class RichestCustomer {
    public static int maximumWealth(int[][] accounts) {
        int temp = 0;
        int finale = 0;
        for (int i = 0; i < accounts.length; i++) {
            temp = 0;
            for (int j = 0; j < accounts[i].length; j++) {
                temp = temp + accounts[i][j];
            }
            finale = Math.max(finale, temp);
        }
        return finale;
    }
}
