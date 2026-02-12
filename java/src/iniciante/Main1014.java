package iniciante;

import java.util.Scanner;

public class Main1014 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int x = input.nextInt();
        double y = input.nextDouble();

        double distancia = x / y;

        System.out.printf("%.3f km/l%n", distancia);
    }
}
