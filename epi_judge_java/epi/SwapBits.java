package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class SwapBits {
    @EpiTest(testDataFile = "swap_bits.tsv")
    public static long swapBits(long x, int i, int j) {
        // TODO - you fill in here.
        short xi = (short) ((short) (x >> i) & 1);
        short xj = (short) ((short) (x >> j) & 1);

        if (xi == xj) {
            return x;
        }
//        long swap = 2^i + 2^j;
//        long swap0 = (long) (Math.pow(2,i) + Math.pow(2, j));
        long swap0 =  ((long)Math.pow(2,i) + (long)Math.pow(2, j));
        long swap1 = (1L<<i) | (1L<<j);

        return x ^ swap0;
    }

    public static void main(String[] args) {
        System.exit(
                GenericTest
                        .runFromAnnotations(args, "SwapBits.java",
                                new Object() {
                                }.getClass().getEnclosingClass())
                        .ordinal());
    }
}
