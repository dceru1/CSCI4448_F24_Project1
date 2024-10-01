import re
from arm64em_structures import registers
from arm64em_structures import stackClass
#Function to convert a w reg to a xreg
#def wreg_to_xreg(registers : dict, )



def SUB(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if(arg2.find("x") == 0) and (arg2.find("w") == 0):
        registers[ret] = registers[arg1] - registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] - int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] - int(arg2, 10)
    return

def ADD(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if(arg2.find("x") == 0) or (arg2.find("w") == 0):
        registers[ret] = registers[arg1] + registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] + int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] + int(arg2, 10)
    return

def EOR(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if(arg2.find("x") == 0) and (arg2.find("w") == 0):
        registers[ret] = registers[arg1] ^ registers[arg2]
    # arg2 is a base 16 value
    elif(arg2.find("0x") == 0):
        registers[ret] = registers[arg1] ^ int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] ^ int(arg2, 10)
    return

def AND(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if(arg2.find("x") == 0) and (arg2.find("w") == 0):
        registers[ret] = registers[arg1] & registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] & int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] & int(arg2, 10)
    return

def MUL(ret : str, arg1 : str, arg2 : str):
        # arg2 is another register
    if (arg2.find("x") == 0) or (arg2.find("w") == 0) :
        registers[ret] = registers[arg1] * registers[arg2]
    # arg2 is a base 16 value
    elif(arg2.find("0x") == 0):
        registers[ret] = registers[arg1] * int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] * int(arg2, 10)
    return
    
def MOV(arg1 : str, arg2 : str):
    # arg2 is another register
    if(arg2.find("x") == 0) and (arg2.find("w") == 0) :
        registers[arg1] = registers[arg2]
    # arg2 is a base 16 value
    elif not arg2.find("0x"):
        registers[arg1] = int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[arg1] = int(arg2, 10)
    return
    
def STR(stack : stackClass, arg1 : str, arg2 : str):
    # command includes a STR immediate offset
    if (not arg2.find("[")) and (arg2.find("]")) :
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        if parser[0] == 'sp' and len(parser) > 1:
            stack.push(registers[arg1],int(parser[1]) + int(registers['pc']))
        elif len(parser) == 1:
            stack.push(registers[arg1],registers['pc'])
        else: raise AssertionError(f"Unknown STR register {parser[0]}")
    else: raise AssertionError(f"Cannot perform a STR directly on a register!")
    return
    
def STRB(stack : stackClass, arg1 : str, arg2 : str):
    return
    
def LDR(stack : stackClass, arg1 : str, arg2 : str):
    if (not arg2.find("[")) and (arg2.find("]")) :
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        if parser[0] == 'sp' :
            registers[arg1] = stack.pop(int(parser[1]) + registers['pc'])
        else: raise AssertionError(f"Unknown LDR register {parser[0]}")
    else: raise AssertionError(f"Cannot perform a STR directly on a register!")
    return
    
def LDRB(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def B(x : int, arg1 : str):
    registers['pc'] = int(arg1,16)
    print()
    # divide by 4 so that x knows what line number it was at
    return int(int(arg1,16)/4) - 1

def BGT(x : int, arg1 : str):
    if (registers['Z'] == 0) and (registers['N'] == 1):
        return B(x, arg1)

def BLE(x : int, arg1 : str):
    if (registers['Z'] == 1) and (registers['N'] == 0):
        return B(x, arg1)

def CMP(arg1 : str, arg2 : str):
    if(arg2.find("x") == 0) and (arg2.find("w") == 0):
        res = registers[arg1] - registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        res = registers[arg1] - int(arg2, 16)
    # arg2 is a base 10 value
    else:
        res = registers[arg1] - int(arg2, 10)
    print(res)
    return
    