package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class ReverseBits {
    @EpiTest(testDataFile = "reverse_bits.tsv")
    public static long reverseBits(long x) {
        long result = 0;
        int count = 0;
        while (x > 0) {
            count++;
            short rightBit = (short) (x & 1);
            result = (result << 1) + rightBit;
            x >>= 1;
        }
        result <<= (64 - count);
        return result;
    }

    public static void main(String[] args) {
        System.exit(
                GenericTest
                        .runFromAnnotations(args, "ReverseBits.java",
                                new Object() {
                                }.getClass().getEnclosingClass())
                        .ordinal());
    }
}
