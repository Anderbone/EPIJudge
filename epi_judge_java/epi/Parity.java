package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class Parity {
    @EpiTest(testDataFile = "parity.tsv")
    public static short parity(long x) {
        short flag = 0;
        while (x > 0) {
            short last = (short) (x & 1);
            flag = (short) (flag ^ last);
            x = x >> 1;


//            flag ^= 1;
//            x = x&(x-1);
        }
        return flag;
    }

    public static void main(String[] args) {
        System.exit(
                GenericTest
                        .runFromAnnotations(args, "Parity.java",
                                new Object() {
                                }.getClass().getEnclosingClass())
                        .ordinal());
    }
}
