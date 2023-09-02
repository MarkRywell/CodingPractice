package movie_tapes;

import java.util.ArrayList;

public class Movie_Customer {

    String movieName ;
    String StarringActors ;
    String Producer ;
    String ProductionCompany;
    int Copies_inStock ;

    Movie_Customer (String movieName, String StarringActors, String Producer, String ProductionCompany, int Copies_inStock){

        this.movieName = movieName;
        this.StarringActors = StarringActors;
        this.Producer = Producer;
        this.ProductionCompany = ProductionCompany;
        this.Copies_inStock = Copies_inStock;

        System.out.println();
        System.out.printf("%s : MOVIE ADDED!", movieName);

    }

    public String getName() {

        System.out.println();
        System.out.print("Movie Title: ");
        return this.movieName;
    }

    public int getCopy() {

        Copies_inStock--;
        System.out.println();
        System.out.printf("Got a copy! %d left \n", this.Copies_inStock);
        return this.Copies_inStock;


    }

    public int returnCopy() {

        Copies_inStock++;
        System.out.println();
        return this.Copies_inStock;

    }
}
