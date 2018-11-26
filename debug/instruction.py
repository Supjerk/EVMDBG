from util import list_to_int

class Instruction(object):
    def __init__(self, assemble):
        self.assemble = assemble


    def evaluate(self, global_state):
        assemble = self.assemble.lower()
        
	if self.assemble.startswith('PUSH'):
            assemble = 'push'
        elif self.assemble.startswith('DUP'):
            assemble = 'dup'
        elif self.assemble.startswith('SWAP'):
            assemble = 'swap'
        elif self.assemble.startswith('LOG'):
            assemble = 'log'

        mutator = getattr(self, assemble + '_', None)
        
        return mutator(global_state)

    
    def add_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a + b)
        global_state.mstate.pc += 1

        return global_state


    def mul_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a * b)
        global_state.mstate.pc += 1

        return global_state


    def sub_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a - b)
        global_state.mstate.pc += 1

        return global_state


    def div_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a // b)
        global_state.mstate.pc += 1

        return global_state

    
    def sdiv_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a // b)
        global_state.mstate.pc += 1

        return global_state


    def mod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a % b)
        global_state.mstate.pc += 1

        return global_state


    def smod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a % b)
        global_state.mstate.pc += 1

        return global_state


    def addmod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()
        N = global_state.mstate.stack.pop()

        global_state.mstate.stack.push((a + b) % N)
        global_state.mstate.pc += 1

        return global_state


    def mulmod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()
        N = global_state.mstate.stack.pop()

        global_state.mstate.stack.push((a * b) % N)
        global_state.mstate.pc += 1

        return global_state


    def exp_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()
        
        global_state.mstate.stack.push(a ** b)
        global_state.mstate.pc += 1

        return global_state


    def signextend_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def lt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a < b)
        global_state.mstate.pc += 1

        return global_state


    def gt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a > b)
        global_state.mstate.pc += 1

        return global_state


    def slt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a < b)
        global_state.mstate.pc += 1

        return global_state


    def sgt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a > b)
        global_state.mstate.pc += 1

        return global_state


    def eq_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a == b)
        global_state.mstate.pc += 1

        return global_state


    def iszero_(self, global_state):
        a = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a == 0)
        global_state.mstate.pc += 1

        return global_state


    def and_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a & b)
        global_state.mstate.pc += 1

        return global_state


    def or_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a | b)
        global_state.mstate.pc += 1

        return global_state


    def xor_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a ^ b)
        global_state.mstate.pc += 1

        return global_state


    def not_(self, global_state):
        a = global_state.mstate.stack.pop()
        
        global_state.mstate.stack.push(-a)
        global_state.mstate.pc += 1

        return global_state


    def byte_(self, global_state):
        i = global_state.mstate.stack.pop()
        x = global_state.mstate.stack.pop()

        y = (x >> (i * 8)) & 0xFF

        global_state.mstate.stack.push(y)
        global_state.mstate.pc += 1

        return global_state


    def sha3_(self, global_state):
        '''
        offset = global_state.mstate.stack.pop()
        length = global_state.mstate.stack.pop()

        value = global_state.mstate.memory_read(offset, length)
        hash_data = keccak256(value)

        global_state.mstate.stack.push(hash_data)
        '''
        global_state.mstate.pc += 1

        return global_state


    def address_(self, global_state):
        address = global_state.environment.active_account.address

        global_state.mstate.stack.push(address)
        global_state.mstate.pc += 1

        return global_state


    def balance_(self, global_state):
        addr = global_state.mstate.stack.pop()
        balance = global_state.world_state.accounts[addr].balance

        global_state.mstate.stack.push(balance)
        global_state.mstate.pc += 1

        return global_state


    def origin_(self, global_state):
        origin = global_state.environment.origin

        global_state.mstate.stack.push(origin)
        global_state.mstate.pc += 1

        return global_state


    def caller_(self, global_state):
        caller = global_state.environment.sender

        global_state.mstate.stack.push(caller)
        global_state.mstate.pc += 1

        return global_state


    def callvalue_(self, global_state):
        value = global_state.environment.callvalue

        global_state.mstate.stack.push(value)
        global_state.mstate.pc += 1

        return global_state


    def calldataload_(self, global_state):
        i = global_state.mstate.stack.pop()
        data = int(global_state.environment.calldata[i+2:i+66], 16)

        global_state.mstate.stack.push(data)
        global_state.mstate.pc += 1

        return global_state

    
    def calldatasize_(self, global_state):
        size = len(hexencode_to_string(str(global_state.environment.calldata)))
        
        global_state.mstate.stack.push(size)
        global_state.mstate.pc += 1

        return global_state

    
    def calldatacopy(self, global_state):
        dest = global_state.mstate.stack.pop()
        offset = global_state.mstate.stack.pop()
        length = global_state.mstate.stack.pop()

        data = global_state.environment.calldata[offset:offset+length]
        global_state.mstate.memory_write(dest, data)
        global_state.mstate.pc += 1

        return global_state


    def codesize_(self, global_state):
        size = len(global_state.environment.active_account.code)

        global_state.mstate.stack.push(size)
        global_state.mstate.pc += 1

        return global_state


    def codecopy_(self, global_state):
        dest = global_state.mstate.stack.pop()
        offset = global_state.mstate.stack.pop()
        length = global_state.mstate.stack.pop()

        data = int(global_state.environment.active_account.code[offset:offset+length], 16)
        global_state.mstate.memory_write(dest, data, length=length)
        global_state.mstate.pc += 1

        return global_state

 
    def gasprice_(self, global_state):
        gasprice = global_state.environment.gasprice

        global_state.mstate.stack.push(gasprice)
        global_state.mstate.pc += 1

        return global_state


    def extcodesize_(self, global_state):
        addr = global_state.mstate.stack.pop()
        size = len(global_state.world_state.accounts[addr].code)

        global_state.mstate.stack.push(size)
        global_state.mstate.pc += 1

        return global_state


    def extcodecopy_(self, global_state):
        addr = global_state.mstate.stack.pop()
        dest = global_state.mstate.stack.pop()
        offset = global_state.mstate.stack.pop()
        length = global_state.mstate.stack.pop()

        data = global_state.world_state.accounts[addr].code[offset:offset+length]
        global_state.mstate.memory_write(dest, data)
        global_state.mstate.pc += 1

        return global_state


    def returndatasize_(self, global_state):
        size = len(global_state.last_return_data)

        global_state.mstate.stack.push(size)
        global_state.mstate.pc += 1

        return global_state


    def returndatacopy_(self, global_state):
        dest = global_state.mstate.stack.pop()
        offset = global_state.mstate.stack.pop()
        length = global_state.mstate.stack.pop()

        data = global_state.last_return_data[offset:offset+length]
        global_state.mstate.memory_write(dest, data)
        global_state.mstate.pc += 1

        return global_state

    ########## Block Instruction ##########
    def blockhash_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def coinbase_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def timestamp_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def number_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def difficulty_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def gaslimit_(self, global_state):
        global_state.mstate.pc += 1

        return global_state
    ########## Block Instruction ##########

    def pop_(self, global_state):
        global_state.mstate.stack.pop()
        global_state.mstate.pc += 1

        return global_state
    
    
    def mload_(self, global_state):
        offset = global_state.mstate.stack.pop()
        value = list_to_int(global_state.mstate.memory[offset:offset+32])

        global_state.mstate.stack.push(value)
        global_state.mstate.pc += 1

        return global_state


    def mstore_(self, global_state):
        offset = global_state.mstate.stack.pop()
        value = global_state.mstate.stack.pop()
        
        global_state.mstate.memory_write(offset, value)
        global_state.mstate.pc += 1
    
        return global_state


    def mstore8_(self, global_state):
        offset = global_state.mstate.stack.pop()
        value = chr(global_state.mstate.stack.pop() & 0xff)

        global_state.mstate.memory_write(offset, value)
        global_state.mstate.pc += 1

        return global_state


    def sload_(self, global_state):
        key = global_state.mstate.stack.pop()
        
        try:
            value = global_state.environment.active_account.storage._storage[key]
        except:
            pass
        global_state.mstate.stack.push(value)
        global_state.mstate.pc += 1

        return global_state


    def sstore_(self, global_state):
        key = global_state.mstate.stack.pop()
        value = global_state.mstate.stack.pop()

        global_state.environment.active_account.storage._storage[key] = value
        global_state.mstate.pc += 1

        return global_state


    def jump_(self, global_state):
        dest = global_state.mstate.stack.pop()
        global_state.mstate.pc = dest

        return global_state


    def jumpi_(self, global_state):
        dest = global_state.mstate.stack.pop()
        condition = global_state.mstate.stack.pop()

        if condition:
            global_state.mstate.pc = dest
        else:
            global_state.mstate.pc += 1

        return global_state


    def pc_(self, global_state):
        pc = global_state.mstate.pc
        
        global_state.mstate.stack.push(pc)
        global_state.mstate.pc += 1

        return global_state


    def msize_(self, global_state):
        size = len(global_state.mstate.memory)

        global_state.mstate.stack.push(size)
        global_state.mstate.pc += 1

        return global_state


    def gas_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def jumpdest_(self, global_state):
        global_state.mstate.pc += 1

        return global_state


    def push_(self, global_state):
        length = int(self.assemble.split(' ')[0][4:])
        argument = int(self.assemble.split(' ')[1], 16)

        global_state.mstate.stack.push(argument)
        global_state.mstate.pc += (1 + length)

        return global_state


    def dup_(self, global_state):
        index = int(self.assemble[3:])
        index = -index
        
        value = global_state.mstate.stack.get(index)
        
        global_state.mstate.stack.push(value)
        global_state.mstate.pc += 1

        return global_state


    def swap_(self, global_state):
        index = int(self.assemble[4:]) + 1
        index = -index
        
        value = global_state.mstate.stack.get(-1)
        target = global_state.mstate.stack.get(index)
        
        global_state.mstate.stack.set(index, value)
        global_state.mstate.stack.set(-1, target)
        global_state.mstate.pc += 1

        return global_state


    def log_(self, global_state):
        offset = global_state.mstate.stack.pop()
        length = global_state.mstate.stack.pop()
        depth = int(self.op_code[3:])
        topic = [global_state.mstate.stack.pop() for _ in range(depth)]
        
        memory = global_state.mstate.memory[offset:offset+length]

        print memory, topic

        global_state.mstate.pc += 1

        return global_state


    def revert_(self, global_state):
        return None


    def assert_(self, global_state):
        return None
