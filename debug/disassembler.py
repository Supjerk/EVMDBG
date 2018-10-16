from opcode import Opcode
from util import hex_decode, split_by_length, list_to_string

class Disassembler(object):
    def __init__(self, opcode):
        self.opcode = opcode


    def disassemble(self):
        op = hex_decode(self.opcode)
        op = split_by_length(op, 2)
         
        count = 0
        end = len(op)
        
        assemble = ['' for _ in range(end)]
        
        while count < end:
            instruction = self._opcode_to_instruction(int(op[count], 16))
            assemble[count], count = self._instruction_with_argument(instruction, op, count)
        
        assemble = list_to_string(assemble, '\n')

        return assemble
   
   
    def _opcode_to_instruction(self, opcode):
        try:
            instruction = Opcode(opcode).name
        except ValueError:
            instruction = 'NOP'

        return instruction


    def _instruction_with_argument(self, instruction, op, count):
        if not instruction.startswith('PUSH'):
            return instruction, count + 1

        length = int(instruction[4:])
        start = count + 1

        argument = op[start:start + length]
        argument = '0x' + list_to_string(argument, '')
        instruction = list_to_string([instruction, argument], ' ')

        return instruction, count + length + 1

