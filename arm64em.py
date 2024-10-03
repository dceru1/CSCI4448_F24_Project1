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
	#stack.push(0x1A)
	#stack.push(0xFF,1)
	#stack.push(0x4B,2)
	#stack.stackPrint()
	#stack.push(0xAA,255)
	#stack.stackPrint()
	#value = stack.pop()

	#Take file input----------------------
	fileName = sys.argv[1]
	#fileName = "./test_code_to_emulate/simple/test4/test4.txt"
	fileIn = open(fileName, 'r')


	# Read file -----------------------
	instructions  = fileIn.readlines()


	# Parse data ------------------------
	x = 0
	while x in range(0,len(instructions)):						# parser[Address, Opcode, Instruction, Operand...] 
		parser = parse(instructions[x])					# Parse the instruction
		print("\nLine Number:", x)			# Print line number
		print("Address:", parser[0])				# Print Address
		print("Opcode:", parser[1])				# Print Opcode
		print("Instruction", parser[2].upper())			# Print instruction

		registers['pc'] = int(parser[0],16)
		match parser[2].upper():					# Call instruction function
			case 'SUB':
				asmSUB(parser[3:])
				arm_instruct.SUB(parser[3], parser[4], parser[5])
			case 'EOR':
				asmEOR(parser[3:])
				arm_instruct.EOR(parser[3],parser[4], parser[5])
			case 'ADD':
				asmADD(parser[3:])
				arm_instruct.ADD(parser[3],parser[4], parser[5])
			case 'AND':
				asmAND(parser[3:])
				arm_instruct.AND(parser[3],parser[4], parser[5])
			case 'MUL':
				asmMUL(parser[3:])
				arm_instruct.MUL(parser[3],parser[4], parser[5])
			case 'MOV':
				asmMOV(parser[3:])
				arm_instruct.MOV(parser[3],parser[4])
			case 'STR':
				asmSTR(parser[3:])
				arm_instruct.STR(stack, parser[3], parser[4])
			case 'STRB':
				asmSTRB(parser[3:])
			case 'LDR':
				asmLDR(parser[3:])
				arm_instruct.LDR(stack,parser[3],parser[4])
			case 'LDRB':
				asmLDRB(parser[3:])
			case 'NOP':
				asmNOP(parser[3:])
			case 'B':
				x = arm_instruct.B(x, parser[3])
				asmB(parser[3:])
				continue
			case 'B.GT':
				asmBGT(parser[3:])
				x = arm_instruct.BGT(x, parser[3])
				continue
			case 'B.LE':
				asmBLE(parser[3:])
				x = arm_instruct.BLE(x, parser[3])
				continue
			case 'CMP':
				asmCMP(parser[3:])
				arm_instruct.CMP(parser[3], parser[4])
			case 'RET':
				regPrint()
				#stack.stackPrint()
				fileIn.close()
				return 0
			case _:
				print("Sorry")
		x += 1



		operandCounter = 1	#TMP
		for n in parser[3:]:
			print("Operand", operandCounter, ":", n)	# Print operand (looped)
			operandCounter+=1
		regPrint()

# FUNCTIONS -----------------------------------------------------------
# operands is a list of the instruction inputs

# Inputs a string, returns a list of independent values from string
def parse(assemLine):	
	parser = re.findall(r"[\.\w]+|\[.*?\]", assemLine)
	print(parser)		# Seperates elements by whitespace or comma, keep bracket content together
	return parser

# Print register content
def regPrint():
	print()
	for x, y in registers.items():
		if x != 'N' and x != 'Z' and x != 'V':
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
