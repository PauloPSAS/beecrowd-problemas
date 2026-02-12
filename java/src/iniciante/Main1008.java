package iniciante;

import java.util.Scanner;

public class Main1008 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int number = input.nextInt();
        int hoursWorked = input.nextInt();
        double salaryHour = input.nextDouble();
        double salaryFinal = salaryHour * hoursWorked;

        System.out.println("NUMBER = " + number);
        System.out.printf("SALARY = U$ %.2f%n", salaryFinal);
    }
}
