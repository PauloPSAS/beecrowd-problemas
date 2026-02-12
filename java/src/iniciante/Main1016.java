package iniciante;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main1016 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int entrada = Integer.parseInt(br.readLine());
        System.out.println((entrada * 2) + " minutos");
    }
}
