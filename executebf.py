

def executebf(bf):
    print(bf)
    out = ""
    hexs = "0123456789ABCDEF"
    stack = [0]
    pc = 0#program counter
    ptr = 0#program pointer
    while(True):
        ins = bf[pc]
        if(ins == ">"):
            ptr += 1
            if(ptr == len(stack)):
                #add one cell
                stack.append(0)
        if(ins == "<"):
            ptr -= 1
            if(ptr < 0):
                print("error, buffer overflow, check y' code. pointer smaller than 0")
                return False
        if(ins == "+"):
            stack[ptr] = (stack[ptr]+1)&15
        if(ins == "-"):
            stack[ptr] = (stack[ptr]+15)&15
        if(ins == "."):
            out += hexs[stack[ptr]]
        if(ins == ","):
            print("unsupported synax \",\"")
            # working on it
        if(ins == "["):
            if(stack[ptr] == 0):
                openparens = 0
                while(True):
                    pc += 1;
                    if(openparens == 0 and bf[pc] == "]"):
                        break
                    if(pc >= len(bf)):
                        print("buffer overflow, program counter larger than the program")
                        return False
                    if(bf[pc] == "["):
                        openparens += 1;
                    elif(bf[pc] == "]"):
                        openparens -= 1;
        if(ins == "]"):
            if(stack[ptr] != 0):
                openparens = 0
                while(True):
                    pc -= 1
                    if(openparens == 0 and bf[pc] == "["):
                        break
                    if(pc < 0):
                        print("buffer overflow, program counter lower than 0")
                        return False
                    if(bf[pc] == "]"):
                        openparens += 1;
                    elif(bf[pc] == "["):
                        openparens -= 1;
        pc += 1;
        if(pc >= len(bf)):
            print("execution success, returning")
            break
    return out
