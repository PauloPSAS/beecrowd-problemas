import java.util.Scanner;

public class Main1006 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double A = input.nextDouble();
        double B = input.nextDouble();
        double C = input.nextDouble();

        double media = ((2 * A) + (3 * B) + (5 * C)) / (2 + 3 + 5);

        System.out.printf("MEDIA = %.1f%n", media);
    }
}
