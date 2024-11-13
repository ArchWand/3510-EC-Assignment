import java.util.Scanner;

public class _01 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int[] values = Parser.parse_arr_int(f, n);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, values);
    }

    public Object run(Object[] input) {
        return Solutions.realEstatePrices((int[])input[0]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "values = %s\n" +
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
