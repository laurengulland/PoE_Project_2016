import serial
import time
from bits import *

def write_bytes(show):
	'''
	This takes in the items created by the bits class and 
	sends them to the arduino to display
	'''
	for item in show:
		print_bits(item)
		bits, delay = item
		ser.write(bytearray(bits))
		time.sleep(delay)

if __name__ == '__main__':
	# Creating a serial object
	ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=10)

	# Sleep for 2 seconds to wait for the serial to init
	time.sleep(2)

	p = phasor(.5)
	for _ in range(10):
		write_bytes(p)

	for _ in range(20):
		write_bytes([[[0,255,0,255],.5]])
		write_bytes([[[255,0,255,0],.5]])

	# Close the serial port
	ser.write(bytearray([0,0,0,0]))
	ser.close()