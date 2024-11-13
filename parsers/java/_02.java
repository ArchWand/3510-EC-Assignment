import java.util.Scanner;

public class _02 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int[][] packages = Parser.parse_arrarr_int(f, n, 2);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, (Object)packages);
    }

    public Object run(Object[] input) {
        return Solutions.maxPackages((int[][])input[0]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "packages = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n",
            Parser.print_arrarr((int[][])input[0]),
            (int)cert,
            (int)ans
        ));
    }

}
