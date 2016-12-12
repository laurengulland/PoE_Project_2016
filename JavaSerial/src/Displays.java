/**
 * Created by carl on 12/10/16.
 */
public class Displays {
    private SerialConnector sc = new SerialConnector();
    boolean connected = false;
    public Displays(String port){
        connected = sc.initialize(port);
    }

    void alternating(){
        int x = 0b11111111111111111111111111111111;
        for(int i = 0; i<100; i++) {
            sc.writeData(x);
            delay(1000);
            x = ~x;
            sc.writeData(x);
            delay(1000);
        }
    }

    void delay(int milliseconds){
        try {
            Thread.sleep(milliseconds);
        } catch (InterruptedException ex) {
            Thread.currentThread().interrupt();
        }
    }

    void disconnect(){
        if(connected)
            sc.close();
    }
}
