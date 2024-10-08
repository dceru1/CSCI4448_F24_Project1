# Example usage: "python3 arm64em.py test.txt" 
# ARM64 Emulator by Daniel Cerulli & Tyler Burzenski
# Reverse Engineering 	Prof. Page	CSCI-4448-01
# Last updated 10/7/24

import re
import sys

import arm64em_functions as arm_instruct
from arm64em_structures import registers, stack


# main -------------------------------------------------------------------
def main():

	#Take file input----------------------
	fileName = sys.argv[1]
	fileIn = open(fileName, 'r')

	# Read file -----------------------
	instructions  = fileIn.readlines()


	# Parse data ------------------------
	x = 0
	while x in range(0,len(instructions)):						# parser[Address, Opcode, Instruction, Operand...] 
		parser = parse(instructions[x])					# Parse the instruction
		print("\nLine Number:", x)					# Print line number
		print("Address:", parser[0])				# Print Address
		print("Opcode:", parser[1])					# Print Opcode
		print("Instruction", parser[2].upper())		# Print instruction

		registers['pc'] = int(parser[0],16)
		match parser[2].upper():					# Call instruction function
			case 'SUB':
				arm_instruct.SUB(parser[3], parser[4], parser[5])
			case 'EOR':
				arm_instruct.EOR(parser[3],parser[4], parser[5])
			case 'ADD':
				arm_instruct.ADD(parser[3],parser[4], parser[5])
			case 'AND':
				arm_instruct.AND(parser[3],parser[4], parser[5])
			case 'MUL':
				arm_instruct.MUL(parser[3],parser[4], parser[5])
			case 'MOV':
				arm_instruct.MOV(parser[3],parser[4])
			case 'STR':
				arm_instruct.STR(parser[3], parser[4])
			case 'STRB':
				arm_instruct.STRB(parser[3], parser[4])
			case 'LDR':
				arm_instruct.LDR(parser[3],parser[4])
			case 'LDRB':
				arm_instruct.LDRB(parser[3], parser[4])
			case 'NOP':
				pass
			case 'B':
				x = arm_instruct.B(x, parser[3])
				continue
			case 'B.GT':
				x = arm_instruct.BGT(x, parser[3])
				continue
			case 'B.LE':
				x = arm_instruct.BLE(x, parser[3])
				continue
			case 'CMP':
				arm_instruct.CMP(parser[3], parser[4])
			case 'RET':
				regPrint()
				stack.stackPrint()
				fileIn.close()
				return 0
			case _:
				print("Error: Instruction not found.")
		x += 1



		operandCounter = 1
		for n in parser[3:]:
			print("Operand", operandCounter, ":", n)	# Print operand (looped)
			operandCounter+=1
		regPrint()				# Print registers every instruction
	#regPrint()					# Print registers at the end of execution
		#stack.stackPrint()		# Print stack every instruction
# FUNCTIONS -----------------------------------------------------------
# operands is a list of the instruction inputs

# Inputs a string, returns a list of independent values from string
def parse(assemLine):	
	parser = re.findall(r"[\.\w]+|\[.*?\]", assemLine)		# Seperates elements by whitespace or comma, keep bracket content together
	return parser

# Print register content
def regPrint():
	print()
	for x, y in registers.items():
		if x != 'N' and x != 'Z' and x != 'V':
			print(f"{x}: {y:#018x}")
		else:
			print(f"{x}: {y}")
main()
