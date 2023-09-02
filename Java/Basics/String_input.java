import java.util.Scanner;

public class String_input {
    public static void main(String[] args){

        Scanner reader = new Scanner(System.in);

        System.out.print("Enter ID: ");
        int id = reader.nextInt();

        System.out.print("Enter Name: ");
        String name = reader.nextLine();
        name += reader.nextLine();

        System.out.print("Enter Course and Year: ");
        String course_year = reader.nextLine();

        System.out.println();
        System.out.println("ID: " + id);
        System.out.println("Name: " + name);
        System.out.println("Course and year: " + course_year);
    }
}
