package OOP1;

import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner reader = new Scanner(System.in);

        /*System.out.print("Enter student name: ");
        String name = reader.nextLine();


        System.out.print("Enter course: ");
        String course = reader.nextLine();


        System.out.print("Enter year (1/2/3/4/5): ");
        int year = reader.nextInt();

        System.out.print("Sex: ");
        char sex = reader.next().charAt(0);

        System.out.print("Age: ");
        int age = reader.nextInt();*/

        Student student1 = new Student("Krishia Ocampo", "BS-IT", 2, 'F', 20);

        System.out.println(student1.getCourse());
        student1.getAge();
        student1.school("USTP");

        Student student2 = new Student("Mark Gaje", "BS - IT", 2, 'M', 20);
        student2.school("Oxford University");

        student1.talkTo(student2);
    }
}
