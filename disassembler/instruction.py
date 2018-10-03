from state import GlobalState

class Instruction(object):
    def __init__(self, assemble):
        self.assemble = self.assemble


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
