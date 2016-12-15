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
        int x = 0b10101010101010101010101010101010;
        for(int i = 0; i<20; i++) {
            sc.writeData(x);
            delay(500);
            x = ~x;
            sc.writeData(x);
            delay(500);
        }
    }

    void stripe(){
        for(int d = 0; d < 5; d++){
            int x = 0b00000000000000000000000000000001;
            for(int i = 0; i<16; i++) {
                sc.writeData(x);
                delay(500);
                x = x<<1;
            }
            for(int i = 0; i<16; i++) {
                sc.writeData(x);
                delay(500);
                x = x>>1;
            }
        }
    }

    void thick_stripe(){
        for(int d = 0; d < 5; d++){
            int x = 0b00000000000000000000000000001111;
            for(int i = 0; i<12; i++) {
                sc.writeData(x);
                delay(500);
                x = x<<1;
            }
            for(int i = 0; i<12; i++) {
                sc.writeData(x);
                delay(500);
                x = x>>1;
            }
        }
    }

    void argile(){
        int x = 0;
        short a = 0b11000000000000;
        byte b = 0b0000011;
        for(int d = 0; d < 5; d++){
            for(int i = 0; i < 5; i++){
                x = 0;
                x = x|a;
                x = x|b;
                sc.writeData(x);

                a = (short)((int)a>>1);
                b = (byte)((int)b<<1);
                delay(500);
            }
            for(int i = 0; i < 5; i++){
                x = 0;
                x = x|a;
                x = x|b;
                sc.writeData(x);

                a = (short)((int)a<<1);
                b = (byte)((int)b>>1);
                delay(500);
            }
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
