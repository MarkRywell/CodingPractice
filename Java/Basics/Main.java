import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Main {
    public static Scanner sc = new Scanner(System.in);
    public static int a = 0;

    public static void main(String[] args) throws FileNotFoundException {
        user_input();
    }
    public static void user_input() throws FileNotFoundException{
        ++a;

        PrintWriter output = new PrintWriter("C:\\Users\\Mark\\Desktop\\employeefile" + a + ".txt");

        System.out.print("Enter Company ID: ");
        long company_id = sc.nextLong();
        System.out.println();

        System.out.print("Enter Last Name: ");
        String lastname = sc.next();
        System.out.println();

        System.out.print("Enter First Name: ");
        String firstname = sc.next();
        firstname += sc.nextLine();
        System.out.println();

        System.out.print("Enter Position: ");
        String position = sc.nextLine();
        System.out.println();

        System.out.print("Department:\n1: R&D department\n2: IT Department\n3: Administration Department\n4: Google\n ");
        System.out.print("Enter Department: ");
        int department = sc.nextInt();
        String department_print = null;
        if (department == 1) {
            department_print = "R&D department";
        }
        else if (department == 2) {
            department_print = "IT department";
        }
        else if (department == 3) {
            department_print = "Administration Department";
        }
        else if (department == 4){
            department_print = "Google";
        }

        System.out.println();
        System.out.print("Enter Contact Number: ");
        long contact = sc.nextLong();
        System.out.println();

        System.out.print("Enter Home Address: ");
        String address = sc.next();
        address += sc.nextLine();
        System.out.println();

        System.out.print("Enter Time In: ");
        String timein = sc.nextLine();
        System.out.println();

        System.out.print("Enter Time Out: ");
        String timeout = sc.next();
        timeout += sc.nextLine();
        System.out.println();

        output.println("Company: Cognizant Technology Solutions, Inc.");
        output.println("Company ID: " + company_id);
        output.println("Last name: "+ lastname);
        output.println("First name: "+ firstname);
        output.println("Position: "+ position);
        output.println("Department: "+ department_print);
        output.println("Contact Number: 0" + contact);
        output.println("Home Address: "+ address);
        output.println("Time In: "+ timein);
        output.println("Time Out: "+ timeout);
        output.close();

        decision();
    }
    public static void decision() throws FileNotFoundException{
        System.out.print("Do you want to enter again? ");
        String answer = sc.next();

        if(answer.equals("yes") || answer.equals("Yes")){
            user_input();
        }
        else if(answer.equals("no") || answer.equals("No")){
            System.out.print("Done!");
        }

    }

}


