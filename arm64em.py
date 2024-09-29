# Example usage: "python3 arm64em.py test.txt" 


import re
import sys
import arm64em_functions


# Register init-------------------------------
registers = {
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


# main -------------------------------------------------------------------
def main():
	#Take file input----------------------
	fileName = sys.argv[1]
	fileIn = open(fileName, 'r')


	# Read file -----------------------
	instructions  = fileIn.readlines()


	# Parse data ------------------------
	lineNumber = 0
	for x in instructions:						# parser[Address, Opcode, Instruction, Operand...] 
		parser = parse(x)					# Parse the instruction
		print("\nLine Number:", lineNumber)			# Print line number
		print("Address:", parser[0])				# Print Address
		print("Opcode:", parser[1])				# Print Opcode
		print("Instruction", parser[2].upper())			# Print instruction

		match parser[2].upper():					# Call instruction function
			case 'SUB':
				asmSUB(parser[3:])
				arm64em_functions.SUB(registers, parser[3], parser[4], parser[5])
			case 'EOR':
				asmEOR(parser[3:])
			case 'ADD':
				asmADD(parser[3:])
			case 'AND':
				asmAND(parser[3:])
			case 'MUL':
				asmMUL(parser[3:])
			case 'MOV':
				asmMOV(parser[3:])
			case 'STR':
				asmSTR(parser[3:])
			case 'STRB':
				asmSTRB(parser[3:])
			case 'LDR':
				asmLDR(parser[3:])
			case 'LDRB':
				asmLDRB(parser[3:])
			case 'NOP':
				asmNOP(parser[3:])
			case 'B':
				asmB(parser[3:])
			case 'B.GT':
				asmBGT(parser[3:])
			case 'B.LE':
				asmBLE(parser[3:])
			case 'CMP':
				asmCMP(parser[3:])
			case 'RET':
				regPrint()
				return
			case _:
				print("Sorry")



		operandCounter = 1	#TMP
		for n in parser[3:]:
			print("Operand", operandCounter, ":", n)	# Print operand (looped)
			operandCounter+=1

		lineNumber+=1



# FUNCTIONS -----------------------------------------------------------
# operands is a list of the instruction inputs

def parse(assemLine):		# Inputs a string, returns a list of independent values from string
	parser = re.findall(r"[\w]+|\[.*?\]", assemLine)		# Seperates elements by whitespace or comma, keep bracket content together
	return parser

def regPrint():			# Print register contents
	print()
	for x, y in registers.items():
		if x != 'N' and x != 'Z':
			print(f"{x}: {y:#018x}")
		else:
			print(f"{x}: {y}")



def asmSUB(operands):
	print("Subracting", operands)

def asmEOR(operands):
	print("EORing", operands)

def asmADD(operands):
	print("Adding", operands)

def asmAND(operands):
	print("ANDing", operands)

def asmMUL(operands):
	print("Multiplying", operands)

def asmMOV(operands):
	print("MOVing", operands)

def asmSTR(operands):
	print("STRing", operands)

def asmSTRB(operands):
	print("STRBing", operands)

def asmLDR(operands):
	print("LDRing", operands)

def asmLDRB(operands):
	print("LDRBing", operands)

def asmNOP(operands):
	print("NOPing", operands)

def asmB(operands):
	print("Bing", operands)

def asmBGT(operands):
	print("B.GTing", operands)

def asmBLE(operands):
	print("BLEing", operands)

def asmCMP(operands):
	print("CMPing", operands)

def asmRET(operands):
	print("RETing", operands)





main()
