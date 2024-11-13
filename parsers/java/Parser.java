import java.util.Scanner;

public interface Parser {
    Object[] parser(Scanner f);
    Object run(Object[] input);
    boolean verifier(Object cert, Object ans);
    void error(Object cert, Object[] input, Object ans);

    static String print_arr(int[] v) {
        String s = "[";
        for (int i = 0; i < v.length-1; i++) {
            s += v[i] + ", ";
        }
        s += v[v.length-1] + "]";
        return s;
    }

    static String print_arrarr(int[][] vv) {
        String s = "[";
        for (int i = 0; i < vv.length-1; i++) {
            s += print_arr(vv[i]) + ", ";
        }
        s += print_arr(vv[vv.length-1]) + "]";
        return s;
    }

    static int[] parse_arr_int(Scanner f, int n) {
        int[] v = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = f.nextInt();
        }
        return v;
    }

    static int[][] parse_arrarr_int(Scanner f, int n, int w) {
        int[][] v = new int[n][w];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < w; j++) {
                v[i][j] = f.nextInt();
            }
        }
        return v;
    }

    static Object[] ret_parser(Object cert, Object... text_in) {
        return new Object[]{cert, text_in};
    }

}
