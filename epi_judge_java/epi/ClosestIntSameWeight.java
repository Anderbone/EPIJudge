package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class ClosestIntSameWeight {
    @EpiTest(testDataFile = "closest_int_same_weight.tsv")
    public static long closestIntSameBitCount(long x) {

        for (int i = 0; i < 64; i++) {
            short end1 = (short) (x & (1<<i));
            short end2 = (short) (x & (1<<(i+1)));
            if ((end1 != end2)&&(end1 == 0 || end2 == 0)) {
                // reverse these last two numbers
                x = (1<<i) ^ x;
                x = (1<<(i+1)) ^ x;
                return x;
            }
        }
        return x;

}

    public static void main(String[] args) {
        System.exit(
                GenericTest
                        .runFromAnnotations(args, "ClosestIntSameWeight.java",
                                new Object() {
                                }.getClass().getEnclosingClass())
                        .ordinal());
    }
}
