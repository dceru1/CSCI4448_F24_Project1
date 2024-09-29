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
	'SP': 0x0000000000000000,
	'PC': 0x0000000000000000,
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
	for x in instructions:
		parser = parse(x)					# Parse the instruction
		print("\nLine Number:", lineNumber)			# Print line number
		print("Instruction", parser[0])				# Print instruction

		match parser[0]:					# Call instruction function
			case 'SUB':
				asmSUB(parser[1:])
				arm64em_functions.SUB(registers, parser[1], parser[2], parser[3])
			case 'EOR':
				asmEOR(parser[1:])
			case 'ADD':
				asmADD(parser[1:])
			case 'AND':
				asmAND(parser[1:])
			case 'MUL':
				asmMUL(parser[1:])
			case 'MOV':
				asmMOV(parser[1:])
			case 'STR':
				asmSTR(parser[1:])
			case 'STRB':
				asmSTRB(parser[1:])
			case 'LDR':
				asmLDR(parser[1:])
			case 'LDRB':
				asmLDRB(parser[1:])
			case 'NOP':
				asmNOP(parser[1:])
			case 'B':
				asmB(parser[1:])
			case 'B.GT':
				asmBGT(parser[1:])
			case 'B.LE':
				asmBLE(parser[1:])
			case 'CMP':
				asmCMP(parser[1:])
			case 'RET':
				return
			case _:
				print("Sorry")



		operandCounter = 1	#TMP
		for n in parser[1:]:
			print("Operand", operandCounter, ":", n)	# Print operand (looped)
			operandCounter+=1

		lineNumber+=1


	# Register print --------------------------
	print()
	for x, y in registers.items():
		if x != 'N' and x != 'Z':
			print(f"{x}: {y:#018x}")
		else:
			print(f"{x}: {y}")



# FUNCTIONS -----------------------------------------------------------
# operands is a list of the instruction inputs


def parse(assemLine):		# Inputs a string, returns a list with seperated instruction and operands
	parser = re.findall(r"[\w]+|\[.*?\]", assemLine)		# Seperates elements by whitespace or comma, keep bracket content together
	return parser

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
