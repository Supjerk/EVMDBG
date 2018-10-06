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
		
        return mutator(mstate)

    def push_(self, mstate):
        argument = self.assemble.split(' ')[1]

        mstate.stack.push(argument)

        return mstate


    def pop_(self, mstate):
        mstate.stack.pop(argument)

        return mstate


    def dup_(self, mstate):
        index = int(self.assemble[3:])
        index = -index
        
        value = mstate.stack.get(index)
        
        mstate.stack.push(value)

        return mstate


    def swap_(self, mstate):
        index = int(self.assemble[4:]) + 1
        index = -index
        
        value = mstate.stack.get(-1)
        target = mstate.stack.get(index)
        
        mstate.stack.set(index, value)
        mstate.stack.set(-1, target)

        return mstate

    
    def add_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a + b)

        return mstate


    def mul_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a * b)

        return mstate


    def sub_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a - b)

        return mstate


    def div_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a // b)

        return mstate

    
    def sdiv_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a // b)

        return mstate


    def mod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a % b)

        return mstate


    def smod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a % b)

        return mstate


    def addmod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()
        N = mstate.stack.pop()

        mstate.stack.push((a + b) % N)

        return mstate


    def mulmod_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()
        N = mstate.stack.pop()

        mstate.stack.push((a * b) % N)

        return mstate


    def exp_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()
        
        mstate.stack.push(a ** b)

        return mstate


    def signextend_(self, mstate):
        pass


    def lt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.psuh(a < b)

        return mstate


    def gt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a > b)

        return mstate


    def slt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a < b)

        return mstate


    def sgt_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a > b)

        return mstate


    def eq_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a == b)

        return mstate


    def iszero_(self, mstate):
        a = mstate.stack.pop()

        mstate.stack.push(a == 0)

        return mstate


    def and_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a & b)

        return mstate


    def or_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a | b)

        return mstate


    def xor_(self, mstate):
        a = mstate.stack.pop()
        b = mstate.stack.pop()

        mstate.stack.push(a ^ b)

        return mstate


    def not_(self, mstate):
        a = mstate.stack.pop()
        
        mstate.stack.push(-a)

        return mstate


    def byte_(self, mstate):
        i = mstate.stack.pop()
        x = mstate.stack.pop()

        y = (x >> (i * 8)) & 0xFF

        mstate.stack.push(y)

        return mstate
