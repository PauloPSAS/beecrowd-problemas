import java.util.Scanner;

public class Main1011 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int R = input.nextInt();

        double vol = (4.0 / 3.0) * Math.PI * (Math.pow(R, 3));

        System.out.printf("VOLUME = %.3f%n", vol);
    }
}
