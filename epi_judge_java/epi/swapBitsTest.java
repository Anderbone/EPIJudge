package epi;

public class swapBitsTest {
    public static void main(String[] args) {
        int i = 3;
        int j = 2;
        long swap0 = (long) (Math.pow(2,i) + Math.pow(2, j));
        long swap = (1L << i) | (1L << j);
        System.out.println(swap0+ "swap" + swap);
    }
}
