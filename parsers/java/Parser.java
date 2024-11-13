import java.util.Scanner;

public interface Parser {
    public Object[] parser(Scanner f);
    public Object run(Object[] input);
    public boolean verifier(Object cert, Object ans);
    public void error(Object cert, Object[] input, Object ans);
}
