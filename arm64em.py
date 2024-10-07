# Example usage: "python3 arm64em.py test.txt" 


import re
import sys


# Register init-------------------------------
registers = {
	'X1': 0x0000000000000000,
	'X2': 0x0000000000000000,
	'X3': 0x0000000000000000,
	'X4': 0x0000000000000000,
	'X5': 0x0000000000000000,
	'X6': 0x0000000000000000,
	'X7': 0x0000000000000000,
	'X8': 0x0000000000000000,
	'X9': 0x0000000000000000,
	'X10': 0x0000000000000000,
	'X11': 0x0000000000000000,
	'X12': 0x0000000000000000,
	'X13': 0x0000000000000000,
	'X14': 0x0000000000000000,
	'X15': 0x0000000000000000,
	'X16': 0x0000000000000000,
	'X17': 0x0000000000000000,
	'X18': 0x0000000000000000,
	'X19': 0x0000000000000000,
	'X20': 0x0000000000000000,
	'X21': 0x0000000000000000,
	'X22': 0x0000000000000000,
	'X23': 0x0000000000000000,
	'X24': 0x0000000000000000,
	'X25': 0x0000000000000000,
	'X26': 0x0000000000000000,
	'X27': 0x0000000000000000,
	'X28': 0x0000000000000000,
	'X29': 0x0000000000000000,
	'X30': 0x0000000000000000,
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
		parser = re.findall(r"[\w]+|\[.*?\]", x)		# Seperates elements by whitespace or comma, keep bracket content together

		print("\nLine Number:", lineNumber)			# Print line number
		print("Instruction", parser[0])				# Print instruction

		match parser[0]:					# Call instruction function
			case 'SUB':
<<<<<<< Updated upstream
				asmSUB(parser[1:])
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
=======
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
>>>>>>> Stashed changes
			case 'RET':
				asmRET(parser[1:])
			case _:
<<<<<<< Updated upstream
				print("Sorry")
=======
				print("Couldn't read instruction")
		x += 1
>>>>>>> Stashed changes



		operandCounter = 1	#TMP
		for n in parser[1:]:
			print("Operand", operandCounter, ":", n)	# Print operand (looped)
			operandCounter+=1
<<<<<<< Updated upstream

		lineNumber+=1
=======
		regPrint()	# Print each iteration remove comment
		stack.stackPrint()		#Test
		print(registers.items())		# test
	#regPrint()	# Print once at the end of execution remove comment
# FUNCTIONS -----------------------------------------------------------
# operands is a list of the instruction inputs
>>>>>>> Stashed changes


	# Register print --------------------------
	print()
	for x, y in registers.items():
		if x != 'N' and x != 'Z':
			print(f"{x}: {y:#018x}")
		else:
			print(f"{x}: {y}")

<<<<<<< Updated upstream


# FUNCTIONS -----------------------------------------------------------
# operands is a list of the instruction inputs

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




=======
>>>>>>> Stashed changes

main()
