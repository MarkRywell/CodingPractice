public class bricks {
    public static void main(String[] args){

        System.out.println(Bricks(3, 1, 8));
        System.out.println(Bricks(4, 5, 15));
        System.out.println(Bricks(1, 2, 12));

    }
    public static boolean Bricks(int small, int big, int goal){
        return small + big * 5 <= goal;
    }
}
