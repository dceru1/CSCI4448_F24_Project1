import re
from arm64em_structures import registers,stack
#Function to convert a w reg to a xreg
#def wreg_to_xreg(registers : dict, )



def SUB(ret : str, arg1 : str, arg2 : str):
    if ret.find("w") == 0:
        ret = "x" + ret[1]
    if arg1.find("w") == 0:
        arg1 = "x" + arg1[1]
    if arg2.find("w") == 0:
        arg2 = "x" + arg2[1]
    if arg2.find("x") == 0:
        registers[ret] = registers[arg1] - registers[arg2]
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] - int(arg2, 16)
    else:
        registers[ret] = registers[arg1] - int(arg2, 10)
    return

def ADD(ret : str, arg1 : str, arg2 : str):
    if ret.find("w") == 0:
        ret = "x" + ret[1]
    if arg1.find("w") == 0:
        arg1 = "x" + arg1[1]
    if arg2.find("w") == 0:
        arg2 = "x" + arg2[1]
    if arg2.find("x") == 0:
        registers[ret] = registers[arg1] + registers[arg2]
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] + int(arg2, 16)
    else:
        registers[ret] = registers[arg1] + int(arg2, 10)
    return

def EOR(ret : str, arg1 : str, arg2 : str):
    if ret.find("w") == 0:
        ret = "x" + ret[1]
    if arg1.find("w") == 0:
        arg1 = "x" + arg1[1]
    if arg2.find("w") == 0:
        arg2 = "x" + arg2[1]
    if arg2.find("x") == 0:
        registers[ret] = registers[arg1] ^ registers[arg2]
    elif(arg2.find("0x") == 0):
        registers[ret] = registers[arg1] ^ int(arg2, 16)
    else:
        registers[ret] = registers[arg1] ^ int(arg2, 10)
    return

def AND(ret : str, arg1 : str, arg2 : str):
    if ret.find("w") == 0:
        ret = "x" + ret[1]
    if arg1.find("w") == 0:
        arg1 = "x" + arg1[1]
    if arg2.find("w") == 0:
        arg2 = "x" + arg2[1]
    print(ret,arg1,arg2)
    if arg2.find("x") == 0:
        registers[ret] = registers[arg1] & registers[arg2]
    elif(not arg2.find("0x")):
        registers[ret] = registers[arg1] & int(arg2, 16)
    else:
        registers[ret] = registers[arg1] & int(arg2, 10)
    return

def MUL(ret : str, arg1 : str, arg2 : str):
    if ret.find("w") == 0:
        ret = "x" + ret[1]
    if arg1.find("w") == 0:
        arg1 = "x" + arg1[1]
    if arg2.find("w") == 0:
        arg2 = "x" + arg2[1]
    registers[ret] = registers[arg1] * registers[arg2]
    
def MOV(arg1 : str, arg2 : str):
    if arg1.find("w") == 0:
        arg1 = "x" + arg1[1]
    if arg2.find("w") == 0:
        arg2 = "x" + arg2[1]
    if(arg2.find("x") == 0 or arg2 == 'sp'):
        registers[arg1] = registers[arg2]
    # arg2 is a base 16 value
    elif not arg2.find("0x"):
        registers[arg1] = int(arg2, 16)
    # arg2 is a base 10 value
    else:
        registers[arg1] = int(arg2, 10)
    return
    
def STR(arg1 : str, arg2 : str):
    # command includes a STR immediate offset
    if (not arg2.find("[")) and (arg2.find("]")) :
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        if parser[0] == 'sp' and len(parser) > 1:
            if arg1.find('x') == 0:
                num = registers[arg1].to_bytes(length=16)
            elif arg1.find('w') == 0:
                num = registers[arg1].to_bytes(length=8)
            stack.push(num,int(parser[1]))
        elif len(parser) == 1:
            if arg1.find('x') == 0:
                num = registers[arg1].to_bytes(length=16)
            elif arg1.find('w') == 0:
                num = registers[arg1].to_bytes(length=8)
            stack.push(num)
        else: raise AssertionError(f"Unknown STR register {parser[0]}")
    else: raise AssertionError(f"Cannot perform a STR directly on a register!")
    return
    
def STRB(arg1 : str, arg2 : str):
    if (not arg2.find("[")) and (arg2.find("]")):
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        arg1 = 'x' + arg1[1]
        if parser[1].find("x") == 0:
            stackOffset = registers[parser[0]] - stack.pointer + registers[parser[1]]
        else:
            stackOffset = registers[parser[0]] - stack.pointer + int(parser[1])
        arg2Bytes = registers[arg1].to_bytes(length=1)
        stack.push(arg2Bytes, stackOffset)
    return
    
def LDR(arg1 : str, arg2 : str):
    if (not arg2.find("[")) and (arg2.find("]")) :
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        if parser[0] == 'sp' and len(parser) > 1:
            if arg1.find('x') == 0:
                registers[arg1] = stack.pop(int(parser[1]), 0)
            elif arg1.find('w') == 0:
                registers[arg1] = stack.pop(int(parser[1]), 1)
        elif len(parser) == 1:
            if arg1.find('x') == 0:
                registers[arg1] = stack.pop(0, 0)
            elif arg1.find('w') == 0:
                registers[arg1] = stack.pop(0, 1)
        else: raise AssertionError(f"Unknown LDR register {parser[0]}")
    else: raise AssertionError(f"Cannot perform a LDR directly on a register!")
    return
    
def LDRB(arg1 : str, arg2 : str):
    if (not arg2.find("[")) and (arg2.find("]")):
        parser = re.findall(r"[\w]+|^\[.*?^\]", arg2)
        arg1 = 'x' + arg1[1]
        if parser[1].find("x") == 0:
            stackOffset = registers[parser[0]] - stack.pointer + registers[parser[1]]
        else:
            stackOffset = registers[parser[0]] - stack.pointer + int(parser[1])
        arg2Bytes = registers[arg1].to_bytes(length=1)
        stack.push(arg2Bytes, stackOffset)
    return

def B(x : int, arg1 : str):
    registers['pc'] = int(arg1,16)
    # divide by 4 so that x knows what line number it was at
    return int(int(arg1,16)/4)

def BGT(x : int, arg1 : str):
    if (registers['Z'] == 0) and (registers['N'] == registers['V']):
        return B(x, arg1)
    return x + 1

def BLE(x : int, arg1 : str):
    if (registers['Z'] != 0) or (registers['N'] != registers['V']):
        return B(x, arg1)
    return x + 1

def CMP(arg1 : str, arg2 : str):
    # ARM 64 flag set docs
    # https://developer.arm.com/documentation/100076/0100/A64-Instruction-Set-Reference/Condition-Codes/Condition-flags?lang=en
    if arg1.find("w") == 0:
        arg1[0] = 'x'
    if arg2.find("w") == 0:
        arg2[0] = 'x'
    if(arg2.find("x") == 0):
        res = registers[arg1] - registers[arg2]
    # arg2 is a base 16 value
    elif(arg2.find("0x") != -1):
        res =  registers[arg1] - int(arg2, 16)
    # arg2 is a base 10 value
    else:
        res = registers[arg1] -  int(arg2, 10)
    # Z flag set if res is zero
    if res == 0:
        print("Z flag raised")
        registers['Z'] = 1
    else:
        registers['Z'] = 0

    # V flag set iff res is the result of a signed overflow
    # We can determine overflow by taking 2's compliment and comparing it to the result
    # (both values have to be absolute)
    resOF = abs(~res + 1)
    if resOF != abs(res):
        print("V flag raised")
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
    