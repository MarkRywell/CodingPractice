import java.util.ArrayList;

public class looping {
    public static void main(String[] args){

        ArrayList <String> gradelist = new ArrayList<>();
        gradelist.add("Math");
        gradelist.add("50");
        gradelist.add("English");
        gradelist.add("40");
        gradelist.add("Science");
        gradelist.add("52");

        System.out.println(gradelist.size());

        int index = 0;
        for(int x = 0; x < (gradelist.size() / 2); x++){
            for (int y = 0; y <  2; y++){
                System.out.print(" " + gradelist.get(index));
                index++;
            }
            System.out.println();
        }


        index = 0;
        for(int x = 0; x < 3; x++) {
            for (int y = 0; y < 2; y++) {
                System.out.print(" " + gradelist.get(index));
                index++;
            }
            System.out.println();
        }

        }
}
