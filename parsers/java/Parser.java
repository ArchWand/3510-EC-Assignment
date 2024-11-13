import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Scanner;
import java.util.Set;

public interface Parser {
    Object[] parser(Scanner f);
    Object run(Object[] input);
    boolean verifier(Object cert, Object ans);
    void error(Object cert, Object[] input, Object ans);

    static String print_arr(int[] v) {
        if (v.length == 0) { return "[]"; }
        String s = "[";
        for (int i = 0; i < v.length-1; i++) {
            s += v[i] + ", ";
        }
        s += v[v.length-1] + "]";
        return s;
    }

    static String print_arr(String[] v) {
        if (v.length == 0) { return "[]"; }
        String s = "[";
        for (int i = 0; i < v.length-1; i++) {
            s += v[i] + ", ";
        }
        s += v[v.length-1] + "]";
        return s;
    }

    static String print_list(List<Integer> v) {
        if (v.size() == 0) { return "[]"; }
        String s = "[";
        for (int i = 0; i < v.size()-1; i++) {
            s += v.get(i) + ", ";
        }
        s += v.get(v.size()-1) + "]";
        return s;
    }

    static String print_set(Set<String> v) {
        return "{ " + String.join(", ", v) + " }";
    }

    static String print_arrarr(int[][] vv) {
        if (vv.length == 0) { return "[]"; }
        String s = "[";
        for (int i = 0; i < vv.length-1; i++) {
            s += print_arr(vv[i]) + ", ";
        }
        s += print_arr(vv[vv.length-1]) + "]";
        return s;
    }

    static String print_listlist(List<List<Integer>> vv) {
        if (vv.size() == 0) { return "[]"; }
        String s = "[";
        for (int i = 0; i < vv.size()-1; i++) {
            s += print_list(vv.get(i)) + ", ";
        }
        s += print_list(vv.get(vv.size()-1 )) + "]";
        return s;
    }

    static int[] parse_arr_int(Scanner f, int n) {
        int[] v = new int[n];
        for (int i = 0; i < n; i++) {
            v[i] = f.nextInt();
        }
        return v;
    }

    static String[] parse_arr_string(Scanner f, int n) {
        String[] v = new String[n];
        for (int i = 0; i < n; i++) {
            v[i] = f.nextLine();
        }
        return v;
    }

    static List<Integer> parse_list_int(Scanner f, int n) {
        List<Integer> v = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            v.add(f.nextInt());
        }
        return v;
    }

    static Set<String> parse_set_string(Scanner f, int n) {
        Set<String> v = new HashSet<>();
        for (int i = 0; i < n; i++) {
            v.add(f.nextLine());
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

    static List<List<Integer>> parse_listlist_int(Scanner f, int n, int w) {
        List<List<Integer>> v = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            v.add(new ArrayList<>());
            for (int j = 0; j < w; j++) {
                v.get(i).add(f.nextInt());
            }
        }
        return v;
    }

    static Object[] ret_parser(Object cert, Object... text_in) {
        return new Object[]{cert, text_in};
    }

}
