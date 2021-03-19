import os
import sys
import re
import executebf

path = os.path.join(os.getcwd(),os.path.basename(sys.argv[0]))

def executePath(path):
    file = open(path)
    program = file.read()
    file.close()
    
    program = program.split("\"\"\"")
    if(len(program) < 2):
        print("no bf program to execute")
        return False
    program = re.sub("[^\<\>\+\-\.\,\[\]]","",program[1])
    if(not program):
        print("no bf program to execute")
        return False
    print("executing the bf program: "+program)
    result = executebf.executebf(program)
    print("result: "+result)

executePath(path)
