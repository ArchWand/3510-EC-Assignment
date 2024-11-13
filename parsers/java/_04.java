import java.util.Scanner;

public class _04 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int k = f.nextInt();
        int[] A = Parser.parse_arr_int(f, n);

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, A, k);
    }

    public Object run(Object[] input) {
        return Solutions.modTwoSum((int[])input[0], (int)input[1]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "A = %s\n" +
            "k = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n" +
            "\n",
            Parser.print_arr((int[])input[0]),
            (int)input[1],
            (int)cert,
            (int)ans
        ));
    }

}
