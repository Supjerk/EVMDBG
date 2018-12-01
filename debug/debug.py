from instruction import Instruction

class Logger:
    def __init__(self, symbol):
        self.symbol = symbol

    
    def end_logger(self):
        self._logger('END', 'END OF TRANSACTION')


    def information_logger(self):
        self._logger('PC', hex(self.symbol.global_state.mstate.pc))
        self._logger('STACK', self.symbol.global_state.mstate.stack.stack)
        self._logger('MEMORY', self.symbol.global_state.mstate.memory)
        self._logger('STORAGE', self.symbol.environment.active_account.storage._storage, end='\n')
        

    def _logger(self, state, value, end=''):
        print state, ':\t', value, end


class Information:
    def __init__(self, symbol):
        self.symbol = symbol


    def memory(self):
        memory = self.symbol.global_state.mstate.memory
        length = len(memory)
        
        print '=' * 16, 'memory', '=' * 16
        
        if memory != []:
            for i in range(0, length, 8):
                print str(i).rjust(4, '0'), '|\t', self.memory_to_string(i, 8)
            print '=' * 40
        else:
            print '=' * 13, 'Empty Memory', '=' * 13
        
    
    def memory_to_string(self, index, size):
        memory = self.symbol.global_state.mstate.memory
        
        value = ''
     
        for i in range(index, index+size):
            value += str(memory[i]).rjust(2, '0')
            value += '  '

        return value


    def stack(self):
        stack = self.symbol.global_state.mstate.stack.stack
        length = len(stack)

        print '=' * 16, 'stack', '=' * 17

        if stack != []:
            for i in range(0, length):
                print str(i).rjust(4, '0'), '|\t', stack[i]
            print '=' * 40
        else:
            print '=' * 13, 'Empty Stack', '=' * 14


class Symbol:
    def __init__(self, account, environment, world_state, global_state):
        self.account = account
        self.environment = environment
        self.world_state = world_state
        self.global_state = global_state


class Trace:
    def __init__(self, code, account, environment, world_state, global_state):
        self.bp = []
        self.break_flag = False

        self.code = code
        self.code_length = len(code)
        self.current_code_index = 0
        
        self.symbol = Symbol(account, environment, world_state, global_state)
        self.logger = Logger(self.symbol)
        self.info = Information(self.symbol)


    def run(self, view=False):
        for i in range(self.code_length):
            try:
                pc = self.symbol.global_state.mstate.pc
                if not self.break_flag:
                    self.logger._logger('INS', self.code[pc])

                    if view:
                        self.logger.information_logger()
                
                if pc in self.bp and not self.break_flag:
                    self.break_flag = True
                    break
                else:
                    self.break_flag = False
            
                self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
            except:
                self.logger.end_logger()
                
                return False


    def continued(self, view=False):
        start = self.symbol.global_state.mstate.pc

        for i in range(start, self.code_length):
            try:
                pc = self.symbol.global_state.mstate.pc

                if not self.break_flag:
                    self.logger._logger('INS', self.code[pc])

                    if view:
                        self.logger.information_logger()
                
                if pc in self.bp and not self.break_flag:
                    self.break_flag = True
                    break
                else:
                    self.break_flag = False
                
                self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
            except:
                self.logger.end_logger()

                return False


    def next(self, view=False):
        try:
            pc = self.symbol.global_state.mstate.pc
        
            self.logger._logger('INS', self.code[pc])
            
            if view:
                self.logger.information_logger()
            
            self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
        except:
            self.logger.end_logger()
            self.symbol.global_state = False

            return False


    def add_breakpoint(self, pc):
        self.bp.append(pc)


    def del_breakpoint(self, index):
        try:
            self.bp.pop(index)
        except:
            print 'Not found index'

    def view_breakpoint(self):
        length = len(self.bp)

        if self.bp != []:
            for i in range(0, length):
                print str(i).rjust(4, '0'), '|\t', self.bp[i]
        else:
            print 'None'
