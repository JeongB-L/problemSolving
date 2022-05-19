import java.util.Scanner;

public class OddorEven {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int number;

        while (in.hasNextInt()) {
            number = in.nextInt();
            if (number % 2 == 0)
                System.out.printf("%d is even\n", number);
            else
                System.out.printf("%d is odd\n", number);
        }
    }
}
