import java.util.ArrayList;
import java.util.Scanner;

public class loop {

    public static Scanner reader = new Scanner(System.in);

    public static String subject;

    public static double quiz_percentage = 0;
    public static double exercise_percentage = 0;
    public static double exam_percentage = 0;

    public static int quiz = 0;
    public static int exercise = 0;
    public static int exam = 0;

    static ArrayList <Integer> quizlist = new ArrayList<>();
    public static void main(String[] args){

        Solving();


    }
    public static void Solving(){
        int i = 3;
        quiz = 0;
        exercise = 0;
        exam = 0;

        System.out.print("Enter subject name: ");
        subject += reader.next();





        while(i > 0){

            System.out.print("Enter grade: ");
            quiz += reader.nextInt();
            System.out.println();
            i--;
        }
        i = 3;

        while (i > 0){

        }




        quizlist.add(quiz);
        System.out.print("Do you want to try again?: ");
        String answer = reader.next();

        if (answer.equals("yes")){
            Solving();

        }
        else{
            Display();
        }
    }

    public static void Display(){
        System.out.println("Grades: ");


        for (Integer integer : quizlist) {
            System.out.println(integer);
        }
    }
}
