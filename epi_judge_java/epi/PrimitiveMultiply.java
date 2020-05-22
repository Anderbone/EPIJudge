package epi;

import epi.test_framework.EpiTest;
import epi.test_framework.GenericTest;

public class PrimitiveMultiply {
    @EpiTest(testDataFile = "primitive_multiply.tsv")
    public static long multiply(long x, long y) {

        long res = 0;
        while (x != 0) {
            if ((x&1) != 0) {
                res = add(res, y);
            }
            x >>= 1;
            y <<= 1;
        }
        return res;
    }

    private static long add(long x, long y) {
        long carry;

        while (y != 0) {
            carry = x & y;
            x = x ^ y;
            y = carry << 1;
        }
        return x;
//        return b == 0 ? a : add(a ^ b, (a & b) << 1);

    }

    public static void main(String[] args) {
        System.exit(
                GenericTest
                        .runFromAnnotations(args, "PrimitiveMultiply.java",
                                new Object() {
                                }.getClass().getEnclosingClass())
                        .ordinal());
    }
}
