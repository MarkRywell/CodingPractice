import java.util.Scanner;

public class Rectangle {

    public static void main(String[] args) {

        Scanner reader = new Scanner(System.in);

        System.out.println("Finding the Parameter and Area of Rectangle");
        System.out.println();

        System.out.print("Enter length of the rectangle: ");
        double length = reader.nextDouble();

        System.out.print("Enter width of the rectangle: ");
        double width = reader.nextDouble();

        double perimeter ;
        double area ;

        perimeter = 2 * (length + width);
        area = length * width;

        System.out.println();
        System.out.println("Perimeter: " + perimeter);
        System.out.println("Area: " + area);


    }
}
