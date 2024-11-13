import java.util.Scanner;

public class _10 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        f.nextLine();
        String ticket = f.nextLine();

        assert(f.nextLine() == "");

        boolean cert = f.nextBoolean();

        return Parser.ret_parser(cert, n, ticket);
    }

    public Object run(Object[] input) {
        return Solutions.reviveStrings((int)input[0], (String)input[1]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (boolean)cert == (boolean)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "n = %d\n" +
            "ticket = %s\n" +
            "\n" +
            "Expected:\n" +
            "%b\n" +
            "\n" +
            "Actual:\n" +
            "%b\n",
            (int)input[0],
            (String)input[1],
            (boolean)cert,
            (boolean)ans
        ));
    }

}
