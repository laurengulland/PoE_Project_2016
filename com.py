import serial
import time
import bitstring

def write_bytes(bits)
	# Convert a string of bits(1s and 0s) to a BitArray 
	byte_array = bitstring.BitArray(bin=bits)

	# Write the BitArray to the arduino
	ser.write(byte_array.tobytes())


if __name__ == "Main":
# Creating a serial object
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=2)

# Sleep for 2 seconds to wait for the serial to init
time.sleep(2)

bits = '00001111000010100000111100001010'

write_bytes(bits)
# Close the serial port
ser.close()