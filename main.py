import argparse

from debug.disassembler import Disassembler
from debug.instruction import Instruction
from debug.state import MachineState

def parsing_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-j', '--JSON')
    parser.add_argument('-o', '--OPCODE')

    args = parser.parse_args()

    return args

def main():
    args = parsing_arguments()

    if args.JSON:
        file_name = args.JSON
        file_type = 'json'
    elif args.OPCODE:
        file_name = args.OPCODE
        file_type = 'opcode'

    f = open(file_name, 'r')
    
    data = f.read()

    if file_type == 'json':
        data = json.loads(data)
        data = data[opcode]
    
    code = data.replace('\n', '')
    code = Disassembler(code).disassemble()
    
    print code
    
    code = code.split('\n')
    
    mstate = MachineState()
        
    for i in code:
        print '> ', i
        
        print 'PC: ', hex(mstate.pc)
        print 'STACK:  ', mstate.stack.stack
        print 'MEMORY: ', mstate.memory
        
        mstate = Instruction(i).evaluate(mstate)
        
        print ''

    f.close()

if __name__ == '__main__':
    main()
