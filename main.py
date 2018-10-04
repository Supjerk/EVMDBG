from disassembler.disassembler import Disassembler

def get_argument():
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--OPCODE')
    args = parser.parse_args()

    return args


def main():
    args = get_argument()
    file_name = args.OPCODE

    f = open(file_name, 'r')
    opcode = f.read().replace('\n', '')
    
    disas = Disassembler(opcode)
    code = disas.disassemble()

    print '----- CODE -----'
    print code

    f.close()

if __name__ == '__main__':
    main()
