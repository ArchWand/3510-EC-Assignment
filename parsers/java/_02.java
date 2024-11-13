import java.util.Scanner;

public class _02 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int[][] packages = new int[n][2];
        for (int i = 0; i < n; i++) {
            packages[i][0] = f.nextInt();
            packages[i][1] = f.nextInt();
        }

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return new Object[]{cert, new Object[]{packages}};
    }

    public Object run(Object[] input) {
        return Solutions.maxPackages((int[][])input[0]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        String packages = "[ ";
        for (int[] x : (int[][])input[0]) {
            packages += "[" + x[0] + ", " + x[1] + "], ";
        }
        packages += "]";

        System.out.println(String.format(
            "Input:\n" +
            "packages = %s\n" +
            "\n" +
            "Expected:\n" +
            "%d\n" +
            "\n" +
            "Actual:\n" +
            "%d\n" +
            "\n"
        , packages, (int)cert, (int)ans));
    }

}
