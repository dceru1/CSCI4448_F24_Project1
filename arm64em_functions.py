
def SUB(registers : dict, ret : str, arg1 : str, arg2 : str):
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

def ADD(registers : dict, ret : str, arg1 : str, arg2 : str):
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

def EOR(registers : dict, ret : str, arg1 : str, arg2 : str):
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

def AND(registers : dict, ret : str, arg1 : str, arg2 : str):
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

def MUL(registers : dict, ret : str, arg1 : str, arg2 : str):
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
    
def MOV(registers : dict, arg1 : str, arg2 : str):
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
    
def STR(registers : dict, ret : str, arg1 : str, arg2 : str):
    # arg2 is another register
    if( (not arg2.find("x"))):
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
    
def NOP():
    return

def B(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def BGT(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def BLE(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def CMP(registers : dict, ret : str, arg1 : str, arg2 : str):
    return
    