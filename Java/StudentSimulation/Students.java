package StudentSimulation;

public class Students {

    String firstName ;
    String lastName ;
    String year ;
    String course ;
    String section ;

    double midtermGrade ;
    double finalGrade ;

    Students (String firstName, String lastName, String year, String course, String section, double midtermGrade, double finalGrade){

        this.firstName = firstName;
        this.lastName = lastName;
        this.year = year;
        this.course = course;
        this.section = section;

        this.midtermGrade = midtermGrade;
        this.finalGrade = finalGrade;

        System.out.println();
        System.out.printf("STUDENT: %s %s ENROLLED.", firstName, lastName);
    }

    void introduceSelf(){

        System.out.println();
        System.out.printf("Name: %s %s \nCourse: %s \nYear: %s \nSection: %s \n", firstName, lastName, course, year, section);

    }

    void evaluateGrade(){

        double average ;

        average = (this.midtermGrade + this.finalGrade) / 2;

        System.out.println("Average Grade: " + average);

        int average_int = (int)average;

        if (average_int > 90){
            System.out.println("HONOR");
        }
        else if (average_int >= 75){
            System.out.println("PASSED");
        }
        else{
            System.out.println("FAILED");
        }


    }

}
