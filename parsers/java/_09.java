import java.util.Scanner;

public class _09 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int[] nums = Parser.parse_arr_int(f, n);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, nums);
    }

    public Object run(Object[] input) {
        return Solutions.maxNonAdjSum((int[])input[0]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "nums = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n",
            Parser.print_arr((int[])input[0]),
            (int)cert,
            (int)ans
        ));
    }

}
