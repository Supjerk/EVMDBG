import argparse

from debug.disassembler import Disassembler
from debug.instruction import Instruction
from debug.state import GlobalState, WorldState, Account, Environment
from debug.debug import Trace

def parsing_arguments():
    parser = argparse.ArgumentParser()

    parser.add_argument('-j', '--JSON')
    parser.add_argument('-o', '--OPCODE')
    parser.add_argument('-i', '--INFO')

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

    f.close()

    if file_type == 'json':
        data = json.loads(data)
        data = data[opcode]
    
    code = data.replace('\n', '')
    code = Disassembler(code).disassemble()  
    code = code.split('\n')

    if args.INFO:
        file_name = args.INFO
        f = open(file_name, 'r')

        data = f.read().replace(' ', '').split('\n')

        address = data[0].split(':')[1]
        balance = int(data[1].split(':')[1])
        sender = data[2].split(':')[1]
        calldata = data[3].split(':')[1]
        gasprice = int(data[4].split(':')[1])
        callvalue = bool(data[5].split(':')[1].lower() == 'true')
        origin = data[6].split(':')[1]

        f.close()
    else:
        address = raw_input('ADDRESS: ')
        balance = int(raw_input('BALANCE: '))
        sender = raw_input('SENDER: ')
        calldata = raw_input('CALL DATA: ')
        gasprice = int(raw_input('GAS PRICE: '))
        callvalue = bool(raw_input('CALL VALUE: ').lower() == 'true')
        origin = raw_input('ORIGIN: ')

    # Target Contract
    account = Account(address, code=data, balance=balance)
    # environment 
    environment = Environment(account, sender, calldata, gasprice, callvalue, origin)
    # etherum world state
    world_state = WorldState()
    # etherum global state (evm all of state)
    global_state = GlobalState(world_state, environment)
    
    trace = Trace(code, account, environment, world_state, global_state)
    
    trace.add_break_point(0x2)
    trace.run(view=True)
    trace.continued(view=True)

'''
    for i in range(0, 3):
        trace.next(view=True)
    
        if global_state == None:
            break

    print 'NEXT -> CONTINUE TEST'

    trace.continued()
'''

if __name__ == '__main__':
    main()
