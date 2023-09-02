import java.util.ArrayList;
import java.util.Scanner;
import static java.lang.Math.*;

public class PT {

    public static Scanner sc = new Scanner(System.in);

    public static double grade;
    public static ArrayList <String> gradelist = new ArrayList<>();

    public static void main(String[] args) {
        Solving();
    }
    public static void Solving(){

        double quiz = 0, exercises = 0, finalexam, quizpercentage, exercisepercentage, finalexampercent, grade = 0;

        System.out.print("Enter Subject name: ");
        String subject = sc.next();
        System.out.println();
        System.out.print("Enter Quiz percentage: ");
        quizpercentage = sc.nextDouble();
        System.out.print("Enter Exercise percentage: ");
        exercisepercentage = sc.nextDouble();
        System.out.print("Enter Final exam percentage: ");
        finalexampercent = sc.nextDouble();

        int a = 3;
        while(a > 0) {
            System.out.print("Enter a quiz points: ");
            quiz += sc.nextDouble();
            a--;
        }

        int b = 3;
        while(b > 0) {
            System.out.print("Enter exercise points: ");
            exercises += sc.nextDouble();
            b--;
        }

        System.out.print("Enter final exam points: ");
        finalexam = sc.nextDouble();
        double qpercentage = quizpercentage / 100;
        double averagequiz = (quiz / 3) * qpercentage ;
        double epercentage = exercisepercentage / 100;
        double averageexercise = (exercises / 3) * epercentage ;
        double fpercent = finalexampercent / 100;
        double averagefinal = (finalexam * fpercent);
        grade = averagequiz + averageexercise + averagefinal;

        double addgrade = ceil(grade);
        gradelist.add(subject);
        gradelist.add(Double.toString(addgrade));

        System.out.println();
        System.out.print("Do you want to enter grades again?: ");
        String answer = sc.next();

        if (answer.equals("yes")){
            Solving();
        }
        else{
            Display();
        }
    }

    public static void Display(){

        System.out.println("Calculated Grades: ");

        int index = 0;
        for(int x = 0; x < (gradelist.size() / 2); x++){
            for (int y = 0; y <  2; y++){
                System.out.print(" " + gradelist.get(index));
                index++;
            }
            System.out.println();
        }
    }
}
