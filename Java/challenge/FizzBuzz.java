package challenge;

public class FizzBuzz {
    int number;

    FizzBuzz(int number) {
        this.number = number;
    }

    public void execute() {
        for(int i = 1; i < this.number; i++) {
            if(i % 15 == 0) {
                System.out.println("fizzbuzz");
            }
            else if(i % 3 == 0) {
                System.out.println("fizz");
            }
            else if(i % 5 == 0) {
                System.out.println("buzz");
            }
            else {
                System.out.println(i);
            }
        }
    }

    public int[] count() {
        int fizzes = 0;
        int buzzes = 0;
        int fizzbuzzes = 0;
        int[] array = new int[3];

        for(int i = 1; i < this.number; i++) {
            if(i % 15 == 0) {
                fizzbuzzes += 1;
            }
            else if(i % 3 == 0) {
                fizzes += 1;
            }
            else if(i % 5 == 0) {
                buzzes += 1;
            }
        }
        array[0] = fizzes;
        array[1] = buzzes;
        array[2] = fizzbuzzes;

        return array;
    }
}
