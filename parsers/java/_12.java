import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

public class _12 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int m = f.nextInt();
        List<List<Integer>> E = Parser.parse_listlist_int(f, m, 2);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int c = f.nextInt();
        List<List<Integer>> cert = Parser.parse_listlist_int(f, c, 2);

        return Parser.ret_parser(cert, n, E);
    }

    public Object run(Object[] input) {
        return Solutions.findNeededBridges((int)input[0], (List<ArrayList<Integer>>)input[1]);
    }

    public boolean verifier(Object cert, Object ans) {
        List<ArrayList<Integer>> c = (List<ArrayList<Integer>>)cert;
        List<ArrayList<Integer>> a = (List<ArrayList<Integer>>)ans;

        Comparator<ArrayList<Integer>> comp = new Comparator<ArrayList<Integer>>() {
            @Override
            public int compare(ArrayList<Integer> list1, ArrayList<Integer> list2) {
                int minLength = Math.min(list1.size(), list2.size());
                for (int i = 0; i < minLength; i++) {
                    int comparison = Integer.compare(list1.get(i), list2.get(i));
                    if (comparison != 0) {
                        return comparison;
                    }
                }
                return Integer.compare(list1.size(), list2.size());
            }
        };

        c.sort(comp);
        a.sort(comp);
        return c.equals(a);
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "n = %d\n" +
            "E = %s\n" +
            "\n" +
            "Expected:\n" +
            "%s\n" +
            "\n" +
            "Actual:\n" +
            "%s\n",
            (int)input[0],
            Parser.print_listlist((List<List<Integer>>)input[1]),
            Parser.print_listlist((List<List<Integer>>)cert),
            Parser.print_listlist((List<List<Integer>>)ans)
        ));
    }

}
