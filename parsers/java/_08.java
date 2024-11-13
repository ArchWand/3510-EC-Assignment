import java.util.Scanner;
import java.util.Set;

public class _08 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        f.nextLine();
        String[] formulas = Parser.parse_arr_string(f, n);


        assert(f.nextLine() == "");

        int c = f.nextInt();
        f.nextLine();
        Set<String> cert = Parser.parse_set_string(f, c);

        return Parser.ret_parser(cert, (Object)formulas);
    }

    public Object run(Object[] input) {
        return Solutions.chemicalConcoctions((String[])input[0]);
    }

    public boolean verifier(Object cert, Object ans) {
        return ((Set<String>)cert).contains((String)ans);
    }

    public void error(Object cert, Object[] input, Object ans) {
        System.out.println(String.format(
            "Input:\n" +
            "formulas = %s\n" +
            "\n" +
            "Expected:\n" +
            "%s\n" +
            "\n" +
            "Actual:\n" +
            "%s\n",
            Parser.print_arr((String[])input[0]),
            Parser.print_set((Set<String>)cert),
            (String)ans
        ));
    }

}
