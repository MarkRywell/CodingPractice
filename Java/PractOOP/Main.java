package PractOOP;


import java.util.Scanner;

public class Main {
    public static void main(String[] args){

        Scanner reader = new Scanner(System.in);

        System.out.print("Enter subject: ");
        String name = reader.nextLine();

        System.out.print("Enter the difficulty: ");
        String difficulty = reader.next();

        Subjects sub1 = new Subjects(name, difficulty);


    }
}
