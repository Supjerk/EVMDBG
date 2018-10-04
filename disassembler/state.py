from exception import StackException

class Environment:
    # MSG, TX, etc State
    def __init__(self, active_account, active_function, sender, data, gas_price, value, origin):
        self.active_account = active_account
        self.active_function = active_function
        
        self.sender = sender
        self.data = data
        self.gas_price = gas_price
        self.origin = origin
        self.value = value


class MachineStack:
    # Stack State
    LIMIT_SIZE = 1024

    def __init__(self):
        self.stack = []


    def push(self, argument):
        if len(self.stack) >= self.LIMIT_SIZE:
            raise StackException('Stack is full')
        
        self.stack.append(argument)


    def pop(self):
        if self.stack == []:
            raise StackException('Stack is empty')

        return self.stack.pop()

    
    def get(self, index):
        if self.stack == []:
            raise StackException('Stack is empty')

        if len(self.stack) < abs(index):
            raise StackExecption('Inacccessible index in Stack')

        return self.stack[index]
    
    
    def set(self, index, value):
        if self.stack == []:
            raise StackException('Stack is empty')

        if len(self.stack) < abs(index):
            raise StackExecption('Inaccessible index in Stack')

        self.stack[index] = value


class MachineState:
    # Smart Contract (EVM) State
    def __init__(self, gas):
        self.pc = 0
        self.stack = MachineStack()
        self.memory = []
        self.gas = gas
        self.constraints = []
        self.depth = 0


class GlobalState:
    # Ethereum Block State
    def __init__(self):
        self.mstate = MachineState()


class WorldState:
    # Ethereum World State
    def __init__(self):
        pass
