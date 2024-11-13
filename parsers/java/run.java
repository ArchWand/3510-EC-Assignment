import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.Scanner;

public class run {

    static final String TESTS = "./tests";
    static String tests_dir(String num) { return TESTS + "/" + num; }
    static String tests_path(String num, String test_case) {
        return tests_dir(num) + "/" + test_case;
    }

    static Parser[] problems = { null,
        new _01(),
        new _02(),
        new _03(),
        new _04(),
        new _05(),
        new _06(),
        new _07(),
        new _08(),
        new _09(),
        new _10(),
        new _11(),
        new _12(),
        new _13(),
        new _14(),
    };

    static final String GREEN = "\033[92m";
    static final String RED = "\033[91m";
    static final String ENDC = "\033[0m";

    public static void print_help() {
        System.out.println(
            "make java [ARGS=-h | ARGS=\"-t [01 02 ...]\"]\n" +
            "  Note that flags cannnot be combined.\n" +
            "\n" +
            "  -h   Print this help text.\n" +
            "\n" +
            "  -t   Test only specific problems. For example, to test 01, 04, and 12:\n" +
            "           make java ARGS=\"-t 01 04 12\"\n"
        );
    }

    public static void run_tests(String[] tests) {
        // Loop over every problem we want to test
        for (String prob : tests) {
            System.out.println("Testing problem " + prob);

            // Try every test case
            File dir = new File(tests_dir(prob));
            for (File file : dir.listFiles()) {
                String test_case = file.getName();
                Scanner f;
                try {
                    f = new Scanner(file);
                } catch(FileNotFoundException e) {
                    System.err.println("FileNotFoundException");
                    return;
                }

                // Parse the test case file, run the solution, and verify the answer
                Parser p = problems[Integer.valueOf(prob)];
                Object[] ret = p.parser(f);
                Object cert = ret[0];
                Object[] test_in = (Object[])ret[1];
                Object ans = p.run(test_in);
                boolean res = p.verifier(cert, ans);

                // Say whether the answer was right
                if (res) {
                    System.out.println("Test case " + test_case + " " + GREEN + "passed" + ENDC);
                } else {
                    System.out.println(RED + "Failed" + ENDC + " on " + test_case);
                    p.error(cert, test_in, ans);
                    break;
                }

            }
        }
    }

    public static void main(String[] args) {

        String[] tests = {"01","02","03","04","05","06","07","08","09","10","11","12","13","14"};
        // Parse command line arguments
        if (args.length > 0) {
            switch (args[0]) {
                case "-h":
                    print_help();
                    return;
                case "-t":
                    tests = Arrays.copyOfRange(args, 1, args.length);
                    break;
                default:
                    System.out.println("Invalid flag " + args[0] + ", ignoring.");
                    break;
            }
        }

        run_tests(tests);
    }
}
