import serial
import time
import bitstring

def write_bytes(bits):
	# Convert a string of bits(1s and 0s) to a BitArray 
	byte_array = bitstring.BitArray(bin=bits)
	print(byte_array.tobytes())
	# Write the BitArray to the arduino
	ser.write(bytearray(byte_array.tobytes()))

if __name__ == '__main__':
	# Creating a serial object
	ser = serial.Serial('/dev/ttyUSB1', 9600, timeout=10)

	# Sleep for 2 seconds to wait for the serial to init
	time.sleep(2)

	'''
	This is one way of sending data - a string of 1's and zeros

	This current sends 4 '0' bytes to clear out the data
	'''
	bits = '0'*32
	write_bytes(bits)
	time.sleep(1)

	'''
	This is another way of sending data - bytearrays

	This is more for testing of response time before lagging
	The current safe time is about 50ms between updates
	'''
	for _ in range(50):
		ser.write(bytearray([0, 255, 0, 255]))
		time.sleep(.05)
		ser.write(bytearray([255, 0, 255, 0]))
		time.sleep(.05)

	# Close the serial port
	ser.close()