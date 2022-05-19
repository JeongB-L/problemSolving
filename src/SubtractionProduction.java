public class SubtractionProduction {
    public int subtractProductAndSum(int n) {
        int product = 1;
        int summation = 0;
        //int subtraction = 0;
        char n1;
        String nString = Integer.toString(n);
        for (int i = 0; i < nString.length(); i++) {
            n1 = nString.charAt(i);
            product = product * (n1 - '0');
            summation = summation + (n1 - '0');
        }
        return product - summation;
    }
}
