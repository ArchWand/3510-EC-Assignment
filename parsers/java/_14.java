import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class _14 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int[][] locations = Parser.parse_arrarr_int(f, n, 2);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        long cert = f.nextLong();

        return Parser.ret_parser(cert, (Object)locations);
    }

    public Object run(Object[] input) {
        return Solutions.minNetworkCost((int[][])input[0]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (long)cert == (long)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "locations = %s\n" +
            "\n" +
            "Expected:\n" +
            "%s\n" +
            "\n" +
            "Actual:\n" +
            "%s\n",
            Parser.print_arrarr((int[][])input[0]),
            (long)cert,
            (long)ans
        ));
    }

}
