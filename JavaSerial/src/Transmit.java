/**
 * Created by carl on 12/6/16.
 */
import gnu.io.*;
public class Transmit {
    private static SerialConnector sc = new SerialConnector();
    public static void main(String[] args) {
        boolean connected = false;
        connected = sc.initialize("/dev/ttyUSB0");
        try {
            Thread.sleep(1000);
        } catch(InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
        for(int i = 0; i<10; i++) {
            int x = 0b10101010101010101010101010101010;
            System.out.println(Integer.toBinaryString(x));
            sc.writeData(x);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }

            x = ~x;
            System.out.println(Integer.toBinaryString(x));
            sc.writeData(x);

            try {
                Thread.sleep(1000);
            } catch (InterruptedException ex) {
                Thread.currentThread().interrupt();
            }
        }

        if(connected)
            sc.close();
    }
}
