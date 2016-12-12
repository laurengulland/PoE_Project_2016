/**
 * Created by carl on 12/6/16.
 */
public class Transmit {
    public static void main(String[] args) {
        Displays d = new Displays("/dev/ttyUSB0");
        d.alternating();

        d.disconnect();
    }
}
