package PractOOP;

public class Subjects {

    String name;
    String difficulty;

    Subjects(String name, String difficulty){
        this.name = name;
        this.difficulty = difficulty;

        System.out.println();
        System.out.printf("Subject: %s\nDifficulty: %s\n", name, difficulty);
    }
}
