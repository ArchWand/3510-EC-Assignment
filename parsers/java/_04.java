import java.util.Scanner;

public class _04 implements Parser {
    public Object[] parser(Scanner f) {
        int n = f.nextInt();
        int k = f.nextInt();
        int[] A = new int[n];
        for (int i = 0; i < n; i++) {
            A[i] = f.nextInt();
        }

        assert(f.nextLine() == "");
        assert(f.nextLine() == "");

        int cert = f.nextInt();

        return new Object[]{cert, new Object[]{A, k}};
    }

    public Object run(Object[] input) {
        return Solutions.modTwoSum((int[])input[0], (int)input[1]);
    }

    public boolean verifier(Object cert, Object ans) {
        return (int)cert == (int)ans;
    }

    public void error(Object cert, Object[] input, Object ans) {
        String A = "[ ";
        for (int x : (int[])input[0]) {
            A += x + " ";
        }
        A += "]";
        int k = (int)input[1];

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
            "\n"
        , A, k, (int)cert, (int)ans));
    }

}
