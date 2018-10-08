class Instruction(object):
    def __init__(self, assemble):
        self.assemble = assemble


    def evaluate(self, mstate):
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
        print mutator		
        
        return mutator(mstate)

    
    def add_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a + b)
        mstate.pc += 1

        return mstate


    def mul_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a * b)
        mstate.pc += 1

        return mstate


    def sub_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a - b)
        mstate.pc += 1

        return mstate


    def div_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a // b)
        mstate.pc += 1

        return mstate

    
    def sdiv_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a // b)
        mstate.pc += 1

        return mstate


    def mod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a % b)
        mstate.pc += 1

        return mstate


    def smod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a % b)
        mstate.pc += 1

        return mstate


    def addmod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()
        N = mstate.stack.pop()

        mstate.stack.push((a + b) % N)
        mstate.pc += 1

        return mstate


    def mulmod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()
        N = mstate.stack.pop()

        mstate.stack.push((a * b) % N)
        mstate.pc += 1

        return mstate


    def exp_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()
        
        mstate.stack.push(a ** b)
        mstate.pc += 1

        return mstate


    def signextend_(self, mstate):
        mstate.pc += 1

        return mstate


    def lt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a < b)
        mstate.pc += 1

        return mstate


    def gt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a > b)
        mstate.pc += 1

        return mstate


    def slt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a < b)
        mstate.pc += 1

        return mstate


    def sgt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a > b)
        mstate.pc += 1

        return mstate


    def eq_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a == b)
        mstate.pc += 1

        return mstate


    def iszero_(self, mstate):
        a = mstate.stack.pop()

        mstate.stack.push(a == 0)
        mstate.pc += 1

        return mstate


    def and_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a & b)
        mstate.pc += 1

        return mstate


    def or_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a | b)
        mstate.pc += 1

        return mstate


    def xor_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a ^ b)
        mstate.pc += 1

        return mstate


    def not_(self, mstate):
        a = mstate.stack.pop()
        
        mstate.stack.push(-a)
        mstate.pc += 1

        return mstate


    def byte_(self, mstate):
        i = mstate.stack.pop()
        x = mstate.stack.pop()

        y = (x >> (i * 8)) & 0xFF

        mstate.stack.push(y)
        mstate.pc += 1

        return mstate


    def sha3_(self, mstate):
        '''
        offset = mstate.stack.pop()
        length = mstate.stack.pop()

        value = mstate.memory_read(offset, length)
        hash_data = keccak256(value)

        mstate.stack.push(hash_data)
        '''
        mstate.pc += 1

        return mstate


    def address_(self, mstate):
        mstate.pc += 1

        return mstate


    def balance_(self, mstate):
        mstate.pc += 1

        return mstate


    def origin_(self, mstate):
        mstate.pc += 1

        return mstate


    def caller_(self, mstate):
        mstate.pc += 1

        return mstate


    def callvalue_(self, mstate):
        mstate.pc += 1

        return mstate


    def calldataload_(self, mstate):
        mstate.pc += 1

        return mstate

    
    def calldatasize_(self, mstate):
        mstate.stack.push(0x1)
        mstate.pc += 1

        return mstate

    
    def calldatacopy(self, mstate):
        mstate.pc += 1

        return mstate


    def codesize_(self, mstate):
        mstate.pc += 1

        return mstate


    def codecopy_(self, mstate):
        mstate.pc += 1

        return mstate

 
    def gasprice_(self, mstate):
        mstate.pc += 1

        return mstate


    def extcodesize_(self, mstate):
        mstate.pc += 1

        return mstate


    def extcodecopy_(self, mstate):
        mstate.pc += 1

        return mstate


    def returndatasize_(self, mstate):
        mstate.pc += 1

        return mstate


    def returndatacopy_(self, mstate):
        mstate.pc += 1

        return mstate


    def blockhash_(self, mstate):
        mstate.pc += 1

        return mstate


    def coinbase_(self, mstate):
        mstate.pc += 1

        return mstate


    def timestamp_(self, mstate):
        mstate.pc += 1

        return mstate


    def number_(self, mstate):
        mstate.pc += 1

        return mstate


    def difficulty_(self, mstate):
        mstate.pc += 1

        return mstate


    def gaslimit_(self, mstate):
        mstate.pc += 1

        return mstate


    def pop_(self, mstate):
        mstate.stack.pop(argument)
        mstate.pc += 1

        return mstate
    
    
    def mload_(self, mstate):
        offset = mstate.stack.pop()
        value = ord(mstate.memory_read(offset, 32))

        mstate.stack.push(value)
        mstate.pc += 1

        return mstate


    def mstore_(self, mstate):
        offset = mstate.stack.pop()
        value = chr(mstate.stack.pop())
        
        mstate.memory_write(offset, value)
        mstate.pc += 1
    
        return mstate


    def mstore8_(self, mstate):
        offset = mstate.stack.pop()
        value = chr(mstate.stack.pop() & 0xff)

        mstate.memory_write(offset, value)
        mstate.pc += 1

        return mstate


    def sload_(self, mstate):
        mstate.pc += 1

        return mstate


    def sstore_(self, mstate):
        mstate.pc += 1

        return mstate


    def jump_(self, mstate):
        dest = mstate.stack.pop()
        mstate.pc = dest

        return mstate


    def jumpi_(self, mstate):
        dest = mstate.stack.pop()
        condition = mstate.stack.pop()

        if condition:
            mstate.pc = dest
        else:
            mstate.pc += 1

        return mstate


    def pc_(self, mstate):
        pc = mstate.pc
        
        mstate.stack.push(pc)
        mstate.pc += 1

        return mstate


    def msize_(self, mstate):
        mstate.pc += 1

        return mstate


    def gas_(self, mstate):
        mstate.pc += 1

        return mstate


    def jumpdest_(self, mstate):
        mstate.pc += 1

        return mstate


    def push_(self, mstate):
        length = int(self.assemble.split(' ')[0][4:])
        argument = int(self.assemble.split(' ')[1], 16)

        mstate.stack.push(argument)
        mstate.pc += (1 + length)

        return mstate


    def dup_(self, mstate):
        index = int(self.assemble[3:])
        index = -index
        
        value = mstate.stack.get(index)
        
        mstate.stack.push(value)
        mstate.pc += 1

        return mstate


    def swap_(self, mstate):
        index = int(self.assemble[4:]) + 1
        index = -index
        
        value = mstate.stack.get(-1)
        target = mstate.stack.get(index)
        
        mstate.stack.set(index, value)
        mstate.stack.set(-1, target)
        mstate.pc += 1

        return mstate


    def log_(self, mstate):
        # offset = 
        mstate.stack.pop()
        # length = 
        mstate.stack.pop()
        # depth = 
        int(self.op_code[3:])
        # topic = 
        [mstate.stack.pop() for _ in range(depth)]
        
        mstate.pc += 1

        return mstate
