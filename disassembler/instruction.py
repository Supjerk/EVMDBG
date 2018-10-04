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

    def push_(self, global_state):
        argument = self.assemble.split(' ')[1]

        global_state.mstate.stack.push(argument)

        return global_state


    def pop_(self, global_state):
        global_state.mstate.stack.pop(argument)

        return global_state


    def dup_(self, global_state):
        index = int(self.assemble[3:])
        index = -index
        
        value = global_state.mstate.stack.get(index)
        
        global_state.mstate.stack.push(value)

        return global_state


    def swap_(self, global_state):
        index = int(self.assemble[4:]) + 1
        index = -index
        
        value = global_state.mstate.stack.get(-1)
        target = global_state.mstate.stack.get(index)
        
        global_state.mstate.stack.set(index, value)
        global_state.mstate.stack.set(-1, target)

        return global_state

    
    def add_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a + b)

        return global_state


    def mul_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a * b)

        return global_state


    def sub_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a - b)

        return global_state


    def div_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a // b)

        return global_state

    
    def sdiv_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a // b)

        return global_state


    def mod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a % b)

        return global_state


    def smod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a % b)

        return global_state


    def addmod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()
        N = global_state.mstate.stack.pop()

        global_state.mstate.stack.push((a + b) % N)

        return global_state


    def mulmod_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()
        N = global_state.mstate.stack.pop()

        global_state.mstate.stack.push((a * b) % N)

        return global_state


    def exp_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()
        
        global_state.mstate.stack.push(a ** b)

        return global_state


    def signextend_(self, global_state):
        pass


    def lt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.psuh(a < b)

        return global_state


    def gt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a > b)

        return global_state


    def slt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a < b)

        return global_state


    def sgt_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a > b)

        return global_state


    def eq_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a == b)

        return global_state


    def iszero_(self, global_state):
        a = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a == 0)

        return global_state


    def and_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a & b)

        return global_state


    def or_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a | b)

        return global_state


    def xor_(self, global_state):
        a = global_state.mstate.stack.pop()
        b = global_state.mstate.stack.pop()

        global_state.mstate.stack.push(a ^ b)

        return global_state


    def not_(self, global_state):
        a = global_state.mstate.stack.pop()
        
        global_state.mstate.stack.push(-a)

        return global_state


    def byte_(self, global_state):
        i = global_state.mstate.stack.pop()
        x = global_state.mstate.stack.pop()

        y = (x >> (i * 8)) & 0xFF

        global_state.mstate.stack.push(y)

        return global_state
