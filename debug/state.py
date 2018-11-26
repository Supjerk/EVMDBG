class Storage:
    def __init__(self, address=None):
        self._storage = {}
        self.address = address


    def __setitem__(self, key, value):
        self._storage[key] = value


class Account:
    def __init__(self, address, code=None, contract_name='unknown', balance=None):
        self.nonce = 0
        self.code = code
        self.balance = balance
        self.storage = Storage(address=address)
        
        self.address = address
        self.contract_name = contract_name

        self.deleted = False

    
    def set_balance(self, balance):
        self.balance = balance    


class Environment:
    def __init__(self, active_account, sender, calldata, gasprice, callvalue, origin, code=None):
        self.active_account = active_account
        self.active_function_name = ''

        self.code = active_account.code if code is None else code

        self.sender = sender
        self.calldata = calldata
        self.gasprice = gasprice
        self.origin = origin
        self.callvalue = callvalue


class MachineStack:
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
        self.call_depth = []
        self.depth = 0


    def memory_extend(self, start, size):
        memory_size = self._memory_size()

        if memory_size > start + size:
            return

        memory_extend_size = (start + size - memory_size)
        self.memory.extend(bytearray(memory_extend_size))


    def memory_write(self, offset, data):
        self.memory_extend(offset, len(data))
        self.memory[offset:offset+len(data)] = data


    def _memory_size(self):
        return len(self.memory)


class GlobalState:
    def __init__(self, world_state, environment, machine_state=None, transaction_stack=None, last_return_data=None):
        # self.node = node
        self.world_state = world_state
        self.environment = environment
        self.mstate = machine_state if machine_state else MachineState(gas=10000000)
        self.transaction_stack = transaction_stack if transaction_stack else []
        self.op_code = ''
        self.last_return_data = last_return_data


    def __del__(self):
        pass

class WorldState:
    def __init__(self, transaction_sequence=None):
        self.accounts = {}
        self.node = None
        self.transaction_sequence = transaction_sequence or []

    
    def create_account(self, balance=0, address=None):
        address = address if address else self._generate_new_address()
        new_account = Account(address, balance=balance)
        
        self._put_account(new_account)
        
        return new_account


    def create_initialized_contract_account(self, contract_code, storage):
        new_account = Account(self._generate_new_address(), code=contract_code, balance=0)
        new_account.storage = storage
        self._put_account(new_account)


    def _generate_new_address(self):
        while True:
            address = '0x' + ''.join([str(hex(randint(0, 16)))[-1] for _ in range(20)])
            
            if address not in self.accounts.keys():
                return address


    def _put_account(self, account):
        self.accounts[account.address] = account
