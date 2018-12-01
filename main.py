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
    end = True

    while True:
        if end == False:
            break

        menu = raw_input('>> ') + ' dump'
        menu = menu.split(' ')
        
        if menu[0] == 'next':
            end = trace.next(view=(menu[1] == 'True'))
        elif menu[0] == 'continue':
            end = trace.continued(view=(menu[1] == 'True'))
        elif menu[0] == 'run':
            end = trace.run(view=(menu[1] == 'True'))
        elif menu[0] == 'addbp':
            trace.add_breakpoint(int(menu[1]))
        elif menu[0] == 'delbp':
            trace.del_breakpoint(int(menu[1]))
        elif menu[0] == 'bp':
            trace.view_breakpoint()
        elif menu[0] == 'memory':
            trace.info.memory()
        elif menu[0] == 'stack':
            trace.info.stack()
        elif menu[0] == 'exit':
            break
        else:
            print menu[0] + 'is not found'

    '''
    for i in range(0, 20):
        end = trace.next(view=True)
        
        if end == False:
            break

        trace.info.stack()
        print ''
        trace.info.memory()

        menu = raw_input()
    '''

if __name__ == '__main__':
    main()
