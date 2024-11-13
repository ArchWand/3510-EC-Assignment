import java.util.Scanner;

public class _03 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int[] blocks1 = Parser.parse_arr_int(f, n);
        int[] blocks2 = Parser.parse_arr_int(f, n);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, blocks1, blocks2);
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
            "blocks1 = %s\n" +
            "blocks2 = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n",
            Parser.print_arr((int[])input[0]),
            Parser.print_arr((int[])input[1]),
            (int)cert,
            (int)ans
        ));
    }

}
