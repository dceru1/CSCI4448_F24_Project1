# Register init-------------------------------
registers = {
	'x0': 0x0000000000000000,
	'x1': 0x0000000000000000,
	'x2': 0x0000000000000001,
	'x3': 0x0000000000000000,
	'x4': 0x0000000000000000,
	'x5': 0x0000000000000000,
	'x6': 0x0000000000000000,
	'x7': 0x0000000000000000,
	'x8': 0x0000000000000010,
	'x9': 0x0000000000000000,
	'x10': 0x0000000000000000,
	'x11': 0x0000000000000000,
	'x12': 0x0000000000000000,
	'x13': 0x0000000000000000,
	'x14': 0x0000000000000000,
	'x15': 0x0000000000000000,
	'x16': 0x0000000000000000,
	'x17': 0x0000000000000000,
	'x18': 0x0000000000000000,
	'x19': 0x0000000000000000,
	'x20': 0x0000000000000000,
	'x21': 0x0000000000000000,
	'x22': 0x0000000000000000,
	'x23': 0x0000000000000000,
	'x24': 0x0000000000000000,
	'x25': 0x0000000000000000,
	'x26': 0x0000000000000000,
	'x27': 0x0000000000000000,
	'x28': 0x0000000000000000,
	'x29': 0x0000000000000000,
	'x30': 0x0000000000000000,
	'sp': 0x0000000000000000,
	'pc': 0x0000000000000000,
	'N': 0,
	'Z': 0
}

class stackClass:
	def __init__(self, maxSize):
		self.stack = []
		self.maxSize = int(256)
		for i in range(int(256)):
			self.stack.append(None)

	def push(self, input, index : int = 0):
		if index < int(256):
			self.stack[index] = input
		else:
			raise OverflowError("Stack Overflow: Stack exceeds maximum size")
	def pop(self, index : int = 0):
		if index > 0 and self.stack[0] != None:
			ret = self.stack[index]
			self.stack[index] = None
			return ret
		else:
			raise IndexError("Stack Underflow: Can not pop, stack empty")
	def stackView(self):
		if self.stack[0] != 0:
			return self.stack[-1]
		else:
			raise IndexError("Stack Underflow: Stack empty")
	def stackPrint(self):
		addr = 0	# Address print counter
		fillStack = self.stack + [None] * (256 - len(self.stack))	# Fill stack with None to max out size
		print()
		for i in range(255, -1, -1):					# Print Bytes + Translate

			if (i+1) % 16 == 0:					# Print address
				print(f"{addr:08x}", end="\t")
				addr+=16

			byte = fillStack[i]					# Byte starts at most recent in stack

			if byte is not None:					# If Byte isn't empty, print the byte
				print(f"{format(byte, "x")}", "", end="")
			else:							# If Byte is empty, print 00
				print("00 ", end="")

			if i % 16 == 0:						# Every 16 bytes, perform the translator
				print("|", end="")
				for j in range(16):				# Print 16 values (1 for each byte)
					if fillStack[(i+16)-(j+1)] != None:
						print(chr(fillStack[(i+16)-(j+1)]), end="")	# Print translated version of the byte
					else:
						print(".", end="")		# If empty print '.'

				print("|\n")					# Close line

