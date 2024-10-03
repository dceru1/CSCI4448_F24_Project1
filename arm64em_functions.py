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
            stack.push(registers[arg1],int(parser[1]))
        elif len(parser) == 1:
            stack.push(registers[arg1])
        else: raise AssertionError(f"Unknown STR register {parser[0]}")
    else: raise AssertionError(f"Cannot perform a STR directly on a register!")
    return
    
def STRB(stack : stackClass, arg1 : str, arg2 : str):
    if (not arg2.find("[")) and (arg2.find("]")) :
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        stack.push(registers[arg1],int(parser[1]) + int())
    else: raise AssertionError(f"Cannot perform a STR directly on a register!")
    return
    
def LDR(stack : stackClass, arg1 : str, arg2 : str):
    if (not arg2.find("[")) and (arg2.find("]")) :
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        if parser[0] == 'sp' :
            registers[arg1] = stack.pop(int(parser[1]))
        else: raise AssertionError(f"Unknown LDR register {parser[0]}")
    else: raise AssertionError(f"Cannot perform a LDR directly on a register!")
    return
    
def LDRB(registers : dict, ret : str, arg1 : str, arg2 : str):
    return

def B(x : int, arg1 : str):
    registers['pc'] = int(arg1,16)
    print()
    # divide by 4 so that x knows what line number it was at
    return int(int(arg1,16)/4)

def BGT(x : int, arg1 : str):
    if (registers['Z'] == 0) and (registers['N'] == registers['V']):
        return B(x, arg1)
    return x + 1

def BLE(x : int, arg1 : str):
    if (registers['Z'] != 0) and (registers['N'] != registers['V']):
        return B(x, arg1)
    return x + 1

def CMP(arg1 : str, arg2 : str):
    # ARM 64 flag set docs
    # https://developer.arm.com/documentation/100076/0100/A64-Instruction-Set-Reference/Condition-Codes/Condition-flags?lang=en
    xreg = None
    if(arg2.find("x") == 0):
        res = registers[arg1] - registers[arg2]
        xreg = True
    elif(arg2.find("w") == 0):
        res = registers[arg1] - registers[arg2]
        xreg = False
    # arg2 is a base 16 value
    elif(arg2.find("0x") != -1):
        res =  registers[arg1] - int(arg2, 16)
    # arg2 is a base 10 value
    else:
        res = registers[arg1] -  int(arg2, 10)
    print(res)
    # Z flag set if res is zero
    if(res is 0):
        print("Z flag raised")
        registers['Z'] = 1
    else:
        registers['Z'] = 0

    # V flag set iff res is the result of a signed overflow
    if xreg is True and (res > 0x0fffffffffffffff or res < -0x0fffffffffffffff):
        print("V flag raised (x)")
        registers['V'] = 1
    elif(xreg is False and (res > 0x0fffffff or res < -0x0fffffff)):
        print("V flag raised (w)")
        registers['V'] = 1
    else:
        registers['V'] = 0
    
    # N is set if res < 0
    if res < 0:
        print("N flag raised")
        registers['N'] = 1
    else:
        registers['N'] = 0
    return
    