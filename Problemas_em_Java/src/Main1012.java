import java.util.Scanner;

public class Main1012 {
    public static void main(String[] args) {
        Scanner input =  new Scanner(System.in);

        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();

        saida(a, b, c);
    }

    private static void saida(double a, double b, double c) {
        System.out.printf("TRIANGULO: %.3f%n", areaTriangulo(a, c));
        System.out.printf("CIRCULO: %.3f%n", areaCirculo(c));
        System.out.printf("TRAPEZIO: %.3f%n", areaTrapezio(a, b, c));
        System.out.printf("QUADRADO: %.3f%n", areaQuadrado(b));
        System.out.printf("RETANGULO: %.3f%n", areaRetangulo(a, b));
    }

    private static double areaTriangulo(double a, double c) {
        return (a * c) / 2.0;
    }

    private static double areaCirculo(double c) {
        double pi = 3.14159;
        return pi * Math.pow(c, 2);
    }

    private static double areaTrapezio(double a, double b, double c) {
        return (a + b) * c / 2;
    }

    private static double areaQuadrado(double b) {
        return Math.pow(b, 2);
    }

    private static double areaRetangulo(double a, double b) {
        return a * b;
    }
}
