import java.util.List;
import java.util.Scanner;

public class _05 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int m = f.nextInt();
        int maxTime = f.nextInt();
        List<Integer> energies = Parser.parse_list_int(f, n);
        List<List<Integer>> edges = Parser.parse_listlist_int(f, m, 3);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, energies, edges, maxTime);
    }

    public Object run(Object[] input) {
        return Solutions.maximumMagicPathPower((List<Integer>)input[0], (List<List<Integer>>)input[1], (int)input[2]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "energies = %s\n" +
            "edges = %s\n" +
            "maxTime = %d\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n",
            Parser.print_list((List<Integer>)input[0]),
            Parser.print_listlist((List<List<Integer>>)input[1]),
            (int)input[2],
            (int)cert,
            (int)ans
        ));
    }

}
