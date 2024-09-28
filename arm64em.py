import re
import sys



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


		match parser[0]:					
			case 'SUB':
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
			case 'RET':
				asmRET(parser[1:])
			case _:
				print("Sorry")



		operandCounter = 1	#TMP
		for n in parser[1:]:
			print("Operand", operandCounter, ":", n)	# Print operand (looped)
			operandCounter+=1

		lineNumber+=1

	




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





main()
