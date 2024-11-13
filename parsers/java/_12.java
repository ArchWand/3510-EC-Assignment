import java.util.ArrayList;
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
        return (List<ArrayList<Integer>>)cert == (List<ArrayList<Integer>>)ans;
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
