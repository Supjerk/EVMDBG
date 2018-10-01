from opcode import Opcode
from util import hex_decode, split_by_length, list_to_string

class Disassembler(object):
    def __init__(self, opcode):
        self.opcode = opcode


    def disassemble(self):
        op = hex_decode(self.opcode)
        op = split_by_length(op, 2)
         
        end = len(op)
        count = 0
        
        assemble = []

        while count < end:
            instruction, argc = self.instruction(int(op[count], 16))
            
            if argc != 0:
                arg = '0x'

                start = i + 1
                
                for i in range(start, start + argc):
                    arg += op[i]
                
                count += argc

            assemble.append(instruction + arg)
            
            count += 1

        assemble = list_to_string(assemble, '\n')

        return assemble

    def instruction(self, opcode):
        try:
            instruction = Opcode(opcode).name
        except ValueError:
            instruction = 'INVALID'

        if instruction.startswith('PUSH'):
            argc = int(instruction[4:])
        else:
            argc = 0

        return instrcution, argc
