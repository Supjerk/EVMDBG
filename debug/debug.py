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


class Symbol:
    def __init__(self, account, environment, world_state, global_state):
        self.account = account
        self.environment = environment
        self.world_state = world_state
        self.global_state = global_state


class Trace:
    def __init__(self, code, account, environment, world_state, global_state):
        self.bp = []

        self.code = code
        self.code_length = len(code)
        self.current_code_index = 0
        
        self.symbol = Symbol(account, environment, world_state, global_state)
        self.logger = Logger(self.symbol)


    def run(self, view=False):
        for i in range(self.code_length):
            try:
                pc = self.symbol.global_state.mstate.pc

                if pc in self.bp:
                    break
            
                self.logger._logger('INS', self.code[pc])
                
                if view:
                    self.logger.information_logger()

                self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
            except:
                self.logger.end_logger()
                
                return None

    def continued(self, view=False):
        start = self.symbol.global_state.mstate.pc

        for i in range(start, self.code_length):
            try:
                pc = self.symbol.global_state.mstate.pc

                if pc in self.bp:
                    break
                
                self.logger._logger('INS', self.code[pc])

                if view:
                    self.logger.information_logger()

                self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
            

            except:
                self.logger.end_logger()

                return None

    def next(self, view=False):
        try:
            pc = self.symbol.global_state.mstate.pc
        
            if view:
                self.logger.information_logger()
            
            self.logger._logger('INS', self.code[pc])
            self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
        except:
            self.logger.end_logger()
            self.symbol.global_state = None

            return None

    def add_break_point(self, pc):
        self.bp.append(pc)  
