/**
 * Created by carl on 12/6/16.
 */
public class Transmit {
    public static void main(String[] args) {
        Displays d = new Displays("/dev/ttyUSB0");
        for(int i = 0; i <100; i++){
            d.thick_stripe();
            d.alternating();
            d.stripe();
            d.argile();
        }

        d.disconnect();
    }
}
