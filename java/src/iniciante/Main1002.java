package iniciante;

import java.util.Scanner;

public class Main1002 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        double raio;
        double pi = 3.14159;

        raio = input.nextDouble();

        System.out.printf("A=%.4f", pi * (raio * raio));
    }

}
