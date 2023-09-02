package OOP1;

public class Student {

    String name;
    String course;
    int year;
    char sex;
    int age;

    Student(String name, String course, int year, char sex, int age){

        this.name = name;
        this.course = course;
        this.year = year;
        this.sex = sex;
        this.age = age;

        System.out.println();
        System.out.println(name + " ENROLLED!");

    }

    public String getCourse(){
        return this.course;
    }

    void getAge(){

        System.out.println ("Hi I'm " + this.age + " years old!");
    }

    void school(String college){

        System.out.println("College: " + college + "\n" + this.year + " " + this.course);
    }

    void talkTo(Student x){

        System.out.println(name + " : Hello! " + x.name);
    }

}
