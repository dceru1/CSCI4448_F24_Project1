class stackClass:
	def __init__(self):
		self.stack = bytearray(256)
		self.pointer = 255
		for i in range(len(self.stack)):
			self.stack.append(0x00)
	def push(self, input : bytearray, index : int = 0) -> None:
		input = input[::-1]							# reverse input for push
		for i in range(len(input)):
			self.stack[255 - registers["sp"] - index + i] = input[i]			# What the register is displaying - offset

	##FLAGS: 0 = x reg, 1 = w reg, 2 = a LDRB command
	def pop(self, index : int = 0, registerFlag : int = 0) -> int:
			pos = 255 - int(registers["sp"]) - index				# changed to 255 from 256
			if registerFlag == 0:
				num = self.stack[pos:pos+8]							# target point to grab
				self.stack[pos:pos+8] = b'\x00\x00\x00\x00\x00\x00\x00\x00'			# remove from stack
			elif registerFlag == 1:
				num = self.stack[pos:pos+4]							# target point to grab
				self.stack[pos:pos+4] = b'\x00\x00\x00\x00'				# remove from stack
			elif registerFlag == 2:
				num = self.stack[pos]
			num = num[::-1]							# reverse for register
			return int(num.hex(),16)
	def stackView(self):
		if self.stack[0] != 0:
			return self.stack[-1]
		else:
			raise IndexError("Stack Underflow: Stack empty")
	def stackPrint(self):
		addr = 0	# Address print counter
		print()
		for i in range(255, -1, -1):					# Print Bytes + Translate

			if (i+1) % 16 == 0:					# Print address
				print(f"{addr:08x}", end="\t")
				addr+=16
			print(f"{int(self.stack[i]):02x}", "", end="")

			if i % 16 == 0:						# Every 16 bytes, perform the translator
				print("|", end="")
				for j in range(16):				# Print 16 values (1 for each byte)
					if self.stack[(i+16)-(j+1)] != 0:
						print(chr(self.stack[(i+16)-(j+1)]), end="")	# Print translated version of the byte
					else:
						print(".", end="")		# If empty print '.'

				print("|\n")					# Close line
	
	# Operator overloads, used to manipulate the stack pointer in the register dict.
	def __eq__(self) -> int: return self.pointer

	def __add__(self, op2 : int) -> int: return self.pointer + op2

	def __sub__(self, op2 : int) -> int: return self.pointer - op2

stack = stackClass()

	# Register init-------------------------------
registers = {
	#https://developer.arm.com/documentation/102374/0101/Registers-in-AArch64---other-registers
	#tl;dr xzr is a all zero register that cannot be written to. Used to 'clear' registers.
	'xzr': 0x0000000000000000,
	'x0':  0x0000000000000000,
	'x1': 0x0000000000000000,
	'x2': 0x0000000000000000,
	'x3': 0x0000000000000000,
	'x4': 0x0000000000000000,
	'x5': 0x0000000000000000,
	'x6': 0x0000000000000000,
	'x7': 0x0000000000000000,
	'x8': 0x0000000000000000,
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
	'sp': stack,
	'pc': 0x0000000000000000,
	'N': 0,
	'Z': 0,
	'V': 0
}