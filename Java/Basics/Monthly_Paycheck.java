import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Scanner;

public class Monthly_Paycheck {
    public static void main(String[] args){

        Scanner reader = new Scanner(System.in);
        DecimalFormat df = new DecimalFormat("#.##");
        df.setRoundingMode(RoundingMode.CEILING);


        System.out.println("Monthly Paycheck");
        System.out.println();

        System.out.print("Enter Base Salary: ");
        double base_salary = reader.nextDouble();

        System.out.print("Enter no. of Years of Service: ");
        int years = reader.nextInt();

        System.out.print("Enter the total sales made: ");
        double total_sales = reader.nextDouble();


        double bonus ;
        double additional_bonus = 0;
        double paycheck ;

        if (years <= 5){
            bonus = 10 * years;
        }
        else {
            bonus = 20 * years;
        }

        if (total_sales >= 5000 && total_sales < 10000){
            additional_bonus = total_sales * 0.03;
        }
        else if (total_sales >= 10000){
            additional_bonus = total_sales * 0.06;
        }

        paycheck = base_salary + additional_bonus + bonus;

        System.out.println();
        System.out.println("Base Salary: " + base_salary);
        System.out.println("Years of Service: " + years);
        System.out.println("Total Sales made: " + total_sales);
        System.out.println("Bonus: " + bonus + " - " + df.format(additional_bonus));
        System.out.println("Paycheck: " + paycheck);
    }
}
