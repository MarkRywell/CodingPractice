import java.util.Scanner;

public class Java_Tutorial {
    public static void main(String[] args){

        Scanner input = new Scanner(System.in);

       int Jeepney_number;
       char Jeepney_letter;
       String JeepneyID;
       String location = "";

       System.out.println("Find my Jeepney!");
       System.out.println();

        //Input Jeepney Details

        System.out.print("Enter Jeepney Number: ");
        Jeepney_number = input.nextInt();
        System.out.println();

        System.out.print("Enter Jeepney Letter: ");
        Jeepney_letter = input.next().charAt(0);
        System.out.println();

        //Combine number and letter into one variable
        JeepneyID = String.valueOf(Jeepney_number) + Jeepney_letter;

        //Find matching details
        switch (JeepneyID) {
            case "12A": location = "Carbon";
            case "12C": location = "Panganiban";
            case "12F": location = "Taboan";
            case "12L": location = "Labangon";
            case "13C": location = "Talamban";
            case "14D": location = "Capitol";
            default: System.out.println("Jeepney cant be located!");
        }

        //Print out result
        System.out.println("Jeepney: " + JeepneyID + " , Usual Location = " + location);
    }
}
