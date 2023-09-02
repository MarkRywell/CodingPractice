import java.util.Scanner;


public class Adding {
    public static void main(String[] args){

        Scanner reader = new Scanner(System.in);
        int grades_list = 0;


        System.out.print("Enter number of students: ");
        int number = reader.nextInt();
        System.out.println();
        int i = number;

        while (i > 0){

            System.out.print("Enter grades: ");
            int grades = reader.nextInt();

            grades_list += grades;
            i -=1;
        }

        int total ;
        total = grades_list / number;
        System.out.println(number);
        System.out.println(total);




    }
}
