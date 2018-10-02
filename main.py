from disassembler.disassembler import Disassembler

opcode = "0x608060405260043610610062576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff1680634df7e3d0146100675780638a054ac21461007e578063b4f40c6114610095578063e2179b8e146100ac575b600080fd5b34801561007357600080fd5b5061007c6100c3565b005b34801561008a57600080fd5b50610093610129565b005b3480156100a157600080fd5b506100aa610132565b005b3480156100b857600080fd5b506100c1610134565b005b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561011f57600080fd5b6001600081905550565b60006002905050565b565b600160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff1614151561019057600080fd5b5600a165627a7a723058206b920fee4013e2461d870b3d74a5c8e7226fd689fd334ff00e247ec8761d4f310029"


opcode_ = opcode.split('6080')
print opcode_
code = Disassembler(opcode).disassemble()
print code
