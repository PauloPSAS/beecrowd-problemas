package iniciante;

import java.util.Scanner;

public class Main1005 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double A = input.nextDouble();
        double B = input.nextDouble();

        double media = ((3.5 * A) + (7.5 * B)) / (3.5 + 7.5);

        System.out.printf("MEDIA = %.5f%n", media);
    }
}
