def print_bits(item):
	'''
	Item: tuple of bytes and display time
	
	This function is used to print out bits of a byte
	'''
	byte, time = item
	s = ""
	for b in byte:
		comp = 0b00000001
		for _ in range(8):
			if(comp&b):
				s += '1'
			else:
				s += '0'
			comp = comp<<1
		s += ' for '+ str(time) + ' '
	print(s)

def flip_bits(byte, time):
	'''
	byte: an array of bytes
	time: the display time

	This function takes in an array of bytes and display time. It
	flips the bits in each of the bytes (0b11110000 -> 0b00001111)

	returns: a tuple with the array of bytes and the display time
	'''
	val = []
	for b in byte:
		val.append(~b)
	return [val, time]

def phasor(time):
	'''
	time: the display time

	This function moves a bit in a set number of bytes across the
	bytes (0b00000001 -> 0b00000010 -> 0b00000100 -> etc...)

	returns: an array of tuples that contain the byte arrays and 
	display times
	'''
	show = []
	byte = 1
	for _ in range(3):
		show.append([[byte], time])
		byte = byte<<1
	for _ in range(3):
		show.append([[byte], time])
		byte = byte>>1
	return show


if __name__ == '__main__':
	b = [1, 70]
	time = 2
	print(print_bits([b,time]))
	b = flip_bits(b,time)
	print(print_bits(b))
	b = phasor(time)
	for thing in b:
		print(print_bits(thing))