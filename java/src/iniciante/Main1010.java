package iniciante;

import java.util.Scanner;

public class Main1010 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int cod1 = input.nextInt();
        int qtd1 = input.nextInt();
        double value1 = input.nextDouble();

        int cod2 = input.nextInt();
        int qtd2 = input.nextInt();
        double value2 = input.nextDouble();

        double total = qtd1 * value1 + qtd2 * value2;

        System.out.printf("VALOR A PAGAR: R$ %.2f%n", total);
    }
}
