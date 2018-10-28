import argparse

from debug.disassembler import Disassembler
from debug.instruction import Instruction
from debug.state import GlobalState, WorldState, Account, Environment
from debug.debug import Trace

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
    code = code.split('\n')
    
    # Target Contract
    account = Account('0xbA9A0426C28d2fc5873C78063F18e5790D0115eC', code=data, balance=5000000000000000000)
    # environment 
    environment = Environment(account, 0x44a4bC2C9C1D8d819923Ad0d6c80BC0D7DE667A5, '0x4df7e3d000000000000000000000000000000000000000000000000000000000', 500000000000000000, 0, 0x44a4bC2C9C1D8d819923Ad0d6c80BC0D7DE667A5)
    # etherum world state
    world_state = WorldState()
    # etherum global state (evm all of state)
    global_state = GlobalState(world_state, environment)
    print code
    trace = Trace(code, account, environment, world_state, global_state)
    trace.run(view=True)

    f.close()

if __name__ == '__main__':
    main()
