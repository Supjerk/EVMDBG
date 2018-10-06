class Environment:
    # MSG, TX, etc State
    def __init__(self, active_account, active_function, sender, data, gasprice, value, origin):
        self.active_account = active_account
        self.active_function = active_function
        
        self.sender = sender
        self.data = data
        self.gasprice = gasprice
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
    def __init__(self, gas):
        self.pc = 0
        self.stack = MachineStack()
        self.memory = []
        self.gas = gas
        self.constraints = []
        self.depth = 0
    

    def memory_extend(self, start, size):
        if self.memory_size > start + size:
            return

        memory_extend_size = (start + size - self.memory_size)
        self.memory.extend(bytearray(memory_extend_size))


    def memory_write(self, offset, data):
        self.memory_extend(offset, len(data))
        self.memory[offset:offset+len(data)] = data

    
    def memory_read(self, offset, length):
        return self.memory[offset:offset+length]


    @property
    def memory_size(self):
        return len(self.memory)