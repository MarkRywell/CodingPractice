package javaIO;

import java.io.*;
import java.util.*;

public class Testing{
    public static void main(String[] args)throws FileNotFoundException
    {

        Scanner inFile = new Scanner(new FileReader("C:\\Users\\Mark\\Desktop\\Mark.txt"));

        String first_name ;
        String last_name ;

        int age ;

        String course ;

        first_name = inFile.next();
        last_name = inFile.next();

        age = inFile.nextInt();

        course = inFile.next();

        PrintWriter outFile = new PrintWriter("C:\\Users\\Mark\\Desktop\\out.txt");


        outFile.println("Your name is " + first_name + " " + last_name);
        outFile.printf("You're %d years old \n", age);
        outFile.println("Course: " + course);

        inFile.close();
        outFile.close();

    }
}