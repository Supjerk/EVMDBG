from instruction import Instruction

class Logger:
    def __init__(self, symbol):
        self.symbol = symbol

    
    def revert_logger(self):
        self._logger('REVERT', 'TRANSACTION REVERT')


    def infomation_logger(self):
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
            pc = self.symbol.global_state.mstate.pc

            self.logger._logger('INS', self.code[pc])
            
            if view:
                self.logger.infomation_logger()
            elif pc in self.bp:
                self.logger.infomation_logger()
                break
            
            self.symbol.global_state = Instruction(self.code[pc]).evaluate(self.symbol.global_state)
            
            if not self.symbol.global_state:
                self.logger.revert_logger()
                break


    def continued(self, view=False):
        current = self.current_code_index

        for i in range(self.current_code_index, self.code_length):
            self.current_code_index += 1

            if view:
                self.logger.information_logger()
            elif self.symbol.global_state.mstate.pc in self.bp:
                self.infomation_logger()
                break

            self.logger._logger('INS', self.code[i])
            self.symbol.global_state = Instruction(self.code[i]).evaluate(self.symbol.global_state)
            
            if not self.symbol.global_state:
                self.logger.revert_logger()
                break


    def next(self, view=False):
        index = self.current_code_index + 1
        if view:
            self.logger.information_logger()
        elif self.symbol.global_state.mstate.pc in self.bp:
            self.logger.information_logger()

        self.logger._logger('INS', self.code[index])
        self.symbol.global_state = Instruction(self.code[index]).evaluate(self.symbol.global_state)
        
        if not self.symbol.global_state:
            self.logger.revert_logger()


    def add_break_point(self, pc):
        self.bp.append(pc)  
