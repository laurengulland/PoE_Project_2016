/**
 * Created by carl on 12/6/16.
 */
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.nio.ByteBuffer;
import java.util.Enumeration;
import gnu.io.*;

public class SerialConnector implements SerialPortEventListener {

    public SerialPort serialPort;
    /** The port we're normally going to use. */
    private static String portName = "COM5"; // Windows
    public static BufferedReader input;
    public static OutputStream output;
    /** Milliseconds to block while waiting for port open */
    private static final int TIME_OUT = 2000;
    /** Default bits per second for COM port. */
    private static final int DATA_RATE = 9600;
    private static long in;

    public void setCOM(String com){
        portName = com;
    }

    public String getCOM(){
        return portName;
    }

    public boolean initialize(String s) {
        setCOM(s);
        CommPortIdentifier portId = null;
        Enumeration portEnum = CommPortIdentifier.getPortIdentifiers();

        //First, Find an instance of serial port as set in PORT_NAMES.
        while (portEnum.hasMoreElements()) {
            CommPortIdentifier currPortId = (CommPortIdentifier) portEnum.nextElement();
            if (currPortId.getName().equals(portName)) {
                portId = currPortId;
                break;
            }
        }

        if (portId == null) {
            return false;
        }

        try {
            // open serial port, and use class name for the appName.
            serialPort = (SerialPort) portId.open(this.getClass().getName(),
                    TIME_OUT);

            // set port parameters
            serialPort.setSerialPortParams(DATA_RATE,
                    SerialPort.DATABITS_8,
                    SerialPort.STOPBITS_1,
                    SerialPort.PARITY_NONE);

            // open the streams
            input = new BufferedReader(new InputStreamReader(serialPort.getInputStream()));
            output = serialPort.getOutputStream();
            writeData(0);

            // add event listeners
            serialPort.addEventListener(this);
            serialPort.notifyOnDataAvailable(true);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public synchronized void close() {
        if (serialPort != null) {
            serialPort.removeEventListener();
            serialPort.close();
            in = 0;
        }
    }

    public synchronized void serialEvent(SerialPortEvent oEvent) {
        if (oEvent.getEventType() == SerialPortEvent.DATA_AVAILABLE) {
            try {
                String inputLine = input.readLine();
                in = Integer.parseInt(inputLine);
            }
            catch(Exception e) {
            }
        }

    }

    public static synchronized void writeData(String data) {
        try {
            output.write(data.getBytes());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }

    public static synchronized void writeData(int data) {
        try {
            ByteBuffer b = ByteBuffer.allocate(4);
            b.putInt(data);
            System.out.println(b);
            output.write(b.array());
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
