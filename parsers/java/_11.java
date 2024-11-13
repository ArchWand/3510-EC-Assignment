import java.util.Scanner;

public class _11 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int l = f.nextInt();
        int[] B = Parser.parse_arr_int(f, n);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, B, l);
    }

    public Object run(Object[] input) {
        return Solutions.countWaysToBuildWall((int[])input[0], (int)input[1]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "B = %s\n" +
            "l = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n",
            Parser.print_arr((int[])input[0]),
            (int)input[1],
            (int)cert,
            (int)ans
        ));
    }

}
