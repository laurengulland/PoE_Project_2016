def print_bits(item):
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
	val = []
	for b in byte:
		val.append(~b)
	return [val, time]

def phasor(time):
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