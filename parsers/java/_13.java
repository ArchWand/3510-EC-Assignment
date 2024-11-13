import java.util.Scanner;

public class _13 implements Parser {
    public Object[] parser(Scanner f) {
        String text = f.nextLine();
        String pattern = f.nextLine();

        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return Parser.ret_parser(cert, text, pattern);
    }

    public Object run(Object[] input) {
        return Solutions.numDistinct((String)input[0], (String)input[1]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "text = %s\n" +
            "pattern = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n",
            (String)input[0],
            (String)input[1],
            (int)cert,
            (int)ans
        ));
    }

}
