from state import global_sate

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
