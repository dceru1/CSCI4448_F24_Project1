# Example usage: "python3 arm64em.py test.txt" 


import re
import sys

import arm64em_functions as arm_instruct
from arm64em_structures import registers
from arm64em_structures import stackClass


# main -------------------------------------------------------------------
def main():

	# Initialize stack -----------------------
	stack = stackClass(256)
	print(len(stack.stack))

	# Stack testing
	stack.push(0x1A)
	stack.push(0xFF,1)
	stack.push(0x4B,2)
	stack.stackPrint()
	stack.push(0xAA,255)
	stack.stackPrint()
	#value = stack.pop()

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
				arm_instruct.SUB(registers, parser[3], parser[4], parser[5])
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
				arm_instruct.STR(registers, stack, parser[3], parser[4])
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
				stack.stackPrint()
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

# Inputs a string, returns a list of independent values from string
def parse(assemLine):	
	parser = re.findall(r"[\w]+|\[.*?\]", assemLine)		# Seperates elements by whitespace or comma, keep bracket content together
	return parser

# Print register content
def regPrint():
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
