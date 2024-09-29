import re
from arm64em_structures import registers
from arm64em_structures import stackClass
#Function to convert a w reg to a xreg
#def wreg_to_xreg(registers : dict, )



def SUB(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if( (not arg2.find("x")) and (not arg2.find("w")) ):
        registers[ret] = registers[arg1] - registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] - int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] - int(arg2, 10)
    return

def ADD(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if( (not arg2.find("x")) and (not arg2.find("w")) ):
        registers[ret] = registers[arg1] + registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] + int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] + int(arg2, 10)
    return

def EOR(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if( (not arg2.find("x")) and (not arg2.find("w")) ):
        registers[ret] = registers[arg1] ^ registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] ^ int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] ^ int(arg2, 10)
    return

def AND(ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if( (not arg2.find("x")) and (not arg2.find("w")) ):
        registers[ret] = registers[arg1] & registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] & int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] & int(arg2, 10)
    return

def MUL(ret : str, arg1 : str, arg2 : str):
        # arg2 is another register
    if( (not arg2.find("x")) and (not arg2.find("w")) ):
        registers[ret] = registers[arg1] * registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] * int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[ret] = registers[arg1] * int(arg2, 10)
    return
    
def MOV(arg1 : str, arg2 : str):
    # arg2 is another register
    if( (not arg2.find("x")) and (not arg2.find("w")) ):
        registers[arg1] = registers[arg2]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[arg1] = int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[arg1] = int(arg2, 10)
    return
    
def STR(stack : stackClass, arg1 : str, arg2 : str):
    # command includes a STR immediate offset
    if( (not arg2.find("[")) and (arg2.find("]")) ):
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        if(parser[0] == 'sp'):
            stack.p
        registers[arg2] = registers[arg1]
    # arg2 is a base 16 value
    elif(not arg2.find("0x")):
        registers[arg1] = int(arg2[2:], 16)
    # arg2 is a base 10 value
    else:
        registers[arg1] = int(arg2, 10)
    return
    
def STRB(registers : dict, ret : str, arg1 : str, arg2 : str):
    return
    
def LDR(registers : dict, ret : str, arg1 : str, arg2 : str):
    return
    
def LDRB(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def B(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def BGT(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def BLE(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def CMP(registers : dict, ret : str, arg1 : str, arg2 : str):
    return
    