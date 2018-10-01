from opcode import Opcode

def check_instruction(opcode):
    try:
        instruction = Opcode(opcode).name
    except ValueError:
        instruction = 'INVALID'

    if instruction.startswith('PUSH'):
        arg = int(instruction[4:])
    else:
        arg = 0

    return instruction, arg


class Instruction(object):
    def __init__(self, opcode):
        self.opcode = opcode


    def evaluate(self):
        pass
