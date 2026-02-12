package iniciante;

import java.util.Scanner;

public class Main1009 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        String name = input.nextLine();
        double fixSalary = input.nextDouble();
        double sales = input.nextDouble();
        double salesCommission = sales / 100 * 15;
        double totalSalary = fixSalary + salesCommission;

        System.out.printf("TOTAL = R$ %.2f%n", totalSalary);
    }
}
